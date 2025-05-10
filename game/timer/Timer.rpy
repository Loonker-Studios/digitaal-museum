
init python:
    # Set the timeout duration in seconds
    INACTIVITY_TIMEOUT = 60
    # This variable will track remaining time
    inactivity_remaining_time = INACTIVITY_TIMEOUT

# Function to reset the timer
init python:
    def reset_inactivity_timer():
        global inactivity_remaining_time
        inactivity_remaining_time = INACTIVITY_TIMEOUT

# Screen that handles the inactivity timer
screen inactivity_timer():

    # Timer that counts down every second
    timer 1 repeat True action If(
        inactivity_remaining_time > 0,
        true=Function(lambda: setattr(store, 'inactivity_remaining_time', inactivity_remaining_time - 1)),
        false=ReturnToMainMenu()
    )

    # Catch any key press to reset timer
    key "mouseup_1" action [Function(reset_inactivity_timer), Return()]
    key "mouseup_2" action [Function(reset_inactivity_timer), Return()]
    key "K_RETURN" action [Function(reset_inactivity_timer), Return()]
    key "K_SPACE" action [Function(reset_inactivity_timer), Return()]

    # Debug display of timer — top-right corner, with styling
    frame:
        background "#0008"  # semi-transparent black
        padding (10, 5)
        align (0.98, 0.02)  # Top-right corner
        text "[inactivity_remaining_time]s to inactivity reset" size 20 color "#FFF" bold True


# Helper action to return to main menu cleanly
init python:
    class ReturnToMainMenu(Action):
        def __call__(self):
            renpy.full_restart()
