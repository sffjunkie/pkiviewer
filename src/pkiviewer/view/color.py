import colorsys
import rich.color


def brighten(color: rich.color.Color | None):
    if color is None:
        return None

    r, g, b = color.get_truecolor()
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    l += (1.0 - l) / 2.0
    new_r, new_g, new_b = colorsys.hls_to_rgb(h, l, s)
    new_r = int(new_r * 255.0)
    new_g = int(new_g * 255.0)
    new_b = int(new_b * 255.0)
    return rich.color.Color.from_rgb(new_r, new_g, new_b)
