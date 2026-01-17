# Diseño de caja negro gris y rosa
# ================================

# Download_box.py
import ipywidgets as widgets
from IPython.display import clear_output, display, HTML

# Estilos de caja
def load_style():
    css = """
    .seg-box {
        background: #232323;
        border-radius: 12px;
        padding: 20px;
        width: 360px;
        font-family: 'Source Sans Pro', sans-serif;
        text-align: center;}

    .seg-title {
        color: rgba(255,255,255,0.25);
        font-size: 20px;
        font-weight: 200;
        margin-bottom: 16px;}

    /* INPUT */
    .seg-input input {
        background: transparent;
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 6px;
        padding: 10px;
        width: 100%;
        color: white;
        text-align: center;
        font-size: 14px;}

    .seg-input input::placeholder {
        color: rgba(255,255,255,0.35);
        text-align: center;}

    /* BOTÓN CREAR tipo Download, rosa con borde más redondo */
    .seg-button {
        width: auto;
        display: inline-block;
        margin-top: 5px;}

    .seg-button button {
        background: #C41564; /* rosa */
        color: #ffffff;
        border: none;
        border-radius: 16px; /* más redondo */
        height: 34px;        
        padding: 0 36px;     /* ancho aumentado */
        font-size: 13px;     
        font-weight: 600;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: background 0.3s ease;
    }

    .seg-button button:hover {
        background: #e03b81;   /* rosa más claro al pasar */
    }
    """
    display(HTML(f"<style>{css}</style>"))

# ===============
# diseño Widget 
def pink_download(title="SegsMaker"):
    load_style()

    # Input
    nombre_input = widgets.Text(
        placeholder="Nombre del proyecto",
        layout=widgets.Layout(width="100%", margin="0 0 15px 0"))
    nombre_input.add_class("seg-input")

    # Botón Crear
    crear_btn = widgets.Button(description="Crear")
    crear_btn.add_class("seg-button")
    crear_btn.layout.width = "160px"
    crear_btn.layout.height = "34px"
    crear_btn.style.button_color = "#C41564"
    crear_btn.style.font_weight = "bold"
    crear_btn.style.font_size = "13px"

    # Caja final
    box = widgets.Box(
        [widgets.HTML(f"<div class='seg-title'>{title}</div>"),
         nombre_input,
         crear_btn],
        layout=widgets.Layout(
            width="360px",
            display="flex",
            flex_flow="column",
            align_items="center",
            justify_content="space-around")
    )
    box.add_class("seg-box")
    display(box)
