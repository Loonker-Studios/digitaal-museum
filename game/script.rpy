﻿
define valerie = Character(valerie_data.name)
define teresa = Character(teresa_data.name)
define aurora = Character(aurora_data.name)
define sasha = Character(sasha_data.name)
define esther = Character(esther_data.name)
define lena = Character(lena_data.name)
define natalie = Character(natalie_data.name)

define speler = Character("Bezoeker")
define medewerkster = Character("Medewerkster")
define intercom = Character("Intercom stem", what_style = "intercom_text")
define schrijver = Character("Schrijver", what_style = "schrijver_text")
define stanley = Character("Schrijver (Stanley)")
define verlosser = Character("De Verlosser", what_style = "verlosser_text")

label start:
    # Start timer
    show screen inactivity_timer

    # jump monogroom
    # jump glitch_art_animation
    # jump wouter_parable
    # jump japanse_tuin_galerij
    jump verlosser

    # jump test

    return