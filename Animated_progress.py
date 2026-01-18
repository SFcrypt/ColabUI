# Barra de progreso personalizada
from IPython.display import display, HTML

# Configuración de la barra
class Animated_progress:
    def __init__(
        self,
        total,
        title="Título",
        button_text="",
        background_color="#1E1F21",
        button_colors=("#ed1570", "#f760a8", "#ed1570"),
        title_color="rgba(255,255,255,0.9)",
        padding_height="10px 0",
        min_height="120px"
    ):
        self.total = total
        self.current = 0
        self.button_text = button_text
        self.title = title
        c1, c2, c3 = button_colors

        html = f"""
        <style>
        @keyframes pinkMove {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        .status-box {{
            background:{background_color};
            width:100%;
            min-height:{min_height};
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            padding:{padding_height};
            border-radius:12px;
            font-family:'Source Sans Pro', sans-serif;
        }}

        .status-title {{
            color:{title_color};
            font-size:25px;
            font-weight:500;
            margin-bottom:12px;
            text-align:center;
        }}

        .progress-btn {{
            width:260px;
            height:36px;
            background:#2a2a2a;
            border-radius:16px;
            overflow:hidden;
            box-shadow:0 4px 12px rgba(0,0,0,0.35);
        }}

        .progress-fill {{
            width:0%;
            height:100%;
            background:linear-gradient(270deg,{c1},{c2},{c3});
            background-size:200% 200%;
            animation:pinkMove 4s ease infinite;
            display:flex;
            align-items:center;
            justify-content:center;
            color:#ffffff;
            font-size:25px;
            transition:width 0.35s ease-out;
            white-space:nowrap;
        }}
        </style>

        <div class="status-box">
            <div id="status-title" class="status-title">{title}</div>
            <div class="progress-btn">
                <div id="btn-fill" class="progress-fill">{button_text}</div>
            </div>
        </div>

        <script>
        function updateButtonProgress(percent, text) {{
            const fill = document.getElementById("btn-fill");
            fill.style.width = percent + "%";
            fill.textContent = text;
        }}

        function updateTitle(text) {{
            const title = document.getElementById("status-title");
            title.textContent = text;
        }}
        </script>
        """

        display(HTML(html))

    def update(self, step=1, text=None):
        self.current += step
        if self.current > self.total:
            self.current = self.total

        percent = int((self.current / self.total) * 100)
        label = text if text else self.button_text
        display(HTML(f'<script>updateButtonProgress({percent}, "{label}");</script>'))

    def complete(self, message="Completado"):
        self.current = self.total
        display(HTML(f'''
        <script>
            updateButtonProgress(100, "{self.button_text}");
            updateTitle("{message}");
        </script>
        '''))
