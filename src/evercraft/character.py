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
#   [] character has the 6 abilities
#   []

class Character:
    def __init__(self, name, align):
        self.name = name
        self.alignment = align
        self.armor = 10
        self.hitpoints = 5        
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




