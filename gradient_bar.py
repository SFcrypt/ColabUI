# progress_bar_anim.py
from IPython.display import display, HTML

# Barra de progreso animada con gradiente
class display_ProgressBarAnimated:
    def __init__(self, total, text="Loading...", width=250, height=30, color1="#3498db", color2="#9b59b6", bg_color="#2c3e50", font_color="white"):
        self.total = total
        self.current = 0
        self.text = text
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.bg_color = bg_color
        self.font_color = font_color

        self.html_code = f"""
        <style>
        .progress-container {{
          display: flex;
          align-items: center;
          justify-content: flex-start;
          gap: 15px;
          width: 100%;
          padding: 10px;
        }}

        .progress-bar {{
          width: {self.width}px;
          height: {self.height}px;
          background-color: {self.bg_color};
          border-radius: 10px;
          overflow: hidden;
          position: relative;
        }}

        .progress-bar__fill {{
          width: 0%;
          height: 100%;
          background: linear-gradient(90deg, {self.color1}, {self.color2});
          background-size: 200% 100%;
          border-radius: 10px;
          transition: width 0.35s ease-out;
          animation: gradientAnimation 3s ease infinite;
        }}

        @keyframes gradientAnimation {{
          0% {{ background-position: 0% 50%; }}
          50% {{ background-position: 100% 50%; }}
          100% {{ background-position: 0% 50%; }}
        }}

        .progress-label {{
          font-family: 'Arial', sans-serif;
          font-size: 1.2rem;
          font-weight: bold;
          color: {self.font_color};
        }}
        </style>

        <div class="progress-container">
          <div class="progress-bar">
            <div id="progress-fill" class="progress-bar__fill"></div>
          </div>
          <div id="progress-label" class="progress-label">{self.text}</div>
        </div>

        <script>
        function updateProgress(percent, message) {{
          const progressFill = document.getElementById('progress-fill');
          const progressLabel = document.getElementById('progress-label');
          progressFill.style.width = percent + "%";
          progressLabel.textContent = message;
        }}
        </script>
        """

        display(HTML(self.html_code))

    def update(self, step=1):
        self.current += step
        if self.current > self.total:
            self.current = self.total
        percent = int((self.current / self.total) * 100)
        js_code = f'<script>updateProgress({percent}, "{self.text}");</script>'
        display(HTML(js_code))

    def complete(self, message="Done!"):
        self.current = self.total
        js_code = f'<script>updateProgress(100, "{message}");</script>'
        display(HTML(js_code))
