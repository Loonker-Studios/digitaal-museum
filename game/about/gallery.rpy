define gallery_entries = [
    {
        "image": "images/background/bg poc glitch-art close-up.png",
        "title": "Glitch-Art 1-6",
        "artist": "Sam Van Lier (Instagram: @burned_music)",
        "id": "POC"
    },
    {
        "image": "images/background/bg poc rgb close-up.png",
        "title": "Monogroom",
        "artist": "Sam Van Lier (Instagram: @burned_music)",
        "id": "POC"
    },
    {
        "image": "bg glitch-art animation",
        "title": "Glitch-Art Animation",
        "artist": "Marc Van Dercruyssen",
        "id": "glitch-art-animation"
    },
    {
        "image": "bg wouter parable cotton",
        "title": "Cotton",
        "artist": "Wouter Derkinderen",
        "id": "wouter_parable"
    },
    {
        "image": "bg wouter parable mask",
        "title": "The Mask (Het Masker)",
        "artist": "Wouter Derkinderen",
        "id": "wouter_parable"
    },
    {
        "image": "bg wouter parable metallic",
        "title": "Metallic",
        "artist": "Wouter Derkinderen",
        "id": "wouter_parable"
    },
    {
        "image": "bg tuin gallerij wide-shot",
        "title": "Japanse tuin compilatie",
        "artist": "Cecile Van der Paal (Instagram @cecilevanderpaal)",
        "id": "japanse_tuin"
    },
    {
        "image": "bg tuin poster1",
        "title": "Durf groots te dromen",
        "artist": "Cecile Van der Paal (Instagram @cecilevanderpaal)",
        "id": "japanse_tuin"
    },
    {
        "image": "bg tuin poster2",
        "title": "Mischien moeten we aan een andere locatie beginnen denken",
        "artist": "Cecile Van der Paal (Instagram @cecilevanderpaal)",
        "id": "japanse_tuin"
    },
    {
        "image": "bg verlosser",
        "title": "Verlosser",
        "artist": "Tamar V.D.",
        "id": "verlosser"
    }
]

screen gallery():

    tag menu

    use game_menu(_("De artist"), scroll="viewport"):
        
        style_prefix "about"
        
        vbox:
            spacing 30
            align (0.5, 0.0)
            
            label "Gallerij overzicht"

            for entry in gallery_entries:
                if room == entry["id"]:
                    vbox:
                        spacing 10
                        add Solid(gui.accent_color, xsize=gui.width, ysize=3) xalign 0.5
                        add entry["image"] size (gui.width * 0.4, gui.height  * 0.4)
                        text "'" + entry["title"] + "'"
                        text "{i}" + entry["artist"]+ "{/i}"