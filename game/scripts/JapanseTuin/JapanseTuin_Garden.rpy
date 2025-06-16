    
label japanse_tuin_tuin:
    scene bg tuin wide-shot with w14

    "Ik betreed een ander deel van de Japanse tuin."

    show valerie casual smug at right
    with dissolve

    valerie "We ontmoeten elkaar weer."
    speler """
    Hey daar.

    Hoe vind je de tuin?
    \nRustgevend, of heb je wat meer chaos nodig?
    """
    
    show valerie casual idle with dissolve

    valerie """
    Nee, ik vind het goed zo.

    De zon is aangenaam en de tuin heeft een toffe layout.
    """
    
    scene bg tuin wide-shot at Transform(
        zoom=1.2,
        yalign=0.5,
        xalign=0.0
    )
    with fade
    show bg tuin wide-shot at pan_zoom

    """
    Ik kijk rustig rond in de tuin.

    De balans tussen planten, rotsen en water is heel aangenaam.
    Een oase van rust.
    """

    scene bg tuin wide-shot with fade

    show valerie casual idle at right
    with dissolve

    valerie "Zo te zien zijn er twee schilderijen om te bekijken."

    show valerie casual smug with dissolve

    valerie "Zullen we ze gaan bekijken?"
    speler "Ja, klinkt goed."

    scene bg black with wipeleft
    pause 0.1

    scene bg tuin poster2 at Transform(
        zoom=1.2,
        yalign=1.0,
        xalign=0.4
    )
    with wipeleft
    show bg tuin poster2 at pan_up
    pause 5.0

    scene bg tuin poster2 with fade
    show valerie casual idle at left
    with dissolve

    valerie """
    Er staat een tekstje onder het schilderij.

    ‘Misschien moeten we aan een andere locatie beginnen denken.’
    """
    speler "Zou het iets te maken hebben met het kind?"
    valerie "Het is wel een vrij absurd beeld."

    show valerie casual shocked with dissolve

    valerie "Wie zet er nu een kind onder een stolp?"
    speler "Misschien willen ze het kind beschermen van de harde buitenwereld?"

    show valerie casual idle zero-fucks with dissolve

    valerie "Sommige ouders zijn inderdaad zo."
    speler """
    Wat zou het kind er zelf van vinden?

    Het lijkt mij meer een kooi of gevangenis dan een vrij leven.
    """

    show valerie casual idle with dissolve

    valerie "Natuur moet vrij zijn en vrij gelaten worden. Dus ik kan zien waar het van komt."
    
    pause 0.3
    show valerie casual idle zero-fucks with dissolve
    pause 0.5

    valerie "..."
    "Ze valt stil..."

    show valerie casual idle with dissolve
    pause 0.7
    show valerie casual smug with dissolve

    valerie "Kom laten we het andere werk bekijken."

    hide valerie with dissolve

    """
    Ze wandelt rustig verder.

    Zo te zien had dit een impact op haar. Dat is de magie van kunst...
    \n{w=0.7}Denk ik.
    """
    
    scene bg black with wipeleft
    pause 0.1

    scene bg tuin poster1 at Transform(
        zoom=1.2,
        yalign=1.0,
        xalign=0.4
    )
    with wipeleft
    show bg tuin poster1 at pan_up
    pause 5.0

    scene bg tuin poster1 with fade

    "Het andere schilderij heeft ook een tekstje."

    show valerie casual idle at left
    with dissolve

    valerie """
    ‘Durf groots te dromen.’

    Past wel goed met het beeld.
    """
    speler """
    Inderdaad.

    Een groot schilderij met een grote boodschap.
    """
    
    show valerie casual smug with dissolve

    valerie "Ik vind het vooral leuk dat het schilderij op meerdere niveaus werkt."
    speler "Aah, omdat het meisje op een andere laag bestaat dan de rest?"
    
    show valerie casual idle with dissolve

    valerie "Onder andere."

    scene bg tuin poster1 at Transform(
        zoom=1.2,
        yalign=1.0,
        xalign=0.4
    )
    with fade
    show bg tuin poster1 at pan_up

    valerie """
    Maar ook meer de betekenis en de compositie.

    Het lijkt alsof zij het landschap heeft gemaakt. Maar tegelijk is ze ook onderdeel van het landschap.
    """

    speler """
    Nu je het zegt. De damp van haar tas maakt de wolken in het landschap.

    Dus zou de boodschap dan eerder iets betekenen van ‘laat je creatieve dromen niet liggen’?
    """
    
    scene bg tuin poster1 with fade
    show valerie casual idle at left
    with dissolve

    valerie """
    Dat is een mooi idee.

    Als je er zo naar kijkt krijg je toch vanzelf zin om iets te gaan maken.
    \nEen schilderij, een tekening, muziek, films, … noem maar op.
    """

    speler "Wie weet wat er kan gebeuren."

    scene bg tuin poster1 at Transform(
        zoom=1.2,
        yalign=0.5,
        xalign=0.0
    )
    with fade
    show bg tuin poster1 at pan_zoom

    "We kijken samen nog eventjes naar het werk en gaan dan elk weer onze eigen weg."

    speler "Misschien moet ik zelf eens iets maken, kan wel is tof zijn."



