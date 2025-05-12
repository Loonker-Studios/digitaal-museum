## The background used for the main menu

### TODO setup all backgound effects
#### 1. If transforms need to be applied to an image, it needs to be done in a separate image (see verlosser_animated)
#### 2. Transitions are allowed (see example)


image verlosser_animated:
    "bg verlosser"
    AnimatedAberate

image bg main_menu:
    # todo setup all backgrounds, effects and animations
    "bg black" with fade
    1
    "bg poc glitch-art" with w14
    5
    "verlosser_animated" with snake
    5
    "bg glitch-art animation" with w17
    10
    repeat

