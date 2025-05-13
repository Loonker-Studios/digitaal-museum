define config.gl2 = True  # Enables OpenGL for smoother transitions (optional)

transform zoom_in:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 1.0
    linear 5.0 zoom 2.0

transform zoom_out:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 2.0
    linear 5.0 zoom 1.0

transform zoom_for_pan:
    zoom 1.2
    yalign 0.5
    xalign 0.0

transform pan_zoom:
    xalign 0.0  # Anchor to the left side of the screen
    yalign 0.5
    zoom 1.2    # Zoom in slightly (adjust as needed)
    linear 5.0 xoffset -192  # Move image left by the correct amount

transform pan_up:
    xalign 0.4  # Anchor to the left side of the screen
    yalign 1.0
    zoom 1.2    # Zoom in slightly (adjust as needed)
    linear 5.0 yoffset 210  # Move image left by the correct amount