import math

class Test:

    DEFAULT_ATTRIBUTES = {
        'strength' : 10, 
        'dexterity' : 10, 
        'constitution' : 10, 
        'wisdom' : 10, 
        'intelligence' : 10, 
        'charisma' : 10,
        'player_level' : 1
    }

    def __init__(self, name, align, **abilities):
        self.name = name
        self.align = align

        for key in self.DEFAULT_ATTRIBUTES:
            setattr(self, key, self.DEFAULT_ATTRIBUTES[key])

def set_modifier(level):
    return math.floor((level - 10) / 2)

class Combat: 

    def attack(attacker, roll, enemy):
        attacker = attacker
        enemy = enemy
        EAC = enemy.armor_class
        if roll == 20:
            Combat.damage(attacker, 'crit', enemy)
            attacker.xp += 10
            attacker.player_level = math.floor((attacker.xp/1000)+1)
            return 'CRIT'
        elif EAC < roll + attacker.str_mod:
            Combat.damage(attacker, 'hit', enemy)
            attacker.xp += 10
            attacker.player_level = math.floor((attacker.xp/1000)+1)
            return "HIT"
        elif EAC >= roll + attacker.str_mod:
            return "MISS"    

    def damage(attacker, hit, enemy):
        enemy.current_condition()
        if hit == 'crit':
            setattr(enemy, 'current_HP', enemy.current_HP - 2 - (attacker.str_mod * 2))
            enemy.current_condition()
            return enemy.current_HP
        if hit == 'hit':
            setattr(enemy, 'current_HP', enemy.current_HP - 1 - (attacker.str_mod))
            enemy.current_condition()
            return enemy.current_HP

class Character:

    first = ['Chaotic', 'Neutral', 'Lawful']

    second = ['Evil', 'Good', 'Neutral']

    DEFAULT_ATTRIBUTES = {
        'strength' : 10, 
        'dexterity' : 10, 
        'constitution' : 10, 
        'wisdom' : 10, 
        'intelligence' : 10, 
        'charisma' : 10,
        'player_level' : 1
    }
    
    def __init__(self, name, align, strength = 10, dexterity = 10, constitution = 10, wisdom = 10, intelligence = 10, charisma = 10, player_level = 1, base_hp = 5):
        self.name = name
        self.alignment = align
        self.base_hp = base_hp
        self.armor_class = 10
        self.xp = 0
        self.player_level = player_level
        self.strength = strength        
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.armor_class += set_modifier(dexterity)
        self.max_HP = (base_hp + set_modifier(constitution)) * player_level
        self.current_HP = (5 + set_modifier(constitution)) * player_level
        self.str_mod = set_modifier(strength)
        self.dex_mod = set_modifier(dexterity)
        self.const_mod = set_modifier(constitution)
        self.death = False

    def current_condition(self):
        if self.current_HP <= 0:
            self.death = True

    def level_check(self):
        self.max_HP = self.baseHP + (self.player_level * 5) + (self.player_level * self.const_mod)






