define inactivity_timeout_seconds = 10

init python:
    persistent.inactivity_timer_remaining = None

    def reset_inactivity_timer():
        if _preferences.afm_enable:
            persistent.inactivity_timer_remaining = None
        else:
            persistent.inactivity_timer_remaining = inactivity_timeout_seconds

    def decrease_timer():
        if persistent.inactivity_timer_remaining is not None:
            persistent.inactivity_timer_remaining -= 1
            if persistent.inactivity_timer_remaining <= 0:
                persistent.inactivity_timer_remaining = None
                renpy.full_restart()
