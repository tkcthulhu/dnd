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

class Character:
    def __init__(self, name, align):
        self.name = name
        self.alignment = align
        self.armor = 10
        self.hit = 5


