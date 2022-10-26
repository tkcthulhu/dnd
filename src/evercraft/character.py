#create an object class
#needs to take parameters/attributes for:
#   Name
#   [X] can we create a character
#   [x] can we name the character
#   Alignment
#   [x] does the character have alignment
#   [x] can you change
#   [x] Armor Class
#   [x] Hit points
#   [x] can attack(method?)
#       pass in (roll, enemy)
#   [x] attack can change
#   damage another character
#   [x] can we prove damage was given
#       IF attack is successful
#           do damage
#       ELSE
#           no damage
#   [x] can we define the damage (1 for regular, 2 for critical)
#   abilities scores applied
#   [X] character has the 6 abilities
#   MODIFIER
#   [x] create a dynamic modifier based on level
#   modifier(level) -> if level == 1 -> modifer == -5 ect
#   [] strength will change roll and damage delt
#   [] Dexterity will change armor
#   [] Constitution will change the hp
# Character xp
#   [] Character has xp
#   [] character can gain 10 xp with each hit

class Test:
    def __init__(self, name, align, **abilities):
        self.name = name
        self.align = align

        for key in abilities:
            setattr(self, key, abilities[key])



class Character:

    first = ['Chaotic', 'Neutral', 'Lawful']

    second = ['Evil', 'Good', 'Neutral']
    
    def __init__(self, name, align):
        self.name = name
        self.alignment = align
        self.armor = 10
        self.hitpoints = 5

    def stats(self, Str, Dex, Const, Wis, Int, Char):
        self.Strength = Str
        self.str_mod = self.modifier(Str)
        self.Dexterity = Dex
        self.dex_mod = self.modifier(Dex)
        self.armor += self.dex_mod
        self.Constitution = Const
        self.const_mod = self.modifier(Const)
        self.hitpoints += self.const_mod
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
        if level == 20:
            return 5
    
    def attack(self, roll, enemy):
        enemy = enemy
        EAC = enemy.armor
        if roll == 20:
            self.damage('crit', enemy)
            return 'CRIT'
        elif EAC < roll:
            self.damage('hit', enemy)
            return "HIT"
        elif EAC > roll:
            return "MISS"

    def damage(self, hit, enemy):
        if hit == 'crit':
            setattr(enemy, 'hitpoints', enemy.hitpoints - 2 - (self.str_mod * 2))
            return enemy.hitpoints
        if hit == 'hit':
            setattr(enemy, 'hitpoints', enemy.hitpoints - 1)
            return enemy.hitpoints




