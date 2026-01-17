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
        color: rgba(255,255,255,0.85);  
        font-size: 20px;
        font-weight: 200;
        margin-bottom: 8px;  
    }

    .seg-input-html input {
        background: #555555;  
        border: none;
        border-radius: 12px;
        padding: 12px 0;
        width: 90%;           
        margin-bottom: 20px;  
        color: rgba(255,255,255,0.85);  
        font-size: 16px;
        text-align: center;
        transition: background 0.3s ease, transform 0.2s ease;
    }

    .seg-input-html input::placeholder {
        color: rgba(255,255,255,0.7);
    }

    .seg-input-html input:hover {
        background: #777777;  
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
    btn_color="#C41564",          
    btn_hover_color="#db5a94",    
    input_placeholder="Nombre del proyecto",
    input_width="99%",
    input_font_size=25,
    input_border_radius=5,
    input_margin_bottom=15
):
    """
    Crea un widget de input + botón y devuelve el botón para poder enlazar eventos.
    """

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
    button = widgets.Button(
        description=btn_text,
        layout=widgets.Layout(height=f"{btn_height}px", width="auto", padding=f"0 {btn_padding}px"),
        style={"button_color": btn_color, "font_size": f"{btn_font_size}px"}
    )
    button.add_class("seg-button")
    
    # Caja principal
    box = widgets.Box(
        [widgets.HTML(f"<div class='seg-title'>{title}</div>"),
         nombre_input_html,
         button],
        layout=widgets.Layout(
            width="100%",
            display="flex",
            flex_flow="column",
            align_items="center",
            justify_content="center"
        )
    )
    box.add_class("seg-box")
    display(box)

    # Retornar el botón y el input para enlazar eventos
    return button, nombre_input_html
