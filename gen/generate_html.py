import re


def parse_markdown(md_text):
    slides = md_text.strip().split("<!-- slide -->")
    # Remove any empty slides at start
    slides = [s for s in slides if s.strip()]
    return slides


def format_inline(text):
    math_placeholders = []
    def save_math(match):
        math_placeholders.append(match.group(0))
        return f"__MATH_IND_{len(math_placeholders)-1}__"

    # Display math
    text = re.sub(r"\$\$(.*?)\$\$", save_math, text)
    # Inline math
    text = re.sub(r"\$(.*?)\$", save_math, text)

    # colors
    text = re.sub(
        r"\{verde\}\((.*?)\)",
        r'<span class="colored-text" style="color: #4ade80;">\1</span>',
        text,
    )
    text = re.sub(
        r"\{amarillo\}\((.*?)\)",
        r'<span class="colored-text" style="color: #fcd34d;">\1</span>',
        text,
    )
    text = re.sub(
        r"\{rojo\}\((.*?)\)",
        r'<span class="colored-text" style="color: #ffa3a3;">\1</span>',
        text,
    )
    text = re.sub(
        r"\{coral\}\((.*?)\)",
        r'<span class="colored-text" style="color: #ffb3b3;">\1</span>',
        text,
    )
    text = re.sub(
        r"\{morado\}\((.*?)\)",
        r'<span class="colored-text" style="color: #c084fc;">\1</span>',
        text,
    )
    text = re.sub(
        r"\{celeste\}\((.*?)\)",
        r'<span class="colored-text" style="color: #38bdf8;">\1</span>',
        text,
    )
    text = re.sub(
        r"\{naranja\}\((.*?)\)",
        r'<span class="colored-text" style="color: #fb923c;">\1</span>',
        text,
    )
    text = re.sub(
        r"\{rosa\}\((.*?)\)",
        r'<span class="colored-text" style="color: #fbcfe8;">\1</span>',
        text,
    )
    text = re.sub(
        r"\{lima\}\((.*?)\)",
        r'<span class="colored-text" style="color: #a3e635;">\1</span>',
        text,
    )

    # bold and italic
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)

    # Inline code
    text = re.sub(r"`(.*?)`", r"<code>\1</code>", text)

    # Restore math
    for i, math_content in enumerate(math_placeholders):
        text = text.replace(f"__MATH_IND_{i}__", math_content)

    return text


def render_slide(slide_content, index):
    lines = slide_content.strip().split("\n")
    lines = [line for line in lines if line.strip() != "---"]

    html = (
        f"    <!-- ===================== SLIDE {index + 1} ===================== -->\n"
    )

    # Check if it's title slide (has <PORTADA> or is the first slide with specific content)
    is_title = False

    if any("<PORTADA>" in line for line in lines):
        is_title = True
    else:
        # Auto-detect section title slide: it has a title but no body text
        has_body = False
        has_title = False
        for line in lines:
            stripped = line.strip()
            if (
                stripped.startswith("### ")
                or stripped.startswith("#### ")
                or stripped.startswith("##### ")
            ):
                has_title = True
            elif stripped.startswith("## Diapositiva"):
                pass
            elif stripped.startswith("<!--"):
                pass
            elif stripped:
                has_body = True

        if has_title and not has_body:
            is_title = True

    if is_title:
        html += f'    <div class="slide slide-title" data-slide="{index}">\n'
        html += '        <div class="slide-inner">\n'
        html += '            <img src="img/unsta-logo-blanco.png" class="logo fragment scale-in" alt="UNSTA Logo" style="height: 200px; width: auto; margin-bottom: 40px;">\n'

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("## "):
                # Skip the slide number heading for portada
                continue
            elif "<PORTADA>" in stripped:
                continue
            elif stripped.startswith("### "):
                # ### now maps to h2 (large title)
                html += f'            <h2 class="fragment">{stripped.replace("### ", "").strip()}</h2>\n'
            elif stripped.startswith("#### "):
                # #### now maps to h1 (smaller pre-title)
                html += f'            <h1 class="fragment">{stripped.replace("#### ", "").strip()}</h1>\n'
            elif stripped.startswith("##### "):
                html += f'            <p class="author fragment">{stripped.replace("##### ", "").strip()}</p>\n'
            elif stripped:
                content = stripped
                content = format_inline(content)
                html += f'            <p class="author fragment">{content}</p>\n'

        html += "        </div>\n"
        html += "    </div>\n"
        return html

    # Normal content slide
    html += f'    <div class="slide slide-content" data-slide="{index}">\n'
    html += '        <div class="slide-inner">\n'

    in_list = False
    in_code_block = False
    code_lang = ""
    code_content = []

    for line in lines:
        stripped_line = line.strip()
        if in_code_block:
            if stripped_line.startswith("```"):
                in_code_block = False
                code_text = "\n".join(code_content)
                code_text = (
                    code_text.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                )
                html += f'            <pre class="fragment"><code class="language-{code_lang}">{code_text}</code></pre>\n'
            else:
                code_content.append(line)
            continue

        if stripped_line.startswith("```"):
            if in_list:
                html += "            </ul>\n"
                in_list = False
            in_code_block = True
            code_lang = stripped_line.replace("```", "").strip()
            code_content = []
            continue

        if stripped_line.startswith("## "):
            pass
        elif stripped_line.startswith("### "):
            if in_list:
                html += "            </ul>\n"
                in_list = False
            html += f'            <h2 class="fragment">{stripped_line.replace("### ", "")}</h2>\n'
        elif stripped_line.startswith("- "):
            if not in_list:
                html += "            <ul>\n"
                in_list = True
            content = stripped_line.replace("- ", "")
            content = format_inline(content)
            html += f'                <li class="fragment">{content}</li>\n'
        elif stripped_line.startswith("![img]") or stripped_line.startswith(
            "![imagen]"
        ):
            if in_list:
                html += "            </ul>\n"
                in_list = False
            match = re.search(r"\!\[.*?\]\((.*?)\)", stripped_line)
            if match:
                img_src = match.group(1)
                html += f'            <img src="{img_src}" class="slide-image-center fragment scale-in" alt="Image">\n'
        else:
            if not stripped_line.startswith("## ") and stripped_line:
                if in_list:
                    html += "            </ul>\n"
                    in_list = False
                content = stripped_line
                content = format_inline(content)
                html += f'            <p class="fragment" style="margin-bottom:14px;">{content}</p>\n'

    if in_list:
        html += "            </ul>\n"

    html += "        </div>\n"
    html += "    </div>\n"
    return html


TEMPLATE_HEADER = '<!DOCTYPE html>\n<html lang="es">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>{page_title}</title>\n    <meta name="description" content="{page_description}">\n    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">\n    <style>\n        /* ============ RESET & BASE ============ */\n        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }\n        html, body { width: 100%; height: 100%; overflow: hidden; font-family: \'Outfit\', sans-serif; }\n\n        /* ============ CSS VARIABLES ============ */\n        :root {\n            --bg-primary: #119de6;\n            --bg-dark: #0b6fa3;\n            --accent-coral: #ef6c6c;\n            --accent-green: #5ee6a0;\n            --accent-blue: #4da6e8;\n            --accent-yellow: #f5c847;\n            --accent-orange: #f5a347;\n            --accent-purple: #9b7dd4;\n            --text-white: #ffffff;\n            --text-light: rgba(255,255,255,0.85);\n            --text-muted: rgba(255,255,255,0.6);\n            --slide-max-width: 1200px;\n        }\n\n        /* ============ PRESENTATION CONTAINER ============ */\n        #presentation {\n            width: 100vw;\n            height: 100vh;\n            position: relative;\n            background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-dark) 100%);\n        }\n\n        /* ============ DECORATIVE BACKGROUND ============ */\n        .bg-decoration {\n            position: fixed;\n            top: 0; left: 0; right: 0; bottom: 0;\n            pointer-events: none;\n            z-index: 0;\n            overflow: hidden;\n        }\n        .bg-stripe {\n            position: absolute;\n            border-radius: 30px;\n            opacity: 0.12;\n            transform: rotate(-45deg);\n        }\n        .bg-stripe:nth-child(1)  { width: 60px;  height: 350px; background: var(--accent-coral);  top: 10%; right: 5%; }\n        .bg-stripe:nth-child(2)  { width: 50px;  height: 280px; background: var(--accent-green);  top: 25%; right: 12%; }\n        .bg-stripe:nth-child(3)  { width: 45px;  height: 220px; background: var(--accent-blue);   top: 40%; right: 3%; }\n        .bg-stripe:nth-child(4)  { width: 55px;  height: 300px; background: var(--accent-yellow); top: 55%; right: 18%; }\n        .bg-stripe:nth-child(5)  { width: 40px;  height: 250px; background: var(--accent-purple); top: 15%; right: 25%; }\n        .bg-stripe:nth-child(6)  { width: 35px;  height: 180px; background: var(--accent-orange); top: 60%; right: 8%; }\n        .bg-dot {\n            position: absolute;\n            border-radius: 50%;\n            opacity: 0.15;\n        }\n        .bg-dot:nth-child(7)  { width: 25px; height: 25px; background: var(--accent-green);  top: 12%; right: 30%; }\n        .bg-dot:nth-child(8)  { width: 18px; height: 18px; background: var(--accent-coral);  top: 35%; right: 22%; }\n        .bg-dot:nth-child(9)  { width: 20px; height: 20px; background: var(--accent-yellow); top: 70%; right: 15%; }\n        .bg-dot:nth-child(10) { width: 22px; height: 22px; background: var(--accent-blue);   top: 80%; left: 8%; }\n        .bg-dot:nth-child(11) { width: 15px; height: 15px; background: var(--accent-orange); top: 50%; left: 4%; }\n\n        /* ============ SLIDE ============ */\n        .slide {\n            position: absolute;\n            top: 0; left: 0;\n            width: 100%; height: 100%;\n            display: flex;\n            align-items: center;\n            justify-content: center;\n            opacity: 0;\n            visibility: hidden;\n            transition: opacity 0.6s ease, visibility 0.6s ease, transform 0.6s ease;\n            transform: translateX(60px);\n            z-index: 1;\n            padding: 60px 80px;\n        }\n        .slide.active {\n            opacity: 1;\n            visibility: visible;\n            transform: translateX(0);\n            z-index: 2;\n        }\n        .slide.exit-left {\n            opacity: 0;\n            visibility: hidden;\n            transform: translateX(-60px);\n        }\n\n        .slide-inner {\n            max-width: var(--slide-max-width);\n            width: 100%;\n            position: relative;\n        }\n\n        /* ============ TITLE SLIDE ============ */\n        .slide-title {\n            text-align: center;\n        }\n        .slide-title .logo {\n            width: 120px;\n            height: 120px;\n            margin-bottom: 30px;\n            filter: drop-shadow(0 4px 20px rgba(0,0,0,0.3));\n            animation: float 3s ease-in-out infinite;\n        }\n        @keyframes float {\n            0%, 100% { transform: translateY(0); }\n            50% { transform: translateY(-10px); }\n        }\n        .slide-title h1 {\n            font-size: 2rem;\n            font-weight: 300;\n            color: var(--text-muted);\n            text-transform: uppercase;\n            letter-spacing: 6px;\n            margin-bottom: 10px;\n        }\n        .slide-title h2 {\n            font-size: 4rem;\n            font-weight: 800;\n            color: var(--text-white);\n            margin-bottom: 25px;\n            line-height: 1.2;\n            padding-bottom: 6px;\n            background: linear-gradient(135deg, #fff 0%, var(--accent-green) 50%, var(--accent-blue) 100%);\n            -webkit-background-clip: text;\n            -webkit-text-fill-color: transparent;\n            background-clip: text;\n        }\n        .slide-title .author {\n            font-size: 1.15rem;\n            color: var(--text-light);\n            font-weight: 300;\n        }\n        .slide-title .author span {\n            color: var(--accent-green);\n            font-weight: 500;\n        }\n\n        /* ============ SECTION SLIDE ============ */\n        .slide-section {\n            text-align: center;\n        }\n        .slide-section h2 {\n            font-size: 3.5rem;\n            font-weight: 800;\n            color: var(--text-white);\n            margin-bottom: 10px;\n            line-height: 1.1;\n        }\n        .slide-section .section-line {\n            width: 80px;\n            height: 4px;\n            border-radius: 4px;\n            margin: 20px auto;\n            background: linear-gradient(90deg, var(--accent-coral), var(--accent-yellow));\n        }\n\n        /* ============ CONTENT SLIDE ============ */\n        .slide-content h3 {\n            font-size: 1rem;\n            font-weight: 500;\n            color: var(--accent-green);\n            text-transform: uppercase;\n            letter-spacing: 3px;\n            margin-bottom: 6px;\n        }\n        .slide-content h2 {\n            font-size: 2.4rem;\n            font-weight: 700;\n            color: var(--text-white);\n            margin-bottom: 28px;\n            line-height: 1.2;\n        }\n        .slide-content p, .slide-content li {\n            font-family: \'Inter\', sans-serif;\n            font-size: 1.15rem;\n            line-height: 1.75;\n            color: var(--text-light);\n        }\n        .slide-content ul {\n            list-style: none;\n            padding: 0;\n        }\n        .slide-content ul li {\n            position: relative;\n            padding-left: 28px;\n            margin-bottom: 14px;\n        }\n        .slide-content ul li::before {\n            content: \'\';\n            position: absolute;\n            left: 0;\n            top: 10px;\n            width: 10px;\n            height: 10px;\n            border-radius: 50%;\n            background: var(--accent-green);\n        }\n        .slide-content ul ul li::before {\n            background: var(--accent-blue);\n            width: 8px;\n            height: 8px;\n            top: 11px;\n        }\n        .slide-content ul ul {\n            margin-top: 8px;\n        }\n\n        .slide-content strong {\n            color: var(--text-white);\n            font-weight: 600;\n        }\n\n        .slide-content blockquote {\n            border-left: 4px solid var(--accent-coral);\n            padding: 16px 20px;\n            margin: 20px 0;\n            background: rgba(255,255,255,0.05);\n            border-radius: 0 12px 12px 0;\n            font-style: italic;\n            color: var(--text-light);\n            font-family: \'Inter\', sans-serif;\n            font-size: 1.1rem;\n            line-height: 1.6;\n        }\n\n        .slide-content a {\n            color: var(--accent-blue);\n            text-decoration: none;\n            border-bottom: 1px solid transparent;\n            transition: border-color 0.3s;\n        }\n        .slide-content a:hover {\n            border-bottom-color: var(--accent-blue);\n        }\n\n        .slide-content ol {\n            padding-left: 28px;\n            color: var(--text-light);\n            font-family: \'Inter\', sans-serif;\n        }\n        .slide-content ol li {\n            margin-bottom: 14px;\n            font-size: 1.15rem;\n            line-height: 1.75;\n        }\n        .slide-content ol li::marker {\n            color: var(--accent-yellow);\n            font-weight: 700;\n        }\n\n        /* ============ TWO COLUMN LAYOUT ============ */\n        .two-col {\n            display: grid;\n            grid-template-columns: 1fr 1fr;\n            gap: 50px;\n            align-items: center;\n        }\n        .two-col.text-heavy {\n            grid-template-columns: 1.3fr 0.7fr;\n        }\n\n        .slide-content .slide-image {\n            width: 100%;\n            max-height: 420px;\n            object-fit: contain;\n            border-radius: 16px;\n            box-shadow: 0 8px 40px rgba(0,0,0,0.3);\n        }\n        .slide-content .slide-image-full {\n            display: block;\n            max-width: 80%;\n            max-height: 55vh;\n            margin: 24px auto 0;\n            object-fit: contain;\n            border-radius: 16px;\n            box-shadow: 0 8px 40px rgba(0,0,0,0.3);\n        }\n        .slide-content .slide-image-center {\n            display: block;\n            max-width: 70%;\n            max-height: 65vh;\n            margin: 0 auto;\n            object-fit: contain;\n            border-radius: 16px;\n            box-shadow: 0 8px 40px rgba(0,0,0,0.3);\n        }\n\n        /* ============ FRAGMENT ANIMATIONS ============ */\n        .fragment {\n            opacity: 0;\n            transform: translateY(25px);\n            transition: opacity 0.5s ease, transform 0.5s ease;\n        }\n        .fragment.visible {\n            opacity: 1;\n            transform: translateY(0);\n        }\n        .fragment.fade-left {\n            transform: translateX(-30px);\n        }\n        .fragment.fade-left.visible {\n            transform: translateX(0);\n        }\n        .fragment.fade-right {\n            transform: translateX(30px);\n        }\n        .fragment.fade-right.visible {\n            transform: translateX(0);\n        }\n        .fragment.scale-in {\n            transform: scale(0.85);\n        }\n        .fragment.scale-in.visible {\n            transform: scale(1);\n        }\n\n        /* ============ HEADER BAR ============ */\n        .header-bar {\n            position: fixed;\n            top: 0; left: 0; right: 0;\n            height: 50px;\n            background: rgba(0,0,0,0.2);\n            backdrop-filter: blur(20px);\n            -webkit-backdrop-filter: blur(20px);\n            display: flex;\n            align-items: center;\n            justify-content: space-between;\n            padding: 0 30px;\n            z-index: 100;\n        }\n        .header-bar .header-logo {\n            height: 32px;\n            opacity: 0.9;\n        }\n        .header-bar .header-title {\n            font-size: 0.85rem;\n            color: var(--text-muted);\n            letter-spacing: 2px;\n            text-transform: uppercase;\n            font-weight: 400;\n        }\n\n        /* ============ PROGRESS BAR ============ */\n        .progress-bar {\n            position: fixed;\n            bottom: 0; left: 0;\n            height: 4px;\n            background: linear-gradient(90deg, var(--accent-green), var(--accent-blue), var(--accent-coral));\n            z-index: 100;\n            transition: width 0.4s ease;\n            border-radius: 0 4px 4px 0;\n        }\n\n        /* ============ CONTROLS ============ */\n        .controls {\n            position: fixed;\n            bottom: 30px;\n            right: 30px;\n            display: flex;\n            gap: 10px;\n            z-index: 100;\n        }\n        .controls button {\n            width: 48px;\n            height: 48px;\n            border-radius: 50%;\n            border: none;\n            background: rgba(255,255,255,0.1);\n            backdrop-filter: blur(10px);\n            color: var(--text-white);\n            font-size: 1.2rem;\n            cursor: pointer;\n            transition: all 0.3s ease;\n            display: flex;\n            align-items: center;\n            justify-content: center;\n        }\n        .controls button:hover {\n            background: rgba(255,255,255,0.25);\n            transform: scale(1.1);\n        }\n\n        .slide-counter {\n            position: fixed;\n            bottom: 38px;\n            left: 30px;\n            color: var(--text-muted);\n            font-size: 0.85rem;\n            font-weight: 400;\n            z-index: 100;\n            letter-spacing: 1px;\n        }\n\n        /* ============ OVERVIEW MODE ============ */\n        .overview-mode .slide {\n            position: relative !important;\n            width: calc(25% - 20px) !important;\n            height: 180px !important;\n            display: inline-block !important;\n            opacity: 1 !important;\n            visibility: visible !important;\n            transform: none !important;\n            margin: 10px;\n            overflow: hidden;\n            border-radius: 12px;\n            cursor: pointer;\n            border: 2px solid transparent;\n            transition: border-color 0.3s;\n            padding: 10px !important;\n        }\n        .overview-mode .slide:hover {\n            border-color: var(--accent-green);\n        }\n        .overview-mode .slide.active {\n            border-color: var(--accent-coral);\n        }\n        .overview-mode .slide * {\n            font-size: 30% !important;\n        }\n        .overview-mode {\n            overflow-y: auto !important;\n            padding: 60px 20px 20px !important;\n        }\n\n        /* ============ RESPONSIVE ============ */\n        @media (max-width: 900px) {\n            .slide { padding: 50px 30px; }\n            .slide-title h2 { font-size: 2.5rem; }\n            .slide-section h2 { font-size: 2.5rem; }\n            .slide-content h2 { font-size: 1.8rem; }\n            .two-col { grid-template-columns: 1fr; gap: 24px; }\n            .two-col.text-heavy { grid-template-columns: 1fr; }\n        }\n\n        /* ============ TOOLTIP HELP ============ */\n        .help-tooltip {\n            position: fixed;\n            bottom: 90px;\n            right: 30px;\n            background: rgba(0,0,0,0.8);\n            backdrop-filter: blur(10px);\n            color: var(--text-light);\n            padding: 16px 20px;\n            border-radius: 12px;\n            font-size: 0.85rem;\n            line-height: 1.7;\n            z-index: 200;\n            opacity: 0;\n            transform: translateY(10px);\n            transition: all 0.3s ease;\n            pointer-events: none;\n            font-family: \'Inter\', sans-serif;\n        }\n        .help-tooltip.show {\n            opacity: 1;\n            transform: translateY(0);\n        }\n        .help-tooltip kbd {\n            background: rgba(255,255,255,0.15);\n            padding: 2px 8px;\n            border-radius: 4px;\n            font-family: \'Inter\', sans-serif;\n            font-size: 0.8rem;\n        }\n\n        /* ============ PRINT ============ */\n        @media print {\n            .slide { page-break-after: always; position: relative !important; opacity: 1 !important; visibility: visible !important; transform: none !important; height: 100vh !important; }\n            .header-bar, .progress-bar, .controls, .slide-counter, .help-tooltip, .goto-overlay { display: none !important; }\n        }\n\n        /* ============ DUAL IMAGE SIDE BY SIDE ============ */\n        .dual-image {\n            display: flex;\n            gap: 30px;\n            align-items: center;\n            justify-content: center;\n            margin-top: 20px;\n        }\n        .dual-image img {\n            max-width: 45%;\n            max-height: 300px;\n            object-fit: contain;\n            border-radius: 12px;\n            box-shadow: 0 8px 30px rgba(0,0,0,0.3);\n        }\n\n        /* ============ GO-TO-SLIDE OVERLAY ============ */\n        .goto-overlay {\n            position: fixed;\n            top: 0; left: 0; right: 0; bottom: 0;\n            background: rgba(0,0,0,0.5);\n            backdrop-filter: blur(8px);\n            -webkit-backdrop-filter: blur(8px);\n            z-index: 300;\n            display: flex;\n            align-items: center;\n            justify-content: center;\n            opacity: 0;\n            visibility: hidden;\n            transition: opacity 0.25s ease, visibility 0.25s ease;\n        }\n        .goto-overlay.show {\n            opacity: 1;\n            visibility: visible;\n        }\n        .goto-box {\n            background: rgba(11, 111, 163, 0.9);\n            backdrop-filter: blur(20px);\n            -webkit-backdrop-filter: blur(20px);\n            border: 1px solid rgba(255,255,255,0.12);\n            border-radius: 16px;\n            padding: 28px 36px;\n            text-align: center;\n            transform: translateY(20px);\n            transition: transform 0.25s ease;\n            min-width: 280px;\n        }\n        .goto-overlay.show .goto-box {\n            transform: translateY(0);\n        }\n        .goto-box label {\n            display: block;\n            font-family: \'Outfit\', sans-serif;\n            font-size: 0.85rem;\n            color: var(--text-muted);\n            text-transform: uppercase;\n            letter-spacing: 2px;\n            margin-bottom: 14px;\n        }\n        .goto-box input {\n            width: 100%;\n            padding: 12px 16px;\n            border: 2px solid rgba(255,255,255,0.15);\n            border-radius: 10px;\n            background: rgba(255,255,255,0.07);\n            color: var(--text-white);\n            font-family: \'Outfit\', sans-serif;\n            font-size: 1.6rem;\n            font-weight: 600;\n            text-align: center;\n            outline: none;\n            transition: border-color 0.3s;\n        }\n        .goto-box input:focus {\n            border-color: var(--accent-green);\n        }\n        .goto-box input::placeholder {\n            color: var(--text-muted);\n            font-weight: 300;\n            font-size: 1rem;\n        }\n        .goto-box .goto-hint {\n            margin-top: 12px;\n            font-size: 0.78rem;\n            color: var(--text-muted);\n            font-family: \'Inter\', sans-serif;\n        }\n        .goto-box .goto-hint kbd {\n            background: rgba(255,255,255,0.12);\n            padding: 2px 7px;\n            border-radius: 4px;\n            font-family: \'Inter\', sans-serif;\n            font-size: 0.75rem;\n        }\n    </style>\n    <style>\n        .colored-text strong, .colored-text em {\n            color: inherit !important;\n        }\n        code {\n            font-family: monospace;\n            background: rgba(255, 255, 255, 0.15);\n            padding: 3px 6px;\n            border-radius: 4px;\n            font-size: 0.92em;\n            color: var(--accent-yellow);\n        }\n        pre {\n            background: rgba(0, 0, 0, 0.4);\n            padding: 16px;\n            border-radius: 12px;\n            overflow-x: auto;\n            margin: 15px 0;\n            border: 1px solid rgba(255,255,255,0.1);\n            box-shadow: 0 4px 20px rgba(0,0,0,0.2);\n        }\n        pre code {\n            background: none !important;\n            padding: 0 !important;\n            font-size: 0.95em;\n            color: var(--text-white);\n            font-family: monospace;\n            display: block;\n        }\n    </style>\n    <script>\n      window.MathJax = {\n        tex: {\n          inlineMath: [[\'$\', \'$\'], [\'\\\\(\', \'\\\\)\']],\n          displayMath: [[\'$$\', \'$$\'], [\'\\\\[\', \'\\\\]\']]\n        }\n      };\n    </script>\n    <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js\"></script>\n</head>\n<body>\n\n<!-- ========== HEADER BAR ========== -->\n<div class="header-bar">\n    <img src="img/unsta-logo-peq.png" class="header-logo" alt="UNSTA Logo">\n    <span class="header-title">{header_title}</span>\n</div>\n\n<!-- ========== PROGRESS BAR ========== -->\n<div class="progress-bar" id="progressBar"></div>\n\n<!-- ========== SLIDE COUNTER ========== -->\n<div class="slide-counter" id="slideCounter"></div>\n\n<!-- ========== HELP TOOLTIP ========== -->\n<div class="help-tooltip" id="helpTooltip">\n    <kbd>←</kbd> <kbd>→</kbd> Navegar &nbsp;|&nbsp;\n    <kbd>Space</kbd> Fragmento / Siguiente<br>\n    <kbd>F</kbd> Pantalla completa &nbsp;|&nbsp;\n    <kbd>G</kbd> Ir a diapositiva<br>\n    <kbd>?</kbd> Mostrar / ocultar ayuda\n</div>\n\n<!-- ========== GO TO SLIDE OVERLAY ========== -->\n<div class="goto-overlay" id="gotoOverlay">\n    <div class="goto-box">\n        <label for="gotoInput">Ir a diapositiva</label>\n        <input type="number" id="gotoInput" min="1" placeholder="1–30" autocomplete="off">\n        <div class="goto-hint"><kbd>Enter</kbd> para ir &nbsp;|&nbsp; <kbd>Esc</kbd> para cerrar</div>\n    </div>\n</div>\n\n<!-- ========== PRESENTATION ========== -->\n<div id="presentation">\n\n    <!-- Background decoration -->\n    <div class="bg-decoration">\n        <div class="bg-stripe"></div>\n        <div class="bg-stripe"></div>\n        <div class="bg-stripe"></div>\n        <div class="bg-stripe"></div>\n        <div class="bg-stripe"></div>\n        <div class="bg-stripe"></div>\n        <div class="bg-dot"></div>\n        <div class="bg-dot"></div>\n        <div class="bg-dot"></div>\n        <div class="bg-dot"></div>\n        <div class="bg-dot"></div>\n    </div>\n\n    '

TEMPLATE_FOOTER = (
    "</div><!-- /presentation -->"
    + "\n\n<!-- ========== CONTROLS ========== -->\n<div class=\"controls\">\n    <button id=\"btnPrev\" title=\"Anterior\" aria-label=\"Diapositiva anterior\">&#9664;</button>\n    <button id=\"btnNext\" title=\"Siguiente\" aria-label=\"Diapositiva siguiente\">&#9654;</button>\n</div>\n\n<script>\n(function() {\n    'use strict';\n\n    const slides = document.querySelectorAll('.slide');\n    const totalSlides = slides.length;\n    let currentSlide = 0;\n    let isAnimating = false;\n\n    const progressBar = document.getElementById('progressBar');\n    const slideCounter = document.getElementById('slideCounter');\n    const btnPrev = document.getElementById('btnPrev');\n    const btnNext = document.getElementById('btnNext');\n    const helpTooltip = document.getElementById('helpTooltip');\n\n    // ========== FRAGMENT MANAGEMENT ==========\n    function getFragments(slideEl) {\n        return Array.from(slideEl.querySelectorAll('.fragment'));\n    }\n\n    function getNextHiddenFragment(slideEl) {\n        const fragments = getFragments(slideEl);\n        return fragments.find(f => !f.classList.contains('visible'));\n    }\n\n    function showAllFragments(slideEl) {\n        getFragments(slideEl).forEach((f, i) => {\n            setTimeout(() => f.classList.add('visible'), i * 60);\n        });\n    }\n\n    function showAllFragmentsInstant(slideEl) {\n        getFragments(slideEl).forEach(f => f.classList.add('visible'));\n    }\n\n    function hideAllFragments(slideEl) {\n        getFragments(slideEl).forEach(f => f.classList.remove('visible'));\n    }\n\n    function hasHiddenFragments(slideEl) {\n        return !!getNextHiddenFragment(slideEl);\n    }\n\n    function revealNextFragment(slideEl) {\n        const frag = getNextHiddenFragment(slideEl);\n        if (frag) {\n            frag.classList.add('visible');\n            return true;\n        }\n        return false;\n    }\n\n    function hideLastVisibleFragment(slideEl) {\n        const fragments = getFragments(slideEl);\n        const visibleFragments = fragments.filter(f => f.classList.contains('visible'));\n        if (visibleFragments.length > 0) {\n            visibleFragments[visibleFragments.length - 1].classList.remove('visible');\n            return true;\n        }\n        return false;\n    }\n\n    // ========== SLIDE NAVIGATION ==========\n    function updateUI() {\n        const progress = ((currentSlide + 1) / totalSlides) * 100;\n        progressBar.style.width = progress + '%';\n        slideCounter.textContent = (currentSlide + 1) + ' / ' + totalSlides;\n    }\n\n    function goToSlide(n, direction) {\n        if (n < 0 || n >= totalSlides || isAnimating) return;\n        isAnimating = true;\n\n        const prevSlide = slides[currentSlide];\n        const nextSlide = slides[n];\n\n        // Add exit class\n        if (direction === 'forward') {\n            prevSlide.classList.add('exit-left');\n        }\n        prevSlide.classList.remove('active');\n\n        // Prepare next slide fragments\n        hideAllFragments(nextSlide);\n        nextSlide.classList.remove('exit-left');\n        nextSlide.classList.add('active');\n\n        // Show fragments with stagger\n        showAllFragments(nextSlide);\n\n        currentSlide = n;\n        updateUI();\n\n        setTimeout(() => {\n            prevSlide.classList.remove('exit-left');\n            isAnimating = false;\n        }, 600);\n    }\n\n    function nextAction() {\n        const current = slides[currentSlide];\n        if (hasHiddenFragments(current)) {\n            revealNextFragment(current);\n        } else if (currentSlide < totalSlides - 1) {\n            goToSlide(currentSlide + 1, 'forward');\n        }\n    }\n\n    function prevAction() {\n        const current = slides[currentSlide];\n        if (hideLastVisibleFragment(current)) {\n            // Just hid a fragment, stay on same slide\n        } else if (currentSlide > 0) {\n            goToSlide(currentSlide - 1, 'backward');\n            // Show all fragments of the previous slide instantly\n            setTimeout(() => {\n                showAllFragmentsInstant(slides[currentSlide]);\n            }, 100);\n        }\n    }\n\n    // ========== EVENT LISTENERS ==========\n    document.addEventListener('keydown', function(e) {\n        // Only trigger if no modifier keys are pressed (Cmd, Ctrl, Alt)\n        if (e.metaKey || e.ctrlKey || e.altKey) return;\n\n        switch(e.key) {\n            case 'ArrowRight':\n            case 'ArrowDown':\n            case ' ':\n            case 'Enter':\n                e.preventDefault();\n                nextAction();\n                break;\n            case 'ArrowLeft':\n            case 'ArrowUp':\n            case 'Backspace':\n                e.preventDefault();\n                prevAction();\n                break;\n            case 'Home':\n                e.preventDefault();\n                goToSlide(0, 'backward');\n                break;\n            case 'End':\n                e.preventDefault();\n                goToSlide(totalSlides - 1, 'forward');\n                break;\n            case 'f':\n            case 'F':\n                e.preventDefault();\n                toggleFullscreen();\n                break;\n            case 'g':\n            case 'G':\n                e.preventDefault();\n                showGotoOverlay();\n                break;\n            case '?':\n                e.preventDefault();\n                helpTooltip.classList.toggle('show');\n                break;\n            case 'Escape':\n                helpTooltip.classList.remove('show');\n                hideGotoOverlay();\n                break;\n        }\n    });\n\n    btnNext.addEventListener('click', nextAction);\n    btnPrev.addEventListener('click', prevAction);\n\n    // Touch support\n    let touchStartX = 0;\n    let touchStartY = 0;\n    document.addEventListener('touchstart', function(e) {\n        touchStartX = e.changedTouches[0].screenX;\n        touchStartY = e.changedTouches[0].screenY;\n    }, { passive: true });\n    document.addEventListener('touchend', function(e) {\n        const dx = e.changedTouches[0].screenX - touchStartX;\n        const dy = e.changedTouches[0].screenY - touchStartY;\n        if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 50) {\n            if (dx < 0) nextAction();\n            else prevAction();\n        }\n    }, { passive: true });\n\n    // ========== FULLSCREEN ==========\n    function toggleFullscreen() {\n        if (!document.fullscreenElement && !document.webkitFullscreenElement && \n            !document.mozFullScreenElement && !document.msFullscreenElement) {\n            const el = document.documentElement;\n            if (el.requestFullscreen) {\n                el.requestFullscreen().catch(err => {\n                    console.error(`Error attempting to enable full-screen mode: ${err.message} (${err.name})`);\n                });\n            } else if (el.webkitRequestFullscreen) {\n                el.webkitRequestFullscreen();\n            } else if (el.mozRequestFullScreen) {\n                el.mozRequestFullScreen();\n            } else if (el.msRequestFullscreen) {\n                el.msRequestFullscreen();\n            }\n        } else {\n            if (document.exitFullscreen) {\n                document.exitFullscreen().catch(err => {\n                    console.error(`Error attempting to exit full-screen mode: ${err.message} (${err.name})`);\n                });\n            } else if (document.webkitExitFullscreen) {\n                document.webkitExitFullscreen();\n            } else if (document.mozCancelFullScreen) {\n                document.mozCancelFullScreen();\n            } else if (document.msExitFullscreen) {\n                document.msExitFullscreen();\n            }\n        }\n    }\n\n    // ========== GO TO SLIDE ==========\n    const gotoOverlay = document.getElementById('gotoOverlay');\n    const gotoInput = document.getElementById('gotoInput');\n    let gotoActive = false;\n\n    function showGotoOverlay() {\n        if (gotoActive) return;\n        gotoActive = true;\n        gotoInput.max = totalSlides;\n        gotoInput.placeholder = '1–' + totalSlides;\n        gotoInput.value = '';\n        gotoOverlay.classList.add('show');\n        setTimeout(() => gotoInput.focus(), 50);\n    }\n\n    function hideGotoOverlay() {\n        gotoActive = false;\n        gotoOverlay.classList.remove('show');\n        gotoInput.blur();\n    }\n\n    gotoInput.addEventListener('keydown', function(e) {\n        e.stopPropagation(); // prevent slide navigation keys while typing\n        if (e.key === 'Enter') {\n            e.preventDefault();\n            const n = parseInt(gotoInput.value, 10);\n            if (n >= 1 && n <= totalSlides) {\n                const direction = n - 1 > currentSlide ? 'forward' : 'backward';\n                goToSlide(n - 1, direction);\n            }\n            hideGotoOverlay();\n        } else if (e.key === 'Escape') {\n            e.preventDefault();\n            hideGotoOverlay();\n        }\n    });\n\n    gotoOverlay.addEventListener('click', function(e) {\n        if (e.target === gotoOverlay) hideGotoOverlay();\n    });\n\n    // Also allow clicking the slide counter to open goto\n    slideCounter.style.cursor = 'pointer';\n    slideCounter.addEventListener('click', showGotoOverlay);\n\n    // ========== INIT ==========\n    slides[0].classList.add('active');\n    showAllFragments(slides[0]);\n    updateUI();\n\n})();\n</script>\n</body>\n</html>\n"
)


def generate_html(md_path, html_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    slides = parse_markdown(md_text)

    # Extract dynamic titles from the first slide
    page_title = "Clase"
    page_description = "Presentación de la clase"
    header_title = "Clase — UNSTA"

    if slides:
        first_slide_lines = slides[0].split("\n")
        h3_text = ""
        h4_text = ""
        h5_text = ""
        for line in first_slide_lines:
            if line.startswith("### "):
                h3_text = line.replace("### ", "").strip()
            elif line.startswith("#### "):
                h4_text = line.replace("#### ", "").strip()
            elif line.startswith("##### ") and not h5_text:
                h5_text = line.replace("##### ", "").strip()

        if h4_text:
            cleaned_h3 = h3_text.replace("*", "").replace("_", "")
            cleaned_h4 = h4_text.replace("*", "").replace("_", "")
            page_title = f"{cleaned_h4} | {cleaned_h3}" if cleaned_h3 else cleaned_h4
            # Keep semantic markers out of document titles
            page_title = re.sub(r"\{[^\}]+\}\(", "", page_title).replace(")", "")

            cleaned_h5 = h5_text.replace("*", "").replace("_", "")
            institution = (
                cleaned_h5.split(" - ")[-1] if " - " in cleaned_h5 else "UNSTA"
            )
            header_title = f"{cleaned_h4} — {institution}"
            header_title = re.sub(r"\{[^\}]+\}\(", "", header_title).replace(")", "")

            page_description = f"{cleaned_h3} - {cleaned_h4} - {cleaned_h5}"
            page_description = re.sub(r"\{[^\}]+\}\(", "", page_description).replace(
                ")", ""
            )

    slides_html = ""
    for i, slide in enumerate(slides):
        if i == 0 and "<PORTADA>" not in slide:
            slide = slide + "\n<PORTADA>"
        slides_html += render_slide(slide, i) + "\n"

    final_slide_index = len(slides)
    # The Thank you slide can also dynamically use the extracted title
    thanks_h1 = (
        re.sub(r"\{[^\}]+\}\(", "", h4_text).replace(")", "")
        if h4_text
        else "Análisis y procesamiento de Señales"
    )
    thanks_p = (
        re.sub(r"\{[^\}]+\}\(", "", h5_text).replace(")", "")
        if h5_text
        else "Bioingeniería - Facultad de Ingeniería - UNSTA"
    )

    thanks_html = (
        f"    <!-- ===================== SLIDE {final_slide_index + 1}: CIERRE ===================== -->\n"
        f'    <div class="slide slide-title" data-slide="{final_slide_index}">\n'
        f'        <div class="slide-inner">\n'
        f'            <img src="img/unsta-logo-blanco.png" class="logo fragment scale-in" alt="UNSTA Logo" style="height: 200px; width: auto; margin-bottom: 40px;">\n'
        f'            <h2 class="fragment">Muchas gracias</h2>\n'
        f'            <h1 class="fragment" style="margin-bottom:20px;">{thanks_h1}</h1>\n'
        f'            <p class="author fragment">{thanks_p}</p>\n'
        f"        </div>\n"
        f"    </div>\n\n"
    )
    slides_html += thanks_html

    header_html = (
        TEMPLATE_HEADER.replace("{page_title}", page_title)
        .replace("{page_description}", page_description)
        .replace("{header_title}", header_title)
    )
    final_output = header_html + slides_html + TEMPLATE_FOOTER

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(final_output)


if __name__ == "__main__":
    import os
    import sys

    if len(sys.argv) < 3:
        print(
            "Uso: python3 generate_html.py <archivo_markdown.md> <archivo_salida.html>"
        )
        sys.exit(1)

    md_file = os.path.abspath(sys.argv[1])
    html_file = os.path.abspath(sys.argv[2])

    generate_html(md_file, html_file)
    print(f"HTML generado en: {html_file}")
