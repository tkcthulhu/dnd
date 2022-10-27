from evercraft.character import Stats

class Test:

    DEFAULT_ATTRIBUTES = {
        'strength' : 10, 
        'dexterity' : 10, 
        'constitution' : 10, 
        'wisdom' : 10, 
        'intelligence' : 10, 
        'charisma' : 10,
    }

    def __init__(self, name, align, **abilities):
        self.name = name
        self.align = align

        for key in self.DEFAULT_ATTRIBUTES:
            level = abilities[key] if (key in abilities) else self.DEFAULT_ATTRIBUTES[key]
            mod = Stats(key, level, Stats.set_modifier(level))
            setattr(self, key, mod)

