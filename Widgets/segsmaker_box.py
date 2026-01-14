import ipywidgets as widgets
from IPython.display import display, HTML

# ─────────────────────────────────────
# Cargar diseño (CSS)
# ─────────────────────────────────────
def load_segsmaker_style():
    display(HTML("""
    <style>
    :root {
      --conda-bg: linear-gradient(
        270deg,
        #2197f2,
        #ab22fe,
        #ff2e88,
        #2197f2
      );
      background-size: 600% 600%;
    }

    .seg-box {
      width: 320px;
      border-radius: 26px;
      padding: 14px;
      background: rgba(38,38,38,0.9);
      animation: BorderPulse 12s infinite;
    }

    .seg-title {
      font-family: 'Roboto Mono', monospace;
      font-size: 16px;
      color: #e6e6e6;
      text-align: center;
      margin-bottom: 8px;
    }

    .seg-text {
      font-family: 'Roboto Mono', monospace;
      font-size: 13px;
      color: #cfcfcf;
      text-align: center;
      margin-bottom: 10px;
    }

    .seg-input input {
      font-family: 'Roboto Mono', monospace;
      font-size: 14px;
      height: 32px;
      width: 210px;
      color: #ffffff;
      text-align: center;
      border-radius: 8px;
      border: 3px solid #ab22fe;
      background: rgba(45,45,45,0.95);
    }

    .seg-input input::placeholder {
      color: #d0d0d0;
      opacity: 1;
    }

    .seg-button {
      font-size: 16px;
      width: 110px;
      height: 36px;
      color: #ffffff;
      border-radius: 8px;
      border: 3px solid #2197f2;
      background: rgba(0,0,0,0.5);
      cursor: pointer;
    }

    .seg-button:hover {
      transform: scale(1.15);
      background-image: var(--conda-bg);
      animation: slideBackground 7s linear infinite, BorderPulse 6s infinite;
    }

    @keyframes slideBackground {
      0% {background-position:0% 50%}
      50% {background-position:100% 50%}
      100% {background-position:0% 50%}
    }

    @keyframes BorderPulse {
      0% {box-shadow:0 0 6px #2197f2}
      50% {box-shadow:0 0 16px #ab22fe}
      100% {box-shadow:0 0 6px #2197f2}
    }
    </style>
    """))

# ─────────────────────────────────────
# Caja reutilizable (tipo gradient_box)
# ─────────────────────────────────────
def segsmaker_box(
    title: str | None = None,
    text: str | None = None,
    content: list | None = None,
    width: str = "320px"
):
    items = []

    if title:
        items.append(
            widgets.HTML(f"<div class='seg-title'>{title}</div>")
        )

    if text:
        items.append(
            widgets.HTML(f"<div class='seg-text'>{text}</div>")
        )

    if content:
        items.extend(content)

    box = widgets.Box(
        items,
        layout=widgets.Layout(
            width=width,
            display="flex",
            flex_flow="column",
            align_items="center",
            justify_content="space-around"
        )
    )

    box.add_class("seg-box")
    display(box)
