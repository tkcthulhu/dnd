import math

class Test:
    def __init__(self, name, align, **abilities):
        self.name = name
        self.align = align

        for key in abilities:
            setattr(self, key, abilities[key])



class Character:

    DEFAULT_ATTRIBUTES = {
        "strength": 10, 
        "dexterity":10,
        "constitution":10,
        "wisdom": 10,
        "intelligence": 10,
        "charisma": 10,
        "base_hp": 5,
        "armor_class": 10,
        "xp": 0,
        "player_level": 1,
    }

    first = ['Chaotic', 'Neutral', 'Lawful']

    second = ['Evil', 'Good', 'Neutral']
    
    def __init__(self, name, align, **DEFAULT_ATTRIBUTES):
        self.name = name
        self.alignment = align

        for key in DEFAULT_ATTRIBUTES:
            setattr(self, key, DEFAULT_ATTRIBUTES[key])

    def stats(self, strength, dexterity, constitution, Wis, Int, Char):
        self.strength = strength
        self.str_mod = self.modifier(strength)
        self.dexterity = dexterity
        self.dex_mod = self.modifier(dexterity)
        self.armor_class += self.dex_mod
        self.constitution = constitution
        self.const_mod = self.modifier(constitution)
        self.max_HP = self.baseHP + self.const_mod
        self.Wisdom = Wis
        self.Intelligence = Int
        self.Charisma = Char  

    def modifier(self, level):
        if level == 1:
            return -5
        if level == 2 or level == 3:
            return -4
        if level == 4 or level == 5:
            return -3
        if level == 6 or level == 7:
            return -2
        if level == 8 or level == 9:
            return -1
        if level == 10 or level == 11:
            return 0
        if level == 12 or level == 13:
            return 1
        if level == 14 or level == 15:
            return 2
        if level == 16 or level == 17:
            return 3
        if level == 18 or level == 19:
            return 4
        if level >= 20:
            return 5
    
    def attack(self, roll, enemy):
        enemy = enemy
        EAC = enemy.armor_class
        if roll == 20:
            self.damage('crit', enemy)
            self.xp += 10
            self.player_level = math.floor((self.xp/1000)+1)
            return 'CRIT'
        elif EAC < roll + self.str_mod:
            self.damage('hit', enemy)
            self.xp += 10
            self.player_level = math.floor((self.xp/1000)+1)
            return "HIT"
        elif EAC >= roll + self.str_mod:
            return "MISS"

    def level_check(self):
        self.max_HP = self.baseHP + (self.player_level * 5) + (self.player_level * self.const_mod)

    def damage(self, hit, enemy):
        if hit == 'crit':
            setattr(enemy, 'hit_points', enemy.hit_points - 2 - (self.str_mod * 2))
            return enemy.hit_points
        if hit == 'hit':
            setattr(enemy, 'hit_points', enemy.hit_points - 1 - (self.str_mod))
            return enemy.hit_points




