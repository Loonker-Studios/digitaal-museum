label intro:
    # TODO implement
    scene bg black with fade

    show teresa casual idle at center
    with dissolve

    medewerkster """
    Welkom bij het Digitaal Museum.
    \n(klik op “spatie”,“enter” of “linker muis knop” om verder te gaan.)

    In dit museum kan je werken bekijken van de hogere graad Digitaal Atelier.

    Tijdens je bezoek gaan er andere bezoekers met jou praten.

    Het is ook interactief, dus je gaat keuzes krijgen zoals dit:
    """

    menu :
        "Ik moet met de muis op een keuze klikken."

        "Oké, Ik snap het":
            medewerkster "Perfect."

    show teresa casual idle happy with dissolve

    medewerkster "Ik wens je veel plezier met je bezoek."

    hide teresa

    jump choose_room
    