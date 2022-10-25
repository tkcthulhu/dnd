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
#   [] create a dynamic modifier based on level
#   modifier(level) -> if level == 1 -> modifer == -5 ect



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
        self.Dexterity = Dex
        self.Constitution = Const
        self.Wisdom = Wis
        self.Intelligence = Int
        self.Charisma = Char   

    def modifier(self, level):
        if level == 1:
            return -5
        if level == 2 or 3:
            return -4
        if level == 4 or 5:
            return -3
        if level == 6 or 7:
            return -2
        if level == 8 or 9:
            return -1
        if level == 10 or 11:
            return 0
        if level == 12 or 13:
            return 1
        if level == 14 or 15:
            return 2
        if level == 16 or 17:
            return 3
        if level == 18 or 19:
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
            setattr(enemy, 'hitpoints', enemy.hitpoints - 2)
            return enemy.hitpoints
        if hit == 'hit':
            setattr(enemy, 'hitpoints', enemy.hitpoints - 1)
            return enemy.hitpoints




