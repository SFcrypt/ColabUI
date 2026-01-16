from IPython.display import display, HTML

# Barras de progreso
def loading_bars(width=200, height=40):
    html_code = f"""
    <style>
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
        height: 40%;  /* altura inicial más grande */
        border-radius: 4px;
    }}
    .loader-inline div:nth-child(1) {{ background-color: #754fa0; animation-delay: -1.1s; }}
    .loader-inline div:nth-child(2) {{ background-color: #09b7bf; animation-delay: -1.0s; }}
    .loader-inline div:nth-child(3) {{ background-color: #90d36b; animation-delay: -0.9s; }}
    .loader-inline div:nth-child(4) {{ background-color: #f2d40d; animation-delay: -0.8s; }}
    .loader-inline div:nth-child(5) {{ background-color: #fcb12b; animation-delay: -0.7s; }}
    .loader-inline div:nth-child(6) {{ background-color: #ed1b72; animation-delay: -0.6s; }}

    @keyframes stretchdelay {{
        0%, 40%, 100% {{ transform: scaleY(0.1); }}
        20% {{ transform: scaleY(1); }}
    }}
    </style>

    <div class="loader-inline">
        <div></div><div></div><div></div><div></div><div></div><div></div>
    </div>
    """
    display(HTML(html_code))
