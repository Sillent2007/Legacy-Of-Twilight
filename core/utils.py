import os
import sys
import time
from pathlib import Path

import pygame
from PIL import Image, ImageEnhance
from readchar import key, readkey
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich_pixels import Pixels

from core.music import EFFECT, audio


def line(symbol="=", color="purple"):
    line = symbol * WIDTH_TERMINAL
    console.print(line, style=colour["purple"])


def skip_line(quant_lines):
    for _ in range(quant_lines):
        print(" ")


def title(title, symbol=" ", color="reset"):
    title = colour[color] + title + colour["reset"]
    print(title.center(WIDTH_TERMINAL))
    line(symbol, color)
    print("")


def clear():
    return os.system("cls" if os.name == "nt" else "clear")


def write(text, delay=0.06):
    started = False

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if not started and char == " ":
            continue

        started = True

        if char.isspace():
            continue

        audio.play_sfx(EFFECT["dialogue"])

        if char in ",;":
            time.sleep(delay * 4)
        elif char in ".!?":
            time.sleep(delay * 8)
        else:
            time.sleep(delay)


WIDTH_TERMINAL = 180
HEIGHT_TERMINAL = 85


def center(text="text", color="normal"):
    console.print(text, justify="center", style=colour[color])
    return " "


console = Console()


colour = {
    "normal": "",
    "red": "#FF0000",
    "blue": "#0051FF",
    "green": "#0AE42E",
    "yellow": "#FFF700",
    "purple": "#810681",
    "gray": "#808080FF",
}


def image_to_pixels(img_path="url", width=WIDTH_TERMINAL, height=88):
    console = Console()
    clear_lines(999)
    try:
        pixels = Pixels.from_image_path(
            f"{Path(img_path).as_posix()}", resize=(width, height)
        )
    except Exception as error:
        raise FileNotFoundError("Diretório de imagem incorreto") from error
    console.print(pixels)


def logo_fade(
    image_path, resize=(WIDTH_TERMINAL, 100), fade_time=0.5, hold_time=0.5, fps=30
):
    console = Console()

    img = Image.open(image_path).convert("RGBA")

    total_frames = int(fade_time * fps)

    with Live(console=console, refresh_per_second=fps, screen=True) as live:
        # ---------- FADE IN ----------
        for frame in range(total_frames):
            brightness = (frame + 1) / total_frames

            enhancer = ImageEnhance.Brightness(img)
            current = enhancer.enhance(brightness)

            pixels = Pixels.from_image(current, resize=resize)

            live.update(Align.center(pixels, vertical="middle"))

            time.sleep(1 / fps)

        # ---------- SEGURA ----------
        time.sleep(hold_time)

        # ---------- FADE OUT ----------
        for frame in range(total_frames):
            brightness = 1 - ((frame + 1) / total_frames)

            enhancer = ImageEnhance.Brightness(img)
            current = enhancer.enhance(max(brightness, 0))

            pixels = Pixels.from_image(current, resize=resize)

            live.update(Align.center(pixels, vertical="middle"))

            time.sleep(1 / fps)


def hide_cursor():
    print("\033[?25l", end="", flush=True)
    clear()


def clear_lines(amount=1):
    for _ in range(amount):
        sys.stdout.write("\r")
        sys.stdout.write("\033[2K")
        sys.stdout.write("\033[F")

    sys.stdout.write("\r")
    sys.stdout.write("\033[2K")
    sys.stdout.flush()


def center_input():
    text = ""
    while True:
        # volta para o início da linha e limpa
        console.print(text, justify="center", style="bold #FFD700")

        k = readkey()

        if k == key.ENTER:
            print()
            return text

        elif k == key.BACKSPACE:
            text = text[:-1]

        elif len(k) == 1 and k.isprintable():
            text += k
        if text:
            clear_lines(1)


def cursor_up(amount=1):
    sys.stdout.write(f"\033[{amount}F")


def cursor_down(lines=1):
    sys.stdout.write(f"\033[{lines}B")
    sys.stdout.flush()


def cursor_right(cols=1):
    sys.stdout.write(f"\033[{cols}C")


def cursor_left(cols=1):
    sys.stdout.write(f"\033[{cols}D")


if __name__ == "__main__":
    pass
