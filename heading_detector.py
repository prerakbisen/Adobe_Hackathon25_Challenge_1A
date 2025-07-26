def classify_heading(font_size):
    if font_size >= 16:
        return "H1"
    elif font_size >= 13:
        return "H2"
    elif font_size >= 11:
        return "H3"
    else:
        return None
