from IPython.display import display, HTML

def loading_bars(message="", width=200, height=40, bar_height=30, padding_left=0):
    """
    message: texto que aparece arriba de la barra
    width: ancho de la barra
    height: altura del contenedor de la barra
    bar_height: altura visual de las líneas
    padding_left: espacio en píxeles desde la izquierda para el texto
    """
    html_code = f"""
    <style>
    .loader-container {{
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* alineado a la izquierda */
        font-family: Arial, sans-serif;
        font-weight: bold;
        color: #fff; /* texto visible */
        margin-bottom: 8px;
    }}
    .loader-message {{
        margin-bottom: 4px;
        font-size: 16px;
        padding-left: {padding_left}px; /* espacio para centrar el texto */
    }}
    .loader-inline {{
        display: flex;
        align-items: flex-end;
        width: {width}px;
        height: {height}px;
    }}
    .loader-inline div {{
        flex: 1;
        margin: 0 3px;
        background-color: #754fa0;
        animation: stretchdelay 1.2s infinite ease-in-out;
        transform-origin: center bottom;
        height: {bar_height}px;
        border-radius: 4px;
    }}
    .loader-inline div:nth-child(1) {{ background-color: #754fa0; animation-delay: -1.1s; }}
    .loader-inline div:nth-child(2) {{ background-color: #09b7bf; animation-delay: -1.0s; }}
    .loader-inline div:nth-child(3) {{ background-color: #90d36b; animation-delay: -0.9s; }}
    .loader-inline div:nth-child(4) {{ background-color: #f2d40d; animation-delay: -0.8s; }}
    .loader-inline div:nth-child(5) {{ background-color: #fcb12b; animation-delay: -0.7s; }}
    .loader-inline div:nth-child(6) {{ background-color: #ed1b72; animation-delay: -0.6s; }}

    @keyframes stretchdelay {{
        0%, 40%, 100% {{ transform: scaleY(0.2); }}
        20% {{ transform: scaleY(1); }}
    }}
    </style>

    <div class="loader-container">
        <div class="loader-message">{message}</div>
        <div class="loader-inline">
            <div></div><div></div><div></div><div></div><div></div><div></div>
        </div>
    </div>
    """
    display(HTML(html_code))
