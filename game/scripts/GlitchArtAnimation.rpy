label glitch_art_animation:
    scene bg glitch-animation 1 with fade

    show natalie casual idle happy at left
    show lena casual glaring at right, darken
    with dissolve

    natalie "Oooh ja het beweegt echt!"

    show natalie at darken
    show lena at spotlight
    with dissolve

    lena "Nee. Het kan niet bewegen."
    "Zo te zien zijn deze twee meisjes over iets aan het discussiëren."

    show natalie casual curious smug at spotlight
    show lena at darken
    with dissolve

    menu optional_name:
        "Ze wijst naar mij."
        "Ik?":
            pause 0.6
            show natalie at nod_once
            "Ze knikt."
        "Huh?":
            pause 0.6
            show natalie at nod_once
            "Ze knikt."

    natalie """
    Ja, jij.

    Kom eens kijken.
    \nDeze foto,{w=0.4} schilderij,{w=0.4} whatever,{w=0.2} kan bewegen.
    """
    speler "De enige manier een foto kan bewegen is als het een video was."

    show natalie casual idle deadpan with dissolve

    natalie "Wel, het is een normale foto."

    scene bg glitch-animation close-up with dissolve

    "We bekijken het werk van dichtbij."
    speler """
    Het lijkt mij een normale foto.

    Hoe kan die dan bewegen?
    """

    show natalie casual idle at left, darken
    show lena casual glaring at right
    with dissolve

    lena "Dat is wat ik ook al zei. Maar volgens madam hier kan het bewegen als je maar ‘genoeg gelooft’."

    show lena casual angry
    with dissolve

    lena "Er is toch geen indicatie dat dit kan bewegen?"

    show natalie at spotlight
    show lena at darken

    natalie "Oke, laten we terug wat naar achter gaan en dan leg ik het uit."

    scene bg glitch-animation 1 with dissolve

    show natalie casual idle at left
    show lena casual idle at right, darken
    with dissolve

    natalie """
    Dus, ik heb onlangs iets gelezen over ‘kinetic art’. Het is een bewegende kunst vorm, vaak gezien in beeldhouwwerken.

    Beweging is een centraal thema in de werkjes. En hier gebeurt dat door een spel van kleuren en licht.
    """

    show lena casual flustered at spotlight
    show natalie at darken
    with dissolve

    lena """
    Maar dat verklaart nog niet waarom een foto zou kunnen bewegen.

    Een foto is een snapshot in tijd. Het representeert één specifiek moment.
    """

    show natalie casual idle wink at spotlight
    show lena at darken
    with dissolve

    natalie "Half, maar zeg dat best niet tegen fotografen."

    show natalie casual idle
    with dissolve

    natalie "Nee, hier zijn de lijnen of het object ook niet in ‘beweging’. Maar als je gelooft dat het kan bewegen kan het wel veranderen."

    show natalie at darken
    show lena casual glaring at spotlight
    with dissolve

    lena "Hier ga je weer."

    show natalie casual curious wink at spotlight
    show lena at darken
    with dissolve

    natalie "Daarom dat ik het aan deze geweldige persoon vraag."
    speler """
    Dus wat moet ik doen? 

    Want ik geef haar gelijk.
    \nBij mijn weten kunnen normale fotos niet bewegen.
    """

    show natalie casual idle
    with dissolve

    natalie """
    Het is heel simpel.

    Kijk naar de foto en geloof dat het kan bewegen.
    """

    show natalie casual idle happy
    with dissolve
    natalie "Zo simpel is het."

    speler "Oke, ik zal het is proberen."

    scene bg black with eyesclosed

    menu :
        "..."
        "{i}Het kan bewegen.{/i}":
            jump glitch_art_animation_a
        "{i}Het kan niet bewegen.{/i}":
            jump glitch_art_animation_b
    return

label glitch_art_animation_a:
    """
    {i}Foto’s kunnen bewegen.{/i}

    {i}Ik bedoel maar, dit kan bewegen. Dit museum heeft me al meer fantastische elementen laten zien dus waarom zou een foto niet kunnen bewegen.{/i}

    {i}Er is ook geen rede dat dit meisje zou liegen.{/i}

    {i}Als het maar gaat over geloven dat het beweegt, dan wil ik het graag geloven.{/i}
    """
    natalie "{size=*0.6}Het kan bewegen. Geloof in de mij dat gelooft in jou."
    """
    Haar woorden,{w=1} ze dringen door tot diep in mij.

    De foto kan bewegen.
    """
    speler "{size=*0.6}De foto kan bewegen."

    scene bg glitch-art animation with eyesopen
    pause 1.0

    show natalie casual curious smug at left
    with dissolve

    natalie "En? Kan je het zien?"

    speler """
    Ja, de foto beweegt.

    Ze veranderd langzaam van kleur en vorm.
    """

    show natalie at darken
    show lena casual flustered at right
    with dissolve

    lena "Kan niet. Neem je me nu in de maling!?"
    speler """
    Nee, ik meen het echt. Het beweegt.
    
    Alsof het danst.
    """

    show natalie at spotlight
    show lena at darken
    with dissolve

    natalie "Ik zei het toch. Kom probeer jij nu."

    show lena casual glaring at spotlight
    with dissolve
    
    lena "Urgh oké."

    show lena casual pouting blush
    with dissolve

    lena "Ik zal het nog is proberen."

    hide lena
    hide natalie
    with dissolve

    "Ze sluit haar ogen en bereid haar voor."
    speler "..."
    pause 2
    "Haar ogen gaan terug open."
    speler "..."
    
    show lena casual flustered at right
    with dissolve
    
    lena "Wauw, je hebt gelijk. Misschien geloofde ik het niet hard genoeg."
    speler "Blij dat je het nu ook kon zien. Mooi eh?"

    show lena casual idle with dissolve

    lena "Ja, het is heel mooi."

    show natalie casual idle happy at left
    with dissolve

    "Met een glimlach op hun gezicht lopen de meisje weer verder."

    hide natalie
    hide lena
    with fade

    "Ik kijk nog eventjes naar het werk."
    speler "Kinetic art? Het is me wat."

    return


label glitch_art_animation_b:
    speler "Foto’s kunnen echt niet bewegen."
    natalie "Je moet je geest verruimen. Probeer het eens."
    speler "Fijn..."
    "{i}Als ik men ogen open doen gaat het toch niet kunnen bewegen.{/i}"

    scene bg glitch-animation 1 with eyesopen

    speler "..."
    pause 2.0
    speler "Het beweegt niet hoor."

    show lena casual glaring at right
    show natalie casual idle at left, darken
    with dissolve

    lena "Ik zei het toch."
    
    show natalie casual idle wink at spotlight
    show lena at darken
    with dissolve
    
    natalie "Je gelooft niet genoeg. Probeer het nog eens."

    menu:
        "..."
        "Ik zal nog een keer proberen.":
            speler "Oke. Ik zal het nog een keer proberen."
            scene bg black with eyesclosed
            jump glitch_art_animation_a
        "Ik denk dat het toch niets voor mij is.":
            speler "Ik denk niet dat het kan bewegen."

    show natalie casual idle at darken
    show lena casual angry at spotlight
    with dissolve

    lena "Zie je wel. Foto’s kunnen niet bewegen."

    show natalie at spotlight
    show lena at darken
    with dissolve

    natalie "Spijtig dat jullie het niet kunnen zien. Het is echt de moeite om te zien."

    show lena casual glaring at spotlight
    show natalie at darken
    with dissolve

    lena "Fijn voor jou."

    hide lena
    hide natalie
    with fade
    
    """Ik kijk nog eventjes naar het werk.

    {i}Misschien kan het toch bewegen. Wie weet...{/i}"""

    pause .5
    jump choose_room
