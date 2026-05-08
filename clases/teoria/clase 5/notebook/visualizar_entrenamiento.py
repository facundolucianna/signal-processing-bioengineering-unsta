"""
Visualización paso a paso del entrenamiento de un perceptrón.

Genera un GIF mostrando cómo evoluciona el error y cómo se mueve la
frontera de decisión durante el entrenamiento sobre el dataset Iris
(setosa vs versicolor) usando la Regla del Perceptrón.

Para ejecutar:
    python visualizar_entrenamiento.py
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation, PillowWriter


SCRIPT_DIR = Path(__file__).parent
SEED = 10  # elegida para que la frontera de decisión arranque dentro del área visible


class Perceptron:
    def __init__(self, n_inputs, eta=0.1, max_epochs=50, seed=SEED):
        rng = np.random.default_rng(seed)
        self.W = rng.uniform(-1, 1, size=n_inputs + 1)
        self.eta = eta
        self.max_epochs = max_epochs
        self.snapshots = []

    def _add_bias(self, X):
        return np.hstack([X, np.ones((X.shape[0], 1))])

    def fit(self, X, d):
        Xb = self._add_bias(X)
        n_samples = len(X)
        rng = np.random.default_rng(0)
        errors_per_epoch = []

        # Snapshot inicial (estado antes de entrenar)
        self._snapshot(errors_per_epoch)
        for epoch in range(self.max_epochs):
            errors = 0
            for i in rng.permutation(n_samples):
                x_i, d_i = Xb[i], d[i]
                y_i = 1 if x_i @ self.W >= 0 else 0
                if y_i != d_i:
                    self.W += self.eta * (d_i - y_i) * x_i
                    errors += 1
            errors_per_epoch.append(errors)
            # Snapshot al final de cada época
            self._snapshot(errors_per_epoch)
            if errors == 0:
                print(f"Convergió en la época {epoch + 1}")
                return
        print(f"No convergió tras {self.max_epochs} épocas")

    def _snapshot(self, errors_per_epoch):
        self.snapshots.append({
            "W": self.W.copy(),
            "errors_per_epoch": list(errors_per_epoch),
        })


def main():
    sns.set_style("whitegrid")

    iris = sns.load_dataset("iris")
    mask = iris["species"].isin(["setosa", "versicolor"])
    data = iris[mask].reset_index(drop=True)
    X = data[["petal_length", "petal_width"]].values
    d = (data["species"] == "versicolor").astype(int).values

    perceptron = Perceptron(n_inputs=2, eta=0.002, max_epochs=200)
    perceptron.fit(X, d)
    print(f"Snapshots: {len(perceptron.snapshots)}")

    fig, (ax_err, ax_bnd) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(
        "Entrenamiento paso a paso del perceptrón (setosa vs versicolor)",
        fontsize=13,
        fontweight="bold",
    )

    n_epochs = len(perceptron.snapshots[-1]["errors_per_epoch"])
    max_err = max(
        (max(s["errors_per_epoch"]) for s in perceptron.snapshots if s["errors_per_epoch"]),
        default=10,
    )
    ax_err.set_xlim(0.5, max(n_epochs + 0.5, 2.5))
    ax_err.set_ylim(-0.5, max_err + 2)
    ax_err.set_xlabel("Época")
    ax_err.set_ylabel("Cantidad de muestras mal clasificadas")
    ax_err.set_title("Evolución del error")
    err_line, = ax_err.plot(
        [], [], marker="o", color="#ef6c6c", linewidth=2, markersize=4
    )

    for cls, color, name in zip(
        [0, 1], ["#5ee6a0", "#4da6e8"], ["setosa", "versicolor"]
    ):
        ax_bnd.scatter(
            X[d == cls, 0], X[d == cls, 1],
            color=color, s=60, edgecolor="black", alpha=0.8, label=name,
        )

    x1_min, x1_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    x2_min, x2_max = X[:, 1].min() - 0.3, X[:, 1].max() + 0.3
    ax_bnd.set_xlim(x1_min, x1_max)
    ax_bnd.set_ylim(x2_min, x2_max)
    ax_bnd.set_xlabel("Largo del pétalo (cm)")
    ax_bnd.set_ylabel("Ancho del pétalo (cm)")
    ax_bnd.set_title("Frontera de decisión")
    ax_bnd.legend(loc="upper left")

    boundary_line, = ax_bnd.plot([], [], "k--", linewidth=2)
    info_text = ax_bnd.text(
        0.98, 0.05, "",
        transform=ax_bnd.transAxes,
        fontsize=10,
        ha="right",
        va="bottom",
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85),
    )

    def line_in_box(w1, w2, b):
        """Endpoints of w1*x1 + w2*x2 + b = 0 clipped to the visible bounding box."""
        pts = []
        if abs(w2) > 1e-9:
            for x1 in (x1_min, x1_max):
                x2 = -(w1 * x1 + b) / w2
                if x2_min - 1e-6 <= x2 <= x2_max + 1e-6:
                    pts.append((x1, x2))
        if abs(w1) > 1e-9:
            for x2 in (x2_min, x2_max):
                x1 = -(w2 * x2 + b) / w1
                if x1_min - 1e-6 <= x1 <= x1_max + 1e-6:
                    pts.append((x1, x2))
        return pts[:2]

    def update(frame):
        snap = perceptron.snapshots[frame]
        W = snap["W"]
        errors = snap["errors_per_epoch"]

        if errors:
            err_line.set_data(range(1, len(errors) + 1), errors)

        w1, w2, b = W
        pts = line_in_box(w1, w2, b)
        if len(pts) == 2:
            (a_x, a_y), (b_x, b_y) = pts
            boundary_line.set_data([a_x, b_x], [a_y, b_y])
        else:
            boundary_line.set_data([], [])

        epoch_label = "inicial" if frame == 0 else f"época {frame}"
        info_text.set_text(
            f"{epoch_label:>10s} / {len(perceptron.snapshots) - 1}\n"
            f" w₁ = {w1:+.3f}\n"
            f" w₂ = {w2:+.3f}\n"
            f"  b = {b:+.3f}"
        )
        return err_line, boundary_line, info_text

    n_frames = len(perceptron.snapshots)
    hold_frames = 20
    frame_indices = list(range(n_frames)) + [n_frames - 1] * hold_frames

    anim = FuncAnimation(
        fig, update, frames=frame_indices, interval=80, blit=False
    )

    plt.tight_layout()

    gif_path = SCRIPT_DIR / "entrenamiento_perceptron.gif"
    print(f"Generando GIF: {gif_path}")
    anim.save(str(gif_path), writer=PillowWriter(fps=10))
    print("Listo.")

    plt.show()


if __name__ == "__main__":
    main()
