label monogroom:
    scene bg poc rgb with dissolve

    show sasha casual happy waku-waku at center
    with dissolve 

    sasha "Nee, dat is een vlinder."

    show natalie casual curious smug at right
    show sasha at darken
    with dissolve

    natalie "Nee, dat is een slechte Mickey Mouse."
    
    show sasha casual thinking at spotlight
    show natalie at darken
    with dissolve

    sasha "Uhhmm, nee."

    show valerie casual idle zero-fucks at left
    show sasha at darken
    with dissolve

    valerie "[sasha.name], het maakt niet uit wat jij of [natalie.name] ziet. Ik vroeg je enkel wat je er van vindt."
    "Zo te zien zijn deze meisjes discussie aan het voeren over wat je er kan zien."

    scene bg poc rgb at Transform(
        zoom=1.2,
        yalign=0.5,
        xalign=0.0
    )
    with fade
    
    # Pan from left to right
    show bg poc rgb at pan_zoom  # Apply the transformation

    "Ik laat mijn ogen glijden over de 3 metale platen."

    scene bg poc rgb with fade

    show sasha casual idle at center
    show natalie casual idle at right, darken
    with dissolve

    sasha "Oke, oke.."
    
    show sasha casual idle big-smile with dissolve

    sasha "Eerst en vooral: Love de 3 kleuren pallet. Rood, blauw en groen net zoals de RGB waardes van computers."

    show sasha at darken
    show natalie at spotlight
    with dissolve

    natalie "Nu je het zegt, het lijkt er wel op."

    show sasha at spotlight
    show natalie at darken
    with dissolve
    pause 0.3
    show sasha casual thinking with dissolve

    sasha "Uhm... Ik vind de variaties wel tof. Zo samen zo."

    show sasha at darken
    show valerie casual idle at left
    with dissolve

    valerie "Snap ik, het zorgt ervoor dat het toch niet èèn tonig aan voelt."

    show valerie at darken
    show natalie at spotlight
    with dissolve

    natalie "Het gebruik van metaal maakt het ook een beetje uniek."

    show natalie casual boosting with dissolve
    
    natalie "Als je rondkijkt hier, de andere werken hier zijn foto’s in kaders. Dit voelt anders aan."

    show sasha at spotlight
    show natalie at darken
    with dissolve
    sasha "Nu je het zegt ja."

    show sasha casual idle big-smile with dissolve

    sasha "Haha, zo had ik er nog niet over nagedacht."
    "Zo te horen hebben deze meisje toch wel veel te zeggen over dit werk."

    show sasha at darken
    show valerie at spotlight
    with dissolve

    valerie "Het is wel raar dat de kleur van plaat impact heeft op wat je er in ziet. [natalie.name] zag Mickey Mouse en [sasha.name], jij zag een vlinder."

    show valerie casual smug with dissolve

    valerie "Als je van dichtbij kijkt zie je duidelijk dat het geen van beide is."

    hide sasha
    hide natalie
    hide valerie
    with dissolve
    
    "De meisjes gaan om de beurt dichter kijken naar het werk."

    show sasha casual questioning smug at center
    with dissolve

    sasha "Nu je het zegt zie ik het. Het is een berg en bomen."

    show sasha at darken
    show natalie casual curious smug at right
    with dissolve

    natalie """
    Ja, iets van visueel effect moet gebruikt zijn om het zo te vervormen dat het op iets anders lijkt.

    Wat een tof idee.
    """

    show natalie at darken
    show valerie casual idle at left
    with dissolve

    valerie "Jep, het geeft een andere kijk op de wereld."

    show valerie at darken
    show sasha at spotlight
    with dissolve
    pause .5
    show sasha casual happy waku-waku with dissolve

    sasha "Hey, kom kijken. Deze fotos zijn ook wel tof. Al die kleuren."

    hide sasha with moveoutright

    """
    Ondertussen is 1 van hen al verder gewandeld naar een ander werk.

    {i}Bergen he?{/i}
    """

    hide valerie
    hide natalie
    with moveoutright

    "De andere meisjes wandelen nu ook verder. Nu die weg zijn kan ik ook wat dichter gaan staan."

    speler "Waar zijn die bergen?"

    menu:
        "Ik inspecteer het werkje van dichtbij..."
        "Oh ja, nu zie ik het.":
            speler "Tof."
        "Ik zie het toch niet ze.":
            speler "Spijtig."

    "Ik zet terug een paar stappen achteruit en wandel verder naar het volgende werk."

    jump glitch_art_1_6