label glitch_art_1_6:
    scene bg black with fade
    scene bg poc glitch-art
    with dissolve

    speler """
    Glitch art?

    Wat moet ik mij bij voorstellen?
    """

    show lena casual glaring at right
    with dissolve

    lena "Wat een rommeltje is me dat."
    speler "Oh ja? Waarom vind je dat?"
    lena "Kijk nu toch, het zijn 6 foto's die niets met elkaar te maken hebben."

    show lena casual idle with dissolve

    lena "Oke ja, je kan zeggen dat het meisje voor komt in 3 werkjes maar dan vallen die andere 2 werkjes uit de boot."
    
    menu:
        "Is het niet de chaos van de werkjes dat ze bij elkaar laat horen?":
            call glitch_art_1_6_a from _call_glitch_art_1_6_a
        "Ja, nu je het zegt... Je heb mogelijks wel gelijk.":
            call glitch_art_1_6_b from _call_glitch_art_1_6_b

    pause .5
    jump choose_room

label glitch_art_1_6_a:
    show lena casual disgusted 
    with dissolve

    lena "Chaos"
    
    show lena casual idle with dissolve

    extend "..."
    "Het meisje naast mij valt stil."
    lena """
    Hmmm...

    Oke ja, ik kan het wel een beetje zien zo. Het zijn 6 werkjes met een chaos van kleuren en vormen.
    """
    speler "Dat lijkt me toch wel heel kort door de bocht, vind je niet?"

    show lena casual disgusted with dissolve

    lena "Het lijkt me meer dat de artiest zijn brein aan het flippen was en hij of zij dit werk heeft uitgespuugd op papier."
    speler "De titel bevat het woord \"Glitch\", mogelijks slaagt het op een computer glitch?"
    
    show lena casual glaring with dissolve

    lena """
    Dat is dom. Waarom zou iemand dat willen doen? Is dat niet heel het ding van digitaal werken, dat je fouten makkelijk ongedaan kan maken?

    Waarom zou je kiezen voor de fouten resultaten juist te presenteren?
    """

    menu:
        "Fouten maken is mensenlijk.":
            show lena casual idle 
            with dissolve

            lena "Mogelijks. Als het gaat om een computer glitch en als dat het meer menselijk maakt kan ik het wel een beetje zien."
            speler "En als het toch niet de bedoeling is? Dat een computer menselijk lijkt?"
            lena """
            Dan...

            Goh, de kleuren zijn nog wel mooi. Allemaal een beetje te druk maar toch wel mooi.
            """
            "Ik kijk nog eventjes verder naar het werk terwijl het blonde meisje rustig verder wandelt."
        
        "Wat een dom concept.":
            show lena casual idle 
            with dissolve

            lena """
            Akkoord. 

            Fouten kunnen gebeuren maar dan kiezen om de fouten bij te houden en te pressenteren is dom naar mijn mening.

            Als mensen deze chaos mooi of interessant vinden, goed voor hen. Maar persoonlijk vind ik dit maar niets.
            """
            speler "Iedereen heeft zijn eigen mening en smaak."
            lena "Goed gezegd."
            "Ik kijk nog eventjes naar werk. Ondertussen loop het blonde meisje rustig verder door het museum."

    # continue after menu
    hide lena with dissolve
    return

label glitch_art_1_6_b:
    show lena casual idle 
    with dissolve

    lena "De 2 werkjes rechts kan je tegen elkaar schuiven en dan is het precies 1 foto."

    show lena casual disgusted with dissolve

    lena "Wel met een overduidelijke voorkeur voor zo veel mogelijk kleur in de ogen van de bezoeker te werpen."
    speler """
    Daar heb je een punt, er is veel kleur in deze 6 fotos.

    Maar wat vind je van dat werkje?
    """
    "Ik wijs naar de foto met het meisje."

    show lena casual idle with dissolve

    lena """
    Dat?

    Ze kijkt zo verveeld. Ook al is ze het centrum van heel deze kleuren chaos.
    """
    speler "Zou het iets betekenen?"
    lena """
    Goh, ik weet het niet.

    Naar mijn mening is dit maar niets. Maar ik heb al anderen mensen hier over spreken.

    Voor sommige stelt dit werk de {i}"eenzaamheid van de moderne tiener"{/i} voor. Persoonlijk vind ik dat wat belachelijk.
    """
    speler "Maar?"
    lena """
    Maar, ik kan er wel iets anders in zien.

    Om eerlijk te zijn, de wereld voelt vaak als chaos aan.

    Wat als dit werk die chaos voorstelt? Maar dan nog intenser dan in het echt?
    """
    speler "Ja, zou wel is kunnen."
    lena "..."

    "Ze valt stil."

    hide lena with dissolve

    "Ik kijk rustig verder naar het werk terwijl het meisje verder wandelt door de gang."
    speler "Glitch art... Het is toch wel iets anders."

    return