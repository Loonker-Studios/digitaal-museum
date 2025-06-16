label choose_room:
    scene bg black
    with dissolve

    "Alright, welke zaal zal ik eens bezoeken?"

    python:
        choices = []
        for room in rooms:
                choices.append((room["message"], room["label"]))

        choices.append(("Ik ben klaar voor nu.", "exit"))

        result = renpy.display_menu(choices)

        if result == "exit":
            renpy.jump("end_label")
        else:
            for room in rooms:
                if room["label"] == result:
                    room["visited"] = True
                    visited_rooms.append(room["id"])
                    break
            renpy.jump(result)

label end_label:
    return

