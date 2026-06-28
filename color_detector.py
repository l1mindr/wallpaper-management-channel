import colorsys
import colorgram

COLOR_FAMILY = {
    "Black": "Neutral",
    "White": "Neutral",
    "Gray": "Neutral",
    "Silver": "Neutral",
    "Brown": "Brown",
    "Beige": "Brown",
    "Gold": "Yellow",
    "Yellow": "Yellow",
    "Orange": "Orange",
    "Red": "Red",
    "Maroon": "Red",
    "Pink": "Red",
    "Purple": "Purple",
    "Violet": "Purple",
    "Blue": "Blue",
    "SkyBlue": "Blue",
    "Navy": "Blue",
    "Cyan": "Blue",
    "Green": "Green",
    "Lime": "Green",
    "Olive": "Green",
}


def rgb_to_hsv(r, g, b):
    h, s, v = colorsys.rgb_to_hsv(
        r / 255,
        g / 255,
        b / 255,
    )

    return (
        h * 360,
        s * 100,
        v * 100,
    )


def classify_color(r, g, b):
    h, s, v = rgb_to_hsv(r, g, b)

    # ------------------------
    # Neutral
    # ------------------------

    if v < 12:
        return "Black"

    if s < 10:
        if v > 94:
            return "White"

        if v > 75:
            return "Silver"

        return "Gray"

    # ------------------------
    # Brown / Beige
    # ------------------------

    if 15 <= h < 45:
        if v < 60:
            return "Brown"

        if s < 35:
            return "Beige"

    # ------------------------
    # Gold
    # ------------------------

    if 40 <= h < 58 and s > 45 and v > 60:
        return "Gold"

    # ------------------------
    # Red
    # ------------------------

    if h >= 345 or h < 10:
        if v < 45:
            return "Maroon"

        return "Red"

    # ------------------------
    # Orange
    # ------------------------

    if 10 <= h < 25:
        return "Orange"

    # ------------------------
    # Yellow
    # ------------------------

    if 25 <= h < 60:
        return "Yellow"

    # ------------------------
    # Olive
    # ------------------------

    if 60 <= h < 90:
        return "Olive"

    # ------------------------
    # Green
    # ------------------------

    if 90 <= h < 160:
        if v > 80:
            return "Lime"

        return "Green"

    # ------------------------
    # Cyan
    # ------------------------

    if 160 <= h < 190:
        return "Cyan"

    # ------------------------
    # Blue Family
    # ------------------------

    if 190 <= h < 255:
        if v < 35:
            return "Navy"

        if s < 40:
            return "Blue"

        if v > 80:
            return "SkyBlue"

        return "Blue"

    # ------------------------
    # Violet
    # ------------------------

    if 255 <= h < 290:
        return "Violet"

    # ------------------------
    # Pink / Purple
    # ------------------------

    if 290 <= h < 330:
        if s < 45:
            return "Purple"

        return "Pink"

    if 330 <= h < 345:
        if v < 45:
            return "Maroon"

        return "Pink"

    return "Colorful"


def get_color_tags(image_path: str, count: int = 8):
    colors = colorgram.extract(image_path, count)

    tags = []
    families = set()

    for color in colors:

        if color.proportion < 0.05:
            continue

        tag = classify_color(
            color.rgb.r,
            color.rgb.g,
            color.rgb.b,
        )

        if tag not in tags:
            tags.append(tag)

        family = COLOR_FAMILY[tag]

        if family != "Neutral":
            families.add(family)

    if len(families) >= 4:
        return ["Colorful"]

    return tags
