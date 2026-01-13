from IPython.display import display, HTML

def loading_ball_box(message, background_color="", font_size="14px"):
    # Colores base y sus tonos más oscuros
    colors = [
        {"base": "#1E3793", "dark": "#12245E"},  # Pelota 1
        {"base": "#4CA8C4", "dark": "#2F6F7F"},  # Pelota 2
        {"base": "#7B26B9", "dark": "#4E1775"},  # Pelota 3
        {"base": "#F069EA", "dark": "#B84FAE"},  # Pelota 4
        {"base": "#FF326B", "dark": "#CC2856"}   # Pelota 5
    ]

    html_code = f"""
    <style>
    @keyframes ballAnimation {{
        0% {{
            transform: scale(1);
            background-color: var(--base-color);
        }}
        50% {{
            transform: scale(1.5);
            background-color: var(--dark-color);
        }}
        100% {{
            transform: scale(1);
            background-color: var(--base-color);
        }}
    }}

    .ball {{
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin: 0 8px; /* Más espacio entre pelotas */
        animation: ballAnimation 1.5s ease-in-out infinite;
        --base-color: {colors[0]['base']};
        --dark-color: {colors[0]['dark']};
    }}

    .ball:nth-child(1) {{
        --base-color: {colors[0]['base']};
        --dark-color: {colors[0]['dark']};
        animation-delay: 0s;
    }}

    .ball:nth-child(2) {{
        --base-color: {colors[1]['base']};
        --dark-color: {colors[1]['dark']};
        animation-delay: 0.3s;
    }}

    .ball:nth-child(3) {{
        --base-color: {colors[2]['base']};
        --dark-color: {colors[2]['dark']};
        animation-delay: 0.6s;
    }}

    .ball:nth-child(4) {{
        --base-color: {colors[3]['base']};
        --dark-color: {colors[3]['dark']};
        animation-delay: 0.9s;
    }}

    .ball:nth-child(5) {{
        --base-color: {colors[4]['base']};
        --dark-color: {colors[4]['dark']};
        animation-delay: 1.2s;
    }}

    </style>
    <div style="
        display: inline-block;
        padding: 8px 12px;
        background-color: {background_color};
        color: white;
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: {font_size};
        text-align: center;
        border-radius: 5px;
        margin: 3px 0;
        position: relative;
    ">
        <span style="letter-spacing: 2px; position: relative; z-index: 1;">{message}</span>
        <div style="margin-top: 8px; display: flex; justify-content: center; align-items: center;">
            <div class="ball"></div>
            <div class="ball"></div>
            <div class="ball"></div>
            <div class="ball"></div>
            <div class="ball"></div>
        </div>
    </div>
    """
    display(HTML(html_code))
