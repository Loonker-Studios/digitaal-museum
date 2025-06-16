label japanse_tuin_galerij:
    scene bg tuin gallerij wide-shot with fade

    "Een grote open zaal."

    scene bg tuin gallerij wide-shot at Transform(
        zoom=1.2,
        yalign=0.5,
        xalign=0.0
    )
    with dissolve

    show bg tuin gallerij wide-shot at pan_zoom
    
    "Ik zie kunstwerken aan de muren maar een set van zwevende bladen trekt mijn aandacht."

    scene bg tuin gallerij close-up 1 with dissolve

    "Het is een collectie van prints.
    \nZe zitten in glazen kaders die in de lucht hangen. Zo te zien door heel fijne staaldraad."
    speler "Japans papier?"

    scene bg tuin gallerij wide-shot with dissolve
    pause 0.5
    show valerie casual idle at right
    with dissolve

    valerie "Mooi, eh?"
    speler """
    Het is best wel uniek.

    Maar waarom ‘Japans papier’?
    """
    valerie """
    Eigenlijk heet het ‘Washi papier’. Men noemt het zo omdat het van Japan komt.

    Het is dun en semi-transparant.
    """
    
    hide valerie with dissolve

    valerie "Als je hier kijkt is het duidelijker."

    scene bg tuin gallerij close-up 2 with dissolve

    "Ze wijst naar één van de werken."

    show bg tuin gallerij close-up 2 at Transform(
        zoom=1.5,
        yalign=1.0,
        xalign=0.0
    ) with dissolve

    speler "Ah ja, nu je het zegt."

    scene bg tuin gallerij close-up 2 with dissolve
    show valerie casual idle at right
    with dissolve

    valerie """
    Volgens de beschrijving is het een ‘glitch-art’ versie van Japanse Tuinen.

    Het past dan ook dat ze geprint zijn op ‘Japans papier’.
    """
    speler "De hele ruimte lijkt me redelijk Japans. Verschillende kunstwerken die te maken hebben met Japan."

    show valerie casual smug
    with dissolve

    valerie "En met een uitzicht op een Japanse tuin."
    speler "Een heel thema dus."

    scene bg tuin gallerij close-up 2 at Transform(
        zoom=1.2,
        yalign=0.5,
        xalign=0.0
    )
    with dissolve
    show bg tuin gallerij close-up 2 at pan_zoom
    
    "Ik bekijk de werken van wat dichter bij."
    speler "Ligt het aan mij, of ontbreekt de rust hier?"
    valerie """
    Nu je het zegt.

    Japanse tuinen staan bekend om hun rustgevende omgeving. Maar de glitching brengt wanorde.
    """
    
    scene bg tuin gallerij close-up 2 with dissolve

    show valerie casual idle at right
    with dissolve

    valerie "Ik vind het wel een interesante interpretatie."
    speler "Dat de tuin nu een zooitje is?"

    show valerie casual idle zero-fucks with dissolve

    valerie "Chaos! Groot verschil."

    show valerie casual smug
    with dissolve

    valerie """
    Chaos is een natuurlijke orde.
    \nEr is rust in chaos.
    """
    speler """
    Ik snap het. 

    Net zoals natuur zijn natuurlijk gang gaat.

    Het lijkt chaos voor ons mensen, maar de natuur harmoniseert natuurlijk.
    """

    show valerie casual idle with dissolve

    valerie """
    Leuke pun.

    En het is een goed punt. Chaos is natuurlijk.
    """

    hide valerie with dissolve

    "Ik kijk rustig verder terwijl ze door loopt."
    pause 3.0
    speler "Oh ja,{w=1.0} er is nog een Japanse tuin om te bezoeken."

    scene bg black with w14
    pause 0.5

    jump japanse_tuin_tuin