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
        elif EAC < roll + attacker.roll_modifier + (attacker.player_level // 2):
            Combat.damage(attacker, 'hit', enemy)
            attacker.xp += 10
            attacker.player_level = math.floor((attacker.xp/1000)+1)
            return "HIT"
        elif EAC >= roll + attacker.roll_modifier + (attacker.player_level // 2):
            return "MISS"    

    def damage(attacker, hit, enemy):
        enemy.current_condition()
        if hit == 'crit':
            setattr(enemy, 'current_hp', enemy.current_hp - 2 - (attacker.crit_modifier))
            enemy.current_condition()
            return enemy.current_hp
        if hit == 'hit':
            setattr(enemy, 'current_hp', enemy.current_hp - 1 - (attacker.strength.modifier))
            enemy.current_condition()
            return enemy.current_hp

class Character:

    DEFAULT_ATTRIBUTES = {
        'strength' : 10, 
        'dexterity' : 10, 
        'constitution' : 10, 
        'wisdom' : 10, 
        'intelligence' : 10, 
        'charisma' : 10,
    }
    
    def __init__(self, name, align, player_level = 1, base_hp = 5, hp_gain = 5, **abilities):
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

        self.hp_gain = hp_gain

        self.max_hp = ((base_hp + self.constitution.modifier) + ((self.player_level - 1) * (self.hp_gain + self.constitution.modifier)))

        if self.max_hp <= 0:
            self.max_hp = 1

        self.roll_modifier = self.strength.modifier
        
        self.crit_modifier = self.strength.modifier * 2

        self.current_hp = self.max_hp

        self.death = False

    def current_condition(self):
        if self.current_hp <= 0:
            self.death = True

class Barbarian(Character):
    def __init__(self, name, align, **abilities):
        super().__init__(name, align, base_hp = 12, hp_gain = 7, strength = 12, constitution = 12,  **abilities)
        self.crit_modifier = (self.strength.modifier * 2) + 2
        self.strength.level += ((self.player_level - 1) * 2)
        self.strength.modifier = Stats.set_modifier(self.strength.level)
        self.constitution.level += ((self.player_level - 1) * 2)
        self.constitution.modifier = Stats.set_modifier(self.constitution.level)
        self.roll_modifier = self.strength.modifier + (self.player_level // 2)
class Wizard(Character):
     def __init__(self, name, align, **abilities):
        super().__init__(name, align, base_hp = 6, hp_gain = 4, intelligence=12, wisdom=12, **abilities)
        self.intelligence.level += ((self.player_level - 1) * 2)
        self.intelligence.modifier = Stats.set_modifier(self.intelligence.level)
        self.wisdom.level += ((self.player_level - 1) * 2)
        self.wisdom.modifier = Stats.set_modifier(self.wisdom.level)
        self.roll_modifier = self.intelligence.modifier + (self.player_level // 2)
        self.crit_modifier = (self.intelligence.modifier * 2)
    
class Fighter(Character):
    def __init__(self, name, align, **abilities):
        super().__init__(name, align, base_hp = 10, hp_gain = 10, dexterity=12, charisma=12, **abilities)
        self.dexterity.level += ((self.player_level - 1) * 2)
        self.dexterity.modifier = Stats.set_modifier(self.dexterity.level)
        self.charisma.level += ((self.player_level - 1) * 2)
        self.charisma.modifier = Stats.set_modifier(self.charisma.level)
        self.crit_modifier = (self.charisma.modifier * 2)
        self.roll_modifier = self.dexterity.modifier + (self.player_level - 1)


   







