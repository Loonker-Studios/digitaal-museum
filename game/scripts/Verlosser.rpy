label verlosser:
    scene bg verlosser
    show image "foggy" onlayer texture
    with fade
    "Er hangt een mist in de kamer."

    speler "Volgens de uitleg is de ‘De Verlosser’ gebaseerd op een bewakerspoort."

    scene bg verlosser at Transform(
        zoom=1.2,
        yalign=0.5,
        xalign=0.4
    ) 
    with dissolve

    speler "Het heeft wel een eng gezicht."

    show vignette_65:
        blend "multiply"
    with dissolve

    "..."

    scene bg verlosser at Transform(
        zoom=1.4,
        yalign=0.3,
        xalign=0.45
    ) 
    show vignette_65:
        blend "multiply"
    with dissolve

    "Om één of andere rede kan ik mijn ogen niet los maken van de gloed."
    speler "Wie of wat is ‘De Verlosser’..."


    scene bg verlosser at Transform(
        zoom=1.4,
        yalign=0.3,
        xalign=0.45
    ), AnimatedAberate
    show vignette_65:
        blend "multiply"
    show static:
        blend "multiply"
    with dissolve 

    verlosser "Ik ben de bewaker van de Temple van Balans."
    """
    Ik hoor een stem.

    Maar het lijkt niet van een speaker te komen...
    """
    verlosser """
    In een ander leven,{w=.5} in een andere tijd,{w=.5} in een andere wereld{w=.5} was ik ooit een mens.

    Ik preekte vrede en balans maar een corupt geloof vond dat maar niets.

    Na jaren conflict kwam ik tragisch om het leven.

    De goden die ik heel men leven heb aanbeden namen mij mee naar een heilige tempel.

    Daar werd ik aangeduid als eeuwige bewaker.
    """
    speler "Hoe liep de strijd af?"
    
    verlosser """
    ...{w=1}

    Daar heb ik zelf geen idee van.
    """
    speler "Wat hoop je zelf?"
    verlosser """
    Ik hoop dat de wereld terug balans heeft gevonden.

    Mijn enige wens is voor balans in de wereld.
    \n{w=.5}Balans tussen mensheid en natuur. {w=.5}Balans tussen mensen. {w=.5}En {size=*.9}balans {/size}{size=*.8}tussen {/size}{size=*.7}mensen {/size}{size=*.6}en {/size}{size=*.5}goden{/size}{size=*.4}{w=.4}.{/size}{size=*.3}{w=.4}.{/size}{size=*.2}{w=.4}.
    """
    "De stem vervaagt."

    scene bg black
    hide image "foggy" onlayer texture with fade
    pause .7
    scene bg verlosser with eyesopen
    speler "Huh?"

    scene bg black with eyesclosed_fast
    pause .2
    scene bg verlosser with eyesopen_fast

    scene bg verlosser at Transform(
        zoom=1.2,
        yalign=0.5,
        xalign=0.0
    ) 
    with fade
    scene bg verlosser at pan_zoom

    "De mist is weg en de kamer lijkt me terug normaal."

    speler "Wat was dat? Het voelde zo echt."

    "Ik kijk nog een keer naar de projectie "

    scene bg verlosser qr with dissolve

    extend "en lees de uitleg."
    speler """
    'De verlosser.
    \nEen ornament op de poort van een 19de eeuwse protestantse kerk.'
    """

    "Wat was dat verhaal dan? Het voelde aan als een sprookje of een fantasie wereld."

    scene bg verlosser with fade

    "Misschien liet ik men verbeelding wat te vergaan. Maar toch, het voelde zo echt."
    speler "Dat is de kracht van kunst zeker?"
