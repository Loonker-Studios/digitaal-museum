define center = Position(xpos=0.5, xanchor='center', ypos = 0.8, yanchor='center')
define left = Position(xpos=0, xanchor='left', ypos = 0.8, yanchor='center')
define right = Position(xpos=1.05, xanchor='right', ypos = 0.8, yanchor='center')

define center_right = Position(xpos=.65, xanchor='center', ypos = 0.8, yanchor='center')

# Move a sprite slightly up and down (like giving a slight node).
# This animation takes 0.4 seconds
transform nod_once:
    yoffset 0
    easein 0.2 yoffset 15
    easeout 0.2 yoffset 0

init:
    # make a sprite a silhouette
    transform silhouette:
        # use `at silhouette` to apply the transformation.
        # when using multiple transformations, do `at transform1, transform2, ...`
        matrixcolor TintMatrix("#000000ff")

    transform darken:
        # make a sprite darker (not speaking)
        matrixcolor TintMatrix("#00000080")

    transform spotlight:
        # spotlight a sprite (speaking)
        matrixcolor TintMatrix("#00000000")
