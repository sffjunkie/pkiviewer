import colorsys

import rich.color


def brighten(color: rich.color.Color | None):
    if color is None:
        return None

    red, green, blue = color.get_truecolor()
    hue, lightness, saturation = colorsys.rgb_to_hls(
        red / 255.0, green / 255.0, blue / 255.0
    )
    lightness += (1.0 - lightness) / 2.0
    new_r, new_g, new_b = colorsys.hls_to_rgb(hue, lightness, saturation)
    new_r = int(new_r * 255.0)
    new_g = int(new_g * 255.0)
    new_b = int(new_b * 255.0)
    return rich.color.Color.from_rgb(new_r, new_g, new_b)
