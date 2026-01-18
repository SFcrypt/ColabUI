from IPython.display import display, HTML

def animated_status(
    title="Proyecto",
    button_text="Listo",
    background_color="#232323",
    button_colors=("#ed1570", "#f760a8", "#ed1570"),
    title_color="rgba(255,255,255,0.9)",
    min_height="120px"
):
    """
    Caja visual de estado con botón rosa animado (solo decorativo)
    """

    c1, c2, c3 = button_colors

    display(HTML(f"""
    <style>
    @keyframes pinkMove {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    </style>

    <div style="
        background:{background_color};
        width:100%;
        min-height:{min_height};
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        font-family:'Source Sans Pro', sans-serif;
        padding:10px 0;
        border-radius:12px;
    ">
        <!-- Título -->
        <div style="
            color:{title_color};
            font-size:25px;
            font-weight:500;
            margin-bottom:12px;
            text-align:center;
        ">
            {title}
        </div>

        <!-- Botón decorativo -->
        <button style="
            border:none;
            border-radius:16px;
            background:linear-gradient(270deg,{c1},{c2},{c3});
            background-size:200% 200%;
            animation:pinkMove 4s ease infinite;
            color:#ffffff;
            font-size:25px;
            padding:10px 80px;
            cursor:default;
            pointer-events:none;
            box-shadow:0 4px 12px rgba(0,0,0,0.35);
        ">
            {button_text}
        </button>
    </div>
    """))
