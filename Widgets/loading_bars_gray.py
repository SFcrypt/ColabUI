from IPython.display import display, HTML

def loading_bars_gray(message="Procesando...", width=200, height=40, bar_height=30, padding_left=0):
    html_code = f"""
    <style>
    .loader-gray-container {{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        font-family: Arial, sans-serif;
        font-weight: bold;
        color: #fff;
        margin-bottom: 8px;
    }}
    .loader-gray-message {{
        margin-bottom: 4px;
        font-size: 16px;
        padding-left: {padding_left}px;
    }}
    .loader-gray-inline {{
        display: flex;
        align-items: flex-end;
        width: {width}px;
        height: {height}px;
    }}
    .loader-gray-inline div {{
        flex: 1;
        margin: 0 3px;
        animation: graystretch 1.2s infinite ease-in-out;
        transform-origin: center bottom;
        height: {bar_height}px;
        border-radius: 4px;
    }}
    /* tonos de gris medios para todas las barras */
    .loader-gray-inline div:nth-child(1) {{ background-color: #555; animation-delay: -1.1s; }}
    .loader-gray-inline div:nth-child(2) {{ background-color: #5a5a5a; animation-delay: -1.0s; }}
    .loader-gray-inline div:nth-child(3) {{ background-color: #606060; animation-delay: -0.9s; }}
    .loader-gray-inline div:nth-child(4) {{ background-color: #666; animation-delay: -0.8s; }}
    .loader-gray-inline div:nth-child(5) {{ background-color: #6b6b6b; animation-delay: -0.7s; }}
    .loader-gray-inline div:nth-child(6) {{ background-color: #707070; animation-delay: -0.6s; }}

    @keyframes graystretch {{
        0%, 40%, 100% {{ transform: scaleY(0.2); }}
        20% {{ transform: scaleY(1); }}
    }}
    </style>

    <div class="loader-gray-container">
        <div class="loader-gray-message">{message}</div>
        <div class="loader-gray-inline">
            <div></div><div></div><div></div><div></div><div></div><div></div>
        </div>
    </div>
    """
    display(HTML(html_code))
