define config.gl2 = True  # Enables OpenGL for smoother transitions (optional)

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