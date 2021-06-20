button = document.getElementById("change-color-btn")
div = document.getElementById("square-div")
colors = ["red", "blue", "yellow", "orange", "green", "magenta"]


def error(message: str):
    alert(f"[ERROR]: {message}")
    raise Exception(f"[ERROR]: {message}")


def handle_change_color_button_click(e: any) -> None or any:
    color = prompt("Write color")
    if not color in colors:
        return error(f'Invalid color, available colors: {", ".join(colors)}')
    div.style.background = color


button.onclick = handle_change_color_button_click
