import math

class Test:
    def __init__(self, name, align, **abilities):
        self.name = name
        self.align = align

        for key in abilities:
            setattr(self, key, abilities[key])

def set_modifier(level):
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

def damage(attacker, hit, enemy):
    enemy.current_modifiers()
    enemy.current_condition()
    if hit == 'crit':
        setattr(enemy, 'current_HP', enemy.current_HP - 2 - (attacker.str_mod * 2))
        return enemy.current_HP
    if hit == 'hit':
        setattr(enemy, 'current_HP', enemy.current_HP - 1 - (attacker.str_mod))
        return enemy.current_HP

class Character:

    first = ['Chaotic', 'Neutral', 'Lawful']

    second = ['Evil', 'Good', 'Neutral']
    
    def __init__(self, name, align, strength = 10, dexterity = 10, constitution = 10, wisdom = 10, intelligence = 10, charisma = 10):
        self.name = name
        self.alignment = align
        self.base_hp = 5
        self.armor_class = 10
        self.xp = 0
        self.player_level = 1
        self.strength = strength        
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    def current_modifiers(self):
        self.str_mod = set_modifier(self.strength)
        self.dex_mod = set_modifier(self.dexterity)
        self.armor_class += self.dex_mod
        self.const_mod = set_modifier(self.constitution)
        self.max_HP = self.base_hp + self.const_mod

    def current_condition(self):
        self.current_HP = self.max_HP
    
    def attack(self, roll, enemy):
        self.current_modifiers()
        enemy = enemy
        EAC = enemy.armor_class
        if roll == 20:
            damage(self, 'crit', enemy)
            self.xp += 10
            self.ll = math.floor((self.xp/1000)+1)
            return 'CRIT'
        elif EAC < roll + self.str_mod:
            # self.damage('hit', enemy)
            self.xp += 10
            self.player_level = math.floor((self.xp/1000)+1)
            return "HIT"
        elif EAC >= roll + self.str_mod:
            return "MISS"

    def level_check(self):
        self.max_HP = self.baseHP + (self.player_level * 5) + (self.player_level * self.const_mod)






