# gradient_box.py 

# gradient_boxes/outside_box.py
from IPython.display import display, HTML

def display_outside_box(message, color1="#3498db", color2="#9b59b6", left="7px", right="7px", size="12px", text="white", fund="#292929", Wide="auto"):
    animation_id = hash(message)
    
    html_code = f"""
    <style>
    @keyframes borderGradientAnimation_{animation_id} {{
        0% {{
            border-image-source: linear-gradient(90deg, {color1}, {color2});
        }}
        50% {{
            border-image-source: linear-gradient(90deg, {color2}, {color1});
        }}
        100% {{
            border-image-source: linear-gradient(90deg, {color1}, {color2});
        }}
    }}
    </style>
    <div style="
        display: inline-block;
        padding: 8px 12px;
        background-color: {fund};
        color: {text};
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: {size};
        text-align: center;
        border-left: {left} solid transparent;
        border-right: {right} solid transparent;
        margin: 3px 0;
        border-image: linear-gradient(90deg, {color1}, {color2}) 1;
        animation: borderGradientAnimation_{animation_id} 3s ease infinite;
        width: {Wide};
    ">
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))

# gradient_boxes/inside_box.py
from IPython.display import display, HTML

def display_inside_box(message, color1="#3498db", color2="#9b59b6", left="7px", right="7px", size="12px", text="white", fund="#292929", Wide="auto"):
    animation_id = hash(message)
    
    html_code = f"""
    <style>
    @keyframes gradientAnimation_{animation_id} {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
        }}
    }}
    </style>
    <div style="
        display: inline-block;
        padding: 8px 12px;
        color: {text};
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: {size};
        text-align: center;
        border-left: {left} solid {fund};
        border-right: {right} solid {fund};
        margin: 3px 0;
        background: linear-gradient(90deg, {color1}, {color2});
        background-size: 200% 100%;
        animation: gradientAnimation_{animation_id} 3s ease infinite;
        width: {Wide};
    ">
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))

# gradient_boxes/circular_box.py
from IPython.display import display, HTML

def display_circular_box(message, color1="#3498db", color2="#9b59b6", left="4px", right="4px", top="4px", bottom="4px", size="12px", text="white", fund="#292929", Wide="auto", animation_duration="3s"):
    animation_id = hash(message)
    
    html_code = f"""
    <style>
    @keyframes circularBorderAnimation_{animation_id} {{
        0% {{
            border-color: {color1};
        }}
        50% {{
            border-color: {color2};
        }}
        100% {{
            border-color: {color1};
        }}
    }}
    </style>
    <div style="
        display: inline-block;
        padding: 8px 12px;
        background-color: {fund};
        color: {text};
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: {size};
        text-align: center;
        border-radius: 50px;
        border-left: {left} solid {color1};
        border-right: {right} solid {color1};
        border-top: {top} solid {color1};
        border-bottom: {bottom} solid {color1};
        margin: 3px 0;
        animation: circularBorderAnimation_{animation_id} {animation_duration} ease infinite;
        width: {Wide};
    ">
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    """
    display(HTML(html_code))


# gradient_boxes/interactive_box.py
from IPython.display import display, HTML

def display_interactive_box(message, color1="#3498db", color2="#9b59b6", left="7px", right="7px", size="12px", text="white", fund="#292929", Wide="auto"):
    animation_id = hash(message)
    
    html_code = f"""
    <style>
    @keyframes borderGradientAnimation_{animation_id} {{
        0% {{
            border-image-source: linear-gradient(90deg, {color1}, {color2});
        }}
        50% {{
            border-image-source: linear-gradient(90deg, {color2}, {color1});
        }}
        100% {{
            border-image-source: linear-gradient(90deg, {color1}, {color2});
        }}
    }}
    @keyframes gradientAnimation_{animation_id} {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
        }}
    }}
    </style>
    <div id="box_{animation_id}" style="
        display: inline-block;
        padding: 8px 12px;
        background-color: {fund};
        color: {text};
        font-family: Arial, sans-serif;
        font-weight: bold;
        font-size: {size};
        text-align: center;
        border-left: {left} solid transparent;
        border-right: {right} solid transparent;
        margin: 3px 0;
        border-image: linear-gradient(90deg, {color1}, {color2}) 1;
        animation: borderGradientAnimation_{animation_id} 3s ease infinite;
        width: {Wide};
        cursor: pointer;
    " onmouseover="activateGradient('box_{animation_id}', '{color1}', '{color2}', '{fund}')"
      onmouseout="deactivateGradient('box_{animation_id}', '{color1}', '{color2}', '{fund}')">
        <span style="letter-spacing: 2px;">{message}</span>
    </div>
    <script>
    function activateGradient(boxId, color1, color2, fund) {{
        var box = document.getElementById(boxId);
        box.style.borderImage = "none";
        box.style.borderLeft = "7px solid {fund}";
        box.style.borderRight = "7px solid {fund}";
        box.style.animation = "none";
        box.style.background = `linear-gradient(90deg, ${{color1}}, ${{color2}})`;
        box.style.backgroundSize = '200% 100%';
        box.style.animation = `gradientAnimation_${{boxId.split('_')[1]}} 3s ease infinite`;
    }}

    function deactivateGradient(boxId, color1, color2, fund) {{
        var box = document.getElementById(boxId);
        box.style.borderImage = `linear-gradient(90deg, ${{color1}}, ${{color2}}) 1`;
        box.style.borderLeft = "{left} solid transparent";
        box.style.borderRight = "{right} solid transparent";
        box.style.animation = `borderGradientAnimation_${{boxId.split('_')[1]}} 3s ease infinite`;
        box.style.background = "{fund}";
        box.style.animation = "none";
    }}
    </script>
    """
    display(HTML(html_code))
