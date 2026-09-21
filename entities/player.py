from skills import skill


class Player:
    def __init__(self, health=10, damage=3, defense=1, level=1):
        self.health = health
        self.damage = damage
        self.defense = defense
        self.xp = 0
        self.xp_necessary = 10
        self.level = level
        self.inventory = []
        self.attacks = [skill.KICK]

    def get_info(self, nickname, health=0, damage=0, defense=0, xp=0, level=1):
        self.nickname = nickname
        self.health = health
        self.damage = damage
        self.defense = defense
        self.xp = xp
        self.level = level
        self.inventory = {}

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.xp_necessary = 0

        self.health += 10
        self.damage += 5
        self.defense += 3

    def learn_attack(self, attack:skill.Skill):
        self.attacks.append(attack)

player = Player()
