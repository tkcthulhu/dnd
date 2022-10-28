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
        race_mod_attack = 0
        race_mod_defense = 0

        if attacker.race == 'Orc':
            if enemy.race == 'Elf':
                race_mod_defense += 2

        if attacker.race == 'Dwarf':
            if enemy.race == 'Orc':
                race_mod_attack += 2

        if roll == 20:
            Combat.damage(attacker, 'crit', enemy)
            attacker.xp += 10
            attacker.player_level = math.floor((attacker.xp/1000)+1)
            return 'CRIT'
        elif EAC + race_mod_defense < roll + attacker.roll_modifier + (attacker.player_level // 2) + race_mod_attack:
            Combat.damage(attacker, 'hit', enemy)
            attacker.xp += 10
            attacker.player_level = math.floor((attacker.xp/1000)+1)
            return "HIT"
        elif EAC + race_mod_defense >= roll + attacker.roll_modifier + (attacker.player_level // 2) + race_mod_attack:
            enemy.xp += 10 
            return "MISS"    

    def damage(attacker, hit, enemy):
        enemy.current_condition()
        race_mod_attack = 0
        race_mod_defense = 0

        if attacker.race == 'Dwarf':
            if enemy.race == 'Orc':
                race_mod_attack += 2
        
        if hit == 'crit':
            setattr(enemy, 'current_hp', enemy.current_hp - 2 - (attacker.crit_modifier) - race_mod_attack)
            enemy.current_condition()
            return enemy.current_hp
        if hit == 'hit':
            setattr(enemy, 'current_hp', enemy.current_hp - 1 - (attacker.strength.modifier) - race_mod_attack)
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
    ORC_ATTRIBUTES = {
        'strength' : 12, 
        'dexterity' : 10, 
        'constitution' : 10, 
        'wisdom' : 9, 
        'intelligence' : 9, 
        'charisma' : 9,
    }
    ELF_ATTRIBUTES = {
        'strength' : 10, 
        'dexterity' : 11, 
        'constitution' : 9, 
        'wisdom' : 10, 
        'intelligence' : 10, 
        'charisma' : 11,
    }
    DWARF_ATTRIBUTES = {
        'strength' : 10, 
        'dexterity' : 10, 
        'constitution' : 11, 
        'wisdom' : 10, 
        'intelligence' : 10, 
        'charisma' : 9,
    }
    
    def __init__(self, name, align, race = 'Human', player_level = 1, base_hp = 5, hp_gain = 5, **abilities):
        self.name = name
        self.alignment = align
        self.base_hp = base_hp
        self.armor_class = 10
        self.xp = 0
        self.player_level = player_level
        self.race = race
        
        if self.race == 'Human':
            for key in self.DEFAULT_ATTRIBUTES:
                level = abilities[key] if (key in abilities) else self.DEFAULT_ATTRIBUTES[key]
                mod = Stats(key, level, Stats.set_modifier(level))
                setattr(self, key, mod)
        elif self.race == "Orc":
            self.armor_class += 2
            for key in self.ORC_ATTRIBUTES:
                level = abilities[key] if (key in abilities) else self.ORC_ATTRIBUTES[key]
                mod = Stats(key, level, Stats.set_modifier(level))
                setattr(self, key, mod)
        elif self.race == 'Elf':
            for key in self.ELF_ATTRIBUTES:
                level = abilities[key] if (key in abilities) else self.ELF_ATTRIBUTES[key]
                mod = Stats(key, level, Stats.set_modifier(level))
                setattr(self, key, mod)
        elif self.race == 'Dwarf':
            for key in self.DWARF_ATTRIBUTES:
                level = abilities[key] if (key in abilities) else self.DWARF_ATTRIBUTES[key]
                mod = Stats(key, level, Stats.set_modifier(level))
                setattr(self, key, mod)        

        self.armor_class += self.dexterity.modifier

        self.hp_gain = hp_gain

        self.max_hp = ((base_hp + self.constitution.modifier) + ((self.player_level - 1) * (self.hp_gain + self.constitution.modifier)))
        
        if self.race == 'Dwarf':
            self.max_hp = ((base_hp + self.constitution.modifier) + ((self.player_level - 1) * (self.hp_gain + (self.constitution.modifier * 2))))

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
        super().__init__(name, align, base_hp = 12, hp_gain = 7, **abilities)
        self.strength.level += ((self.player_level - 1) * 2) + 2
        self.strength.modifier = Stats.set_modifier(self.strength.level)
        self.constitution.level += ((self.player_level - 1) * 2) + 2
        self.constitution.modifier = Stats.set_modifier(self.constitution.level)
        self.max_hp = ((self.base_hp + self.constitution.modifier) + ((self.player_level - 1) * (self.hp_gain + self.constitution.modifier)))
        self.current_hp = self.max_hp
        self.roll_modifier = self.strength.modifier + (self.player_level // 2)
        self.crit_modifier = (self.strength.modifier * 2) + 2

class Wizard(Character):
     def __init__(self, name, align, **abilities):
        super().__init__(name, align, base_hp = 6, hp_gain = 4, **abilities)
        self.intelligence.level += ((self.player_level - 1) * 2) + 2
        self.intelligence.modifier = Stats.set_modifier(self.intelligence.level)
        self.wisdom.level += ((self.player_level - 1) * 2) + 2
        self.wisdom.modifier = Stats.set_modifier(self.wisdom.level)
        self.roll_modifier = self.intelligence.modifier + (self.player_level // 2)
        self.crit_modifier = (self.intelligence.modifier * 2)
    
class Fighter(Character):
    def __init__(self, name, align, **abilities):
        super().__init__(name, align, base_hp = 10, hp_gain = 10, **abilities)
        self.dexterity.level += ((self.player_level - 1) * 2) + 2
        self.dexterity.modifier = Stats.set_modifier(self.dexterity.level)
        self.charisma.level += ((self.player_level - 1) * 2) + 2
        self.charisma.modifier = Stats.set_modifier(self.charisma.level)
        self.roll_modifier = self.dexterity.modifier + (self.player_level - 1)
        self.crit_modifier = (self.charisma.modifier * 2)


   







