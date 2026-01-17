# Download_box.py
import ipywidgets as widgets
from IPython.display import display, HTML
import threading
import time

# ================= ESTILOS =================
def load_styles():
    css = """
    .seg-box {
        background: #232323;
        border-radius: 12px;
        padding: 20px;
        width: 360px;
        font-family: 'Source Sans Pro', sans-serif;
        text-align: center;
    }

    .seg-title {
        color: rgba(255,255,255,0.25);
        font-size: 20px;
        font-weight: 200;
        margin-bottom: 16px;
    }

    .seg-input input {
        background: transparent;
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 6px;
        padding: 10px;
        width: 100%;
        color: white;
        text-align: center;
        font-size: 14px;
    }

    .seg-input input::placeholder {
        color: rgba(255,255,255,0.35);
        text-align: center;
    }

    .seg-button {
        width: auto;
        display: inline-block;
        margin-top: 5px;
    }

    .seg-button button {
        background: #C41564;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        height: 34px;        
        padding: 0 36px;
        font-size: 13px;     
        font-weight: 600;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: background 0.3s ease;
    }

    .seg-button button:hover {
        background: #e03b81;
    }

    .seg-progress {
        position: absolute;
        top: 0;
        bottom: 0;
        right: 100%;
        width: 100%;
        background-image: linear-gradient(
            -45deg,
            rgba(0,0,0,0.15) 10%,
            rgba(0,0,0,0.25) 10%,
            rgba(0,0,0,0.25) 20%,
            rgba(0,0,0,0.15) 20%,
            rgba(0,0,0,0.15) 30%,
            rgba(0,0,0,0.25) 30%,
            rgba(0,0,0,0.25) 40%
        );
        transition: 4s linear;
    }

    .seg-button.loading button {
        background: #e03b81;
        color: rgba(255,255,255,0.9);
    }

    .seg-button.done button {
        background: #C41564;
        color: #ffffff;
    }
    """
    display(HTML(f"<style>{css}</style>"))

# ================= WIDGET =================
def segsmaker_download_box(title="SegsMaker"):
    _load_styles()

    # Input
    nombre_input = widgets.Text(
        placeholder="Nombre del proyecto",
        layout=widgets.Layout(width="100%", margin="0 0 15px 0")
    )
    nombre_input.add_class("seg-input")

    # Botón + progreso
    crear_btn = widgets.Button(description="Crear")
    crear_btn.add_class("seg-button")
    progress_html = widgets.HTML("<div class='seg-progress' id='prog'></div>")
    btn_box = widgets.Box([crear_btn, progress_html])
    btn_box.add_class("seg-button")

    # Lógica botón
    def start_download(b):
        crear_btn.description = ""
        btn_box.add_class("loading")

        def finish():
            time.sleep(4.2)
            crear_btn.description = "Done!"
            btn_box.remove_class("loading")
            btn_box.add_class("done")

        threading.Thread(target=finish).start()

    crear_btn.on_click(start_download)

    # Caja final
    box = widgets.Box(
        [widgets.HTML(f"<div class='seg-title'>{title}</div>"),
         nombre_input,
         btn_box],
        layout=widgets.Layout(
            width="360px",
            display="flex",
            flex_flow="column",
            align_items="center",
            justify_content="space-around"
        )
    )
    box.add_class("seg-box")
    display(box)
