from core.music import EFFECT


class Skill:
    def __init__(
        self,
        id,
        name,
        sound,
        multiplier=1,
        effect=None,
    ):
        self.id = id
        self.name = name
        self.sound = sound
        self.multiplier = multiplier
        self.effect = effect


KICK = Skill(id="kick", name="Chute", sound=EFFECT["kick"])

BITE = Skill(id="bite", name="Mordida", multiplier=2, sound=EFFECT["bite"])

skills = [KICK, BITE]
