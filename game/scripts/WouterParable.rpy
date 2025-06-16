label wouter_parable:
    scene bg wouter parable door with fade

    speler "'The Wouter Parable’ (‘Het Wouter Fabeltje’)?"

    show esther casual idle at right
    with dissolve

    medewerkster """
    Het is een tijdelijke tentoonstelling.

    De exibitie gaat zometeen open.

    Wenst u deze te bezichtigen?
    """
    speler "Lijkt een beetje op een attractie uit een pretpark..."
    medewerkster "Dat is een zeer interessante opvatting. Het is meer een beleving dan een tentoonstelling van werken."

    show lena casual idle at center
    show sasha casual idle at left
    with dissolve

    """
    Meer mensen verzamelen aan de zaal deuren.

    De deuren gaan open en de mensen gaan naar binnen.
    """
    
    hide lena
    hide sasha
    with dissolve

    menu:
        "Niet binnen gaan.":
            speler "Ik bedenk me net dat er nog andere dingen zijn dat ik wil bekijken eerst."
            medewerkster "Geen probleem. Straks is er terug een vertooning dat u kunt bijwonen."
            speler "Bedankt."
            "Ik geef de medewerkster een glimlach en ga door naar een ander deel van het museum."
            pause .5
            jump choose_room

        "Binnen gaan":
            hide esther with dissolve
            "Ik wandel me naar binnen, de donkere kamer in."
    
    scene bg black with fade

    "..."
    sasha "Ooh nee, dit is echt super donker."
    lena "Stop met zagen..."
    "Ik hoor wat mensen rond mij zuchten en puffen."
    intercom """
    Hallo, en welkom in mijn wereld.

    Ik zou zeggen ‘blij van hier te zijn’, maar dat ben ik niet.
    """
    "De stem praat op een monotone manier."
    intercom """
    Het kantoor is een zooitje en ik wil het niet opruimen.

    Ik word daar zo moe van.
    """
    sasha "Pssst, [lena.name]? Is dit deel van de show?"
    "Duh, lijkt me nog al logisch eh."
    intercom "Nee, dit is geen show. Enkel een nare stem in een audio-box."
    sasha "Eeeeek." with vpunch
    intercom """
    Grapje eh.

    Dit is een opnamen. Een verhaal van een artist, anders dan andere, opgesloten in een wereld van normaliteit.
    """
    "De deuren gaan weer open en ik wandel de andere kamer binnen."
    
    scene bg wouter parable wide
    with fade

    "De kamer is lager dan andere zalen in het museum."
    scene bg wouter parable wide at Transform(
        zoom=1.2,
        yalign=0.5,
        xalign=0.0
    )
    with fade
    
    # Pan from left to right
    show bg wouter parable wide at pan_zoom  # Apply the transformation
    
    pause 5.0
    scene bg wouter parable wide with fade

    """
    De vloer is bedekt met papier. Zo te zien van een boek.

    Het geeft een 'office' vibe.
    """
    intercom """
    Pas op waar je stapt. De papieren van mijn manuscript liggen hier nog op de grond.
    Het zou het volgende best-selling boek moeten worden.

    Oké, nee dat was een leugen. Het is een mislukt verhaal van een hack schrijver.
    """
    "De stem klinkt verslagen. Hij verdringt zijn gevoelens met een poging tot humor."

    show lena casual glaring at right
    with dissolve
    
    lena "Dus de schrijver was slecht? Wat is er zo speciaal aan?"
    
    show lena at darken
    show sasha casual happy waku-waku at left
    with dissolve

    sasha """
    Nee niet waar. De pasages hier zijn eigenlijk goed geschreven en zelfs mooi.

    Hij mag niet opgeven.
    """

    show sasha at darken
    with dissolve

    intercom "Vind je echt dat het goed is?"
    speler "Was het geen opnamen? Het lijkt toch alsof iemand ons kan horen en zien."
    intercom "Nee hoor. Nogmaals, dit is een opgenomen stukje audio.

    De schrijver van dit deeltje dacht al dat jullie zo gingen reageren. Vandaar de reacties."

    show lena casual idle at spotlight
    with dissolve

    lena "Dus de schrijver van dit verhaal verwacht dat wij cliché reacties gaan geven op alles wat er gebeurt?"
    
    show lena at darken
    with dissolve

    intercom "Ja, het is een heel {i}meta{/i} verhaal."
    schrijver """
    Nee Intercom stem. Hou je maar aan het script.

    Dat is duidelijk al moeilijk genoeg voor jou.
    """
    """
    Een tweede stem is te horen over de speakers.

    Terwijl de twee stemmen beginnen te bikkeren, kijk ik rond
    """

    scene bg wouter parable mask
    with dissolve
    pause 1.0
    scene bg wouter parable metallic
    with dissolve
    pause 1.0
    scene bg wouter parable cotton
    with dissolve
    pause 1.0
    scene bg wouter parable wide
    with dissolve

    "De kamer telt drie kunstwerken. Een schilderij, een foto en een metalen plaat."

    sasha "Oooh [lena.name], kijk dat masker. Lijkt wat op een masker van carnaval."

    scene bg wouter parable mask
    with dissolve

    show sasha casual idle at right
    show lena casual idle at left
    with dissolve
    pause .5

    show sasha at darken
    with dissolve

    lena "Ja inderdaad. Het is duidelijk gebaseerd op de maskers die je ziet tijdens het carnaval van Venetië."
    
    show lena at darken
    with dissolve

    schrijver "Hey Intercom stem, let nu is op. Het is normaal jou taak van mensen uitleg te geven."
    intercom """
    Ja ja, zal de uitleg wel doen.

    Urhm.

    Dus aan jullie linkerkant zien jullie een werk genaamd ‘The Mask (Het Masker)’.
    """

    scene bg wouter parable cotton
    with dissolve

    intercom "En aan de rechterkant hebben we een schilderij genaamd ‘Cotton’s Portret'."

    show sasha casual happy waku-waku at left
    with dissolve

    sasha """
    O!{w=0.4} M!{w=0.4} G!

    Zij is zo schattig.
    """

    show sasha at darken
    with dissolve

    intercom """
    Ik ga helemaal akkoord met dat.

    Cotton is één van de hoofdpersonage van het boek.
    """

    show lena casual idle at right
    with dissolve

    lena "Boek? Als in dit mislukte manuscript?"
    "Ze wijst naar de pagina's op de grond."
    
    show lena at darken
    with dissolve

    intercom """
    Nee, nee, nee.

    Dat is{w=0.3}–euhm{w=0.3}–het manuscript van een andere schrijver.

    Puur ter illustratie dat boeken schrijven moeilijk.
    """
    show sasha casual teasing at spotlight
    with dissolve

    sasha "Lijkt me logisch. Als het makkelijk zou zijn, dan zou toch iedereen best-selling auteur worden?"

    show lena at spotlight
    show sasha at darken
    with dissolve
    lena "..."
    "Het blond meisje zucht en focust op het middelste werk."

    show lena at darken
    with dissolve

    intercom "Het verhaal heet `Metallic`. De metale poster toont Bobby."

    scene bg wouter parable metallic
    with dissolve 

    show sasha casual teasing at left
    with dissolve

    sasha "Dit begint verdacht te lijken op een advertentie."
    
    show sasha at darken
    with dissolve
    
    intercom "Nee hoor. We zijn nu in het jaar 2134, exact 100 jaar na het epische einde van Metallic."

    show sasha casual startled at spotlight
    with dissolve

    sasha "Huh? Wat?" with vpunch
    
    show sasha at darken
    show lena casual glaring at right
    with dissolve

    lena "Maak je niet druk, het is maar een verhaaltje."

    show lena casual idle with dissolve

    lena "Tijdreizen is onmogelijk."
    
    show lena at darken
    with dissolve

    intercom "Nee hoor. Dit is de toekomst."

    show lena at spotlight
    with dissolve

    lena "Oke dan. Wie is dan nu de president van Amerika?"

    show lena at darken
    with dissolve

    intercom "Wat doet dat er nu toe?"
    "De stem klinkt nerveus."

    show lena casual disgusted at spotlight
    with dissolve

    lena "Beantwoord de vraag."

    show lena at darken
    with dissolve

    intercom "Psst Stanley, Stanley... Wat doen we nu?"
    stanley """
    Geen idee, ze hebben het door denk ik.

    Snel beëindig de connectie.
    """

    intercom """
    Oké!

    .{w=.3}.{w=.3}.{w=.3}.{w=.3}.{w=.3}.{w=.3}.{w=.3}.{w=.3}
    """

    scene bg wouter parable wide
    show image "wall_glitch":
        alpha 0.1
        linear 0.5 alpha 0.8
    with dissolve

    speler """
    Huh?

    De muren? Wat gebeurt er?
    """

    show sasha casual startled at right
    show lena casual flustered at left
    with dissolve

    sasha "Eeeek, [lena.name] help me."
    lena "Wat gebeurt er hier?"

    scene bg black with fade

    pause 2

    scene bg wouter parable door with fade 

    speler "..."
    "Ik kijk rond. Ik sta voor een paar bekende deuren."
    speler "'The Wouter Parable’ (‘Het Wouter Fabeltje’)?"

    show esther casual idle at right
    with dissolve

    medewerkster """
    Het is een tijdelijke tentoonstelling.

    De exibitie gaat zometeen open.

    Wenst u deze te bezichtigen?
    """
    speler "Nee bedankt. Ik denk dat ik het maar ga overslaan."
    medewerkster "Oke, fijne dag nog."
    "Ze geeft me een vriendelijke glimlach terwijl ik verder wandel naar het volgende deel van de expositie."

    pause .5
    jump choose_room