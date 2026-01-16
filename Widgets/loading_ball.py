from IPython.display import display, HTML

# Pelotas de progreso
def loading_ball():
    colors = [
        {"base": "#1E3793", "dark": "#12245E"},  
        {"base": "#4CA8C4", "dark": "#2F6F7F"},  
        {"base": "#7B26B9", "dark": "#4E1775"},  
        {"base": "#F069EA", "dark": "#B84FAE"},  
        {"base": "#FF326B", "dark": "#CC2856"}   
    ]
    html_code = f"""
    <style>
    @keyframes ballAnimation {{
        0% {{ transform: scale(1); background-color: var(--base-color); }}
        50% {{ transform: scale(1.8); background-color: var(--dark-color); }}
        100% {{ transform: scale(1); background-color: var(--base-color); }}
    }}
    .ball {{
        width: 20px; height: 20px; border-radius: 50%;
        display: inline-block; margin: 0 10px;
        animation: ballAnimation 1.5s ease-in-out infinite;
        --base-color: {colors[0]['base']};
        --dark-color: {colors[0]['dark']};
    }}
    .ball:nth-child(1) {{ --base-color: {colors[0]['base']}; --dark-color: {colors[0]['dark']}; animation-delay: 0s; }}
    .ball:nth-child(2) {{ --base-color: {colors[1]['base']}; --dark-color: {colors[1]['dark']}; animation-delay: 0.3s; }}
    .ball:nth-child(3) {{ --base-color: {colors[2]['base']}; --dark-color: {colors[2]['dark']}; animation-delay: 0.6s; }}
    .ball:nth-child(4) {{ --base-color: {colors[3]['base']}; --dark-color: {colors[3]['dark']}; animation-delay: 0.9s; }}
    .ball:nth-child(5) {{ --base-color: {colors[4]['base']}; --dark-color: {colors[4]['dark']}; animation-delay: 1.2s; }}
    </style>

    <div style="display:inline-block; padding:12px 0 0 0;">
        <div class="ball"></div><div class="ball"></div><div class="ball"></div><div class="ball"></div><div class="ball"></div>
    </div>
    """
    display(HTML(html_code))
