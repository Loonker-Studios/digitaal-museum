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

define rooms = [
    {
        "id": "POC",
        "message": "Zaal: Burned_Music",
        "visited": False,
        "label": "monogroom"
    },
    {
        "id": "glitch-art-animation",
        "message": "Zaal: Glitch Art",
        "visited": False,
        "label": "glitch_art_animation"
    },
    {
        "id": "wouter_parable",
        "message": "Zaal: The Wouter Parable",
        "visited": False,
        "label": "wouter_parable"
    },
    {
        "id": "japanse_tuin",
        "message": "Zaal: Japan",
        "visited": False,
        "label": "japanse_tuin_galerij"
    },
    {
        "id": "verlosser",
        "message": "Zaal: De Verlosser",
        "visited": False,
        "label": "verlosser"
    }
]

define visited_rooms = []

label start:
    jump intro