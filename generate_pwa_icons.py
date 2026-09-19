"""
generate_pwa_icons.py
Generates all PWA icons from a source logo.
Place logo at: static/assets/logo.png
Run: python generate_pwa_icons.py
"""

import os
from pathlib import Path
from PIL import Image


# ============================================================
# CONFIG
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
SOURCE_LOGO = BASE_DIR / "static" / "assets" / "logo.png"
OUTPUT_DIR = BASE_DIR / "static" / "assets" / "pwa"

MASKABLE_BG = "#0f172a"
ICON_SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
SCREENSHOT_DESKTOP = (1280, 720)
SCREENSHOT_MOBILE = (750, 1334)
SHORTCUT_SIZE = 96


# ============================================================
# HELPERS
# ============================================================

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def load_source_logo():
    if not SOURCE_LOGO.exists():
        raise FileNotFoundError(
            f"Source logo not found at: {SOURCE_LOGO}\n"
            f"Place a square PNG (512x512+) there and re-run."
        )
    return Image.open(SOURCE_LOGO).convert("RGBA")


def make_icon(logo, size, bg_color=None, padding_ratio=0.0):
    if bg_color is not None:
        canvas = Image.new("RGBA", (size, size), bg_color)
    else:
        canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    if padding_ratio > 0:
        inner_size = int(size * (1 - 2 * padding_ratio))
    else:
        inner_size = size

    resized = logo.copy()
    resized.thumbnail((inner_size, inner_size), Image.LANCZOS)

    x = (size - resized.width) // 2
    y = (size - resized.height) // 2
    canvas.paste(resized, (x, y), resized)
    return canvas


def save(img, name):
    path = OUTPUT_DIR / name
    img.save(path, "PNG", optimize=True)
    print(f"  OK  {name}  ({img.width}x{img.height}, {path.stat().st_size} bytes)")


# ============================================================
# GENERATORS
# ============================================================

def generate_standard_icons(logo):
    print("\n[1] Standard icons")
    for size in ICON_SIZES:
        save(make_icon(logo, size), f"icon-{size}.png")


def generate_maskable_icons(logo):
    print("\n[2] Maskable icons")
    bg = hex_to_rgb(MASKABLE_BG) + (255,)
    for size in ICON_SIZES:
        save(make_icon(logo, size, bg_color=bg, padding_ratio=0.20),
             f"icon-{size}-maskable.png")


def generate_favicons(logo):
    print("\n[3] Favicons")
    for size in [16, 32, 48]:
        save(make_icon(logo, size), f"favicon-{size}.png")


def generate_apple_touch_icon(logo):
    print("\n[4] Apple touch icon")
    bg = hex_to_rgb(MASKABLE_BG) + (255,)
    save(make_icon(logo, 180, bg_color=bg, padding_ratio=0.10),
         "apple-touch-icon.png")


def generate_shortcuts(logo):
    print("\n[5] Shortcut icons")
    for name in ["shortcut-about", "shortcut-catalogue", "shortcut-contact"]:
        save(make_icon(logo, SHORTCUT_SIZE), f"{name}.png")


def generate_screenshots(logo):
    print("\n[6] Screenshots")
    bg = hex_to_rgb(MASKABLE_BG) + (255,)
    for name, (w, h) in [
        ("screenshot-desktop.png", SCREENSHOT_DESKTOP),
        ("screenshot-mobile.png", SCREENSHOT_MOBILE),
    ]:
        canvas = Image.new("RGBA", (w, h), bg)
        logo_size = int(min(w, h) * 0.4)
        resized = logo.copy()
        resized.thumbnail((logo_size, logo_size), Image.LANCZOS)
        x = (w - resized.width) // 2
        y = (h - resized.height) // 2
        canvas.paste(resized, (x, y), resized)
        save(canvas, name)


# ============================================================
# MAIN
# ============================================================

def main():
    print(f"Source logo: {SOURCE_LOGO}")
    print(f"Output dir : {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    logo = load_source_logo()
    print(f"Loaded logo: {logo.width}x{logo.height}")

    generate_standard_icons(logo)
    generate_maskable_icons(logo)
    generate_favicons(logo)
    generate_apple_touch_icon(logo)
    generate_shortcuts(logo)
    generate_screenshots(logo)

    print(f"\nAll icons generated in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
