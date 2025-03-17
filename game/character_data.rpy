init python:
    class DDCharacter:
        def __init__(self, name, nickname=None):
            self.name = name
            if nickname is None:
                self.nickname = name
            else:
                self.nickname = nickname

# Create character objects with additional properties
init python:
    valerie_data = DDCharacter(name="Valerie")
    teresa_data = DDCharacter(name="Teresa", nickname="Mom")
    aurora_data = DDCharacter(name="Aurora")
    sasha_data = DDCharacter(name="Sasha")
    esther_data = DDCharacter(name="Esther", nickname="Mum")
    lena_data = DDCharacter(name="Lena")
    natalie_data = DDCharacter(name="Natalie")