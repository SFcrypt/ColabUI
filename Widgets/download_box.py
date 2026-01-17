#@title Pink Button Download Widget
import ipywidgets as widgets
from IPython.display import display, HTML

# ==============================
# Estilos CSS
def load_style():
    css = """
    .seg-box {
        background: #232323;
        border-radius: 12px;
        padding: 20px;
        width: 360px;
        font-family: 'Source Sans Pro', sans-serif;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .seg-title {
        color: rgba(255,255,255,0.85);  /* Gris-blanco */
        font-size: 20px;
        font-weight: 200;
        margin-bottom: 8px;  /* Subido un poco */
    }

    .seg-input-html input {
        background: #555555;  /* Gris en lugar de rosa */
        border: none;
        border-radius: 12px;
        padding: 12px 0;
        width: 90%;           
        margin-bottom: 20px;  
        color: rgba(255,255,255,0.85);  /* Letras gris-blanco */
        font-size: 16px;
        text-align: center;
        transition: background 0.3s ease, transform 0.2s ease;
    }

    .seg-input-html input::placeholder {
        color: rgba(255,255,255,0.7);
    }

    .seg-input-html input:hover {
        background: #777777;  /* Gris más claro al pasar el mouse */
        transform: translateY(-1px);
    }

    .seg-button-html button {
        color: #fff;
        border: none;
        cursor: pointer;
        transition: background 0.3s ease, transform 0.2s ease;
    }

    .seg-button-html button:hover {
        transform: translateY(-1px);
    }
    """
    display(HTML(f"<style>{css}</style>"))

# ==============================
# Función del widget
def pink_button_download(
    title="Mitsuri Kanroji",
    btn_text="Crear",
    btn_height=35,
    btn_padding=50,
    btn_font_size=15,
    btn_border_radius=12,
    btn_color="#C41564",          # Botón rosa
    btn_hover_color="#db5a94",    # Rosa más claro al pasar el mouse
    input_placeholder="Nombre del proyecto",
    input_width="99%",
    input_font_size=25,
    input_border_radius=5,
    input_margin_bottom=15
):
    # Cargar estilos
    load_style()

    # Input
    nombre_input_html = widgets.HTML(
        f"""
        <div class='seg-input-html'>
            <input type='text' placeholder='{input_placeholder}'
                   style='width:{input_width}; font-size:{input_font_size}px; border-radius:{input_border_radius}px; margin-bottom:{input_margin_bottom}px;'>
        </div>
        """)

    # Botón
    button_style = f"""
    height: {btn_height}px;
    padding: 0 {btn_padding}px;
    font-size: {btn_font_size}px;
    border-radius: {btn_border_radius}px;
    background: {btn_color};
    """
    crear_btn_html = widgets.HTML(
        f"""
        <div class='seg-button-html'>
            <button style='{button_style}'
                    onmouseover="this.style.background='{btn_hover_color}'"
                    onmouseout="this.style.background='{btn_color}'">
                {btn_text}
            </button>
        </div>
        """)

    # Caja principal
    box = widgets.Box(
        [widgets.HTML(f"<div class='seg-title'>{title}</div>"),
         nombre_input_html,
         crear_btn_html],
        layout=widgets.Layout(
            width="100%",
            display="flex",
            flex_flow="column",
            align_items="center",
            justify_content="center"))
    box.add_class("seg-box")
    display(box)

# ==============================
# Fin del módulo
