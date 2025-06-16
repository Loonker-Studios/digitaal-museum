## The background used for the main menu

### TODO setup all backgound effects
#### 1. If transforms need to be applied to an image, it needs to be done in a separate image (see verlosser_animated)
#### 2. Transitions are allowed (see example)
#### 3. make different loops for different builds


image verlosser_animated:
    "bg verlosser"
    AnimatedAberate

image wouter_parable_animated:
    "bg wouter parable wide" with dissolve
    2
    "bg wouter parable wide" with Dissolve(2)
    zoom_for_pan
    .5
    "bg wouter parable wide"
    pan_zoom
    6
    "bg black" with fade
    .5
    "bg wouter parable wide" with fade
    3

image wouter_parable_animated_vsh:
    "wouter_parable_animated"
    VHS

image bg tuin wide-shot zooming:
    "bg tuin wide-shot"
    2
    "bg tuin wide-shot"
    zoom_in
    2
    "bg tuin wide-shot"
    zoom_out
    2
    "bg tuin wide-shot"

## MAIN MENU images
image poc_main_menu:
    "bg black" with dissolve
    .5
    "bg glitch-art animation" with w19
    11
    "wouter_parable_animated_vsh"
    12
    "bg tuin wide-shot zooming" with w8
    15
    "verlosser_animated" with w3
    7
    "bg black" with dissolve
    .5
    repeat

image glitch_art_animation_menu:
    "bg black" with fade
    .5
    "bg tuin wide-shot zooming" with dots
    15
    "bg poc glitch-art" with w14
    5
    "verlosser_animated" with snake
    5
    "wouter_parable_animated_vsh" with sunshine
    12
    repeat

image wouter_parable_menu:
    "bg black" with fade
    .5
    "bg wouter parable door" with maze
    4
    "bg poc glitch-art" with w14
    5
    "verlosser_animated" with snake
    5
    "bg glitch-art animation" with w17
    10
    repeat

image japanse_tuin_menu:
    "bg black"
    .5
    "verlosser_animated" with curtains
    5
    "wouter_parable_animated_vsh" with bowtie
    12
    "bg glitch-art animation" with edges
    10
    "bg poc rgb" with letter
    5
    "bg wouter parable door" with maze
    6
    "bg black" with radio
    2
    repeat

image verlosser_menu:
    "bg black"
    .5
    "wouter_parable_animated_vsh" with curtains
    12
    "bg glitch-art animation" with edges
    10
    "bg poc rgb" with letter
    5
    "bg tuin wide-shot zooming" with dots
    15
    "bg poc glitch-art" with wet
    5
    "bg black" with radio
    2
    repeat

image bg main_menu = ConditionSwitch(
    "room == \"wouter_parable\"", "wouter_parable_menu",
    "room == \"POC\"", "poc_main_menu",
    "room == \"glitch-art-animation\"", "glitch_art_animation_menu",
    "room == \"japanse_tuin\"", "japanse_tuin_menu",
    "room == \"verlosser\"", "verlosser_menu"
)