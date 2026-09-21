from skills import skill


class Monster:
    def __init__(self, id, name, health, damage, defense, attacks) -> None:
        self.id = id
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.attacks = attacks


rat = Monster("rat", "Rato", 5, 1, 1, [skill.BITE])
