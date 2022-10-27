import math

class Stats:

    def __init__(self, skill, level, modifier):
        self.skill = skill
        self.level = level
        self.modifier = modifier

    def set_modifier(level):
        return (level - 10) // 2

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
        elif EAC < roll + attacker.strength.modifier + (attacker.player_level // 2):
            Combat.damage(attacker, 'hit', enemy)
            attacker.xp += 10
            attacker.player_level = math.floor((attacker.xp/1000)+1)
            return "HIT"
        elif EAC >= roll + attacker.strength.modifier + (attacker.player_level // 2):
            return "MISS"    

    def damage(attacker, hit, enemy):
        enemy.current_condition()
        if hit == 'crit':
            setattr(enemy, 'current_HP', enemy.current_HP - 2 - (attacker.strength.modifier * 2))
            enemy.current_condition()
            return enemy.current_HP
        if hit == 'hit':
            setattr(enemy, 'current_HP', enemy.current_HP - 1 - (attacker.strength.modifier))
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
    }
    
    def __init__(self, name, align, player_level = 1, base_hp = 5, **abilities):
        self.name = name
        self.alignment = align
        self.base_hp = base_hp
        self.armor_class = 10
        self.xp = 0
        self.player_level = player_level
        
        for key in self.DEFAULT_ATTRIBUTES:
            level = abilities[key] if (key in abilities) else self.DEFAULT_ATTRIBUTES[key]
            mod = Stats(key, level, Stats.set_modifier(level))
            setattr(self, key, mod)

        self.armor_class += self.dexterity.modifier

        self.max_HP = ((base_hp + self.constitution.modifier) * player_level)

        if self.max_HP <= 0:
            self.max_HP = 1
        
        self.current_HP = self.max_HP

        self.death = False

    def current_condition(self):
        if self.current_HP <= 0:
            self.death = True







