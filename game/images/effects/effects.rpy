# Overlay effects
#############################
define static_alpha = 0.75
define static_sparkle = 0.85

image static:
    im.Alpha("images/effects/noise/noise1.png", static_alpha) with Dissolve(0.2)
    0.2
    im.Alpha("images/effects/noise/noise2.png", static_alpha) with Dissolve(0.2)
    0.2
    im.Alpha("images/effects/noise/noise3.png", static_alpha) with Dissolve(0.2)
    0.2
    im.Alpha("images/effects/noise/noise4.png", static_alpha) with Dissolve(0.2)
    0.2
    repeat

image sparkle:
    im.Alpha("images/effects/sparkle/sparkle1.png", static_sparkle) with Dissolve(0.6)
    0.6
    im.Alpha("images/effects/sparkle/sparkle3.png", static_sparkle) with Dissolve(0.6)
    0.6
    im.Alpha("images/effects/sparkle/sparkle2.png", static_sparkle) with Dissolve(0.6)
    0.6
    im.Alpha("images/effects/sparkle/sparkle1.png", static_sparkle) with Dissolve(0.6)
    0.6
    im.Alpha("images/effects/sparkle/sparkle2.png", static_sparkle) with Dissolve(0.6)
    0.6
    im.Alpha("images/effects/sparkle/sparkle3.png", static_sparkle) with Dissolve(0.6)
    0.6
    repeat

# image tiledFog = Tile(im.Scale("images/effects/fog/fog.png", 1600, 600), size=(2400, 800))
image particleFog1 = SnowBlossom("images/effects/fog/fog-particle.png", 
    count=40, 
    border=600,
    xspeed=50, 
    yspeed=0, 
    start=0, 
    fast=True,
    horizontal=True
)
image particleFog2 = SnowBlossom("images/effects/fog/fog-particle.png", count=40, border=600, xspeed=-55, yspeed=0, start=5, fast=True, horizontal=True)

image foggy:
    Composite(
        (config.screen_width, config.screen_height),
        (0,0), SnowBlossom("images/effects/fog/fog-particle.png", 
            count=40, 
            border=600,
            xspeed=50, 
            yspeed=0, 
            start=0, 
            fast=True,
            horizontal=True
        ),
        (0,0), SnowBlossom(
            "images/effects/fog/fog-particle.png", 
            count=40, 
            border=600, 
            xspeed=-55, 
            yspeed=0, 
            start=5, 
            fast=True, 
            horizontal=True
        ),
    )

#############################

image top_black_bar = Solid("#000000")
image bottom_black_bar = Solid("#000000")

screen black_bars():
    ## cinemascope 21:9 == 129 px
    $ bar_height = round((config.screen_height - (config.screen_width * 9 / 21)) / 2) 

    add "top_black_bar" xpos 0 ypos 0 xsize config.screen_width ysize bar_height
    add "bottom_black_bar" xpos 0 ypos (config.screen_height- bar_height) xsize config.screen_width ysize bar_height
