from evercraft.character import Character

def test_character_exists():
    assert Character('Doug', 'Lawful-Evil')

def test_character_name():
    Character1 = Character('Bill', 'Lawful-Evil')
    assert Character1.name == 'Bill'

def test_character_alignment():
    Character1 = Character('Charles', 'Chaotic-Neutral')
    assert Character1.alignment == 'Chaotic-Neutral'

def test_armor_hit():
    Character1 = Character('Chuck', 'Lawful')
    assert Character1.armor == 10
    
def test_character_hitpoints():
    Character1 = Character('Cuck', 'Lawful')
    assert Character1.hitpoints == 5

def test_character_attack():
    Character1 = Character('Cuck', 'Lawful')
    Character2 = Character('Keith', 'Lawful-Evil')    
    assert Character1.attack(5, Character2) == 'MISS'

def test_character_hit():
    Character1 = Character('Cuck', 'Lawful')
    Character2 = Character('Keith', 'Lawful-Evil')
    assert Character1.attack(20, Character2) == 'CRIT'

def test_character_hit_EAC():
    Character1 = Character('Cuck', 'Lawful')
    Character2 = Character('Keith', 'Lawful-Evil')
    assert Character1.attack(4, Character2) == False

def test_character_hit_EAC():
    Character1 = Character('Cuck', 'Lawful')
    Character2 = Character('Keith', 'Lawful-Evil')
    assert Character1.attack(15, Character2) == "HIT"
    assert Character2.hitpoints == 4

def test_character_nat_20():
    Character1 = Character('Skisgaar', 'Chaotic-good')
    Character2 = Character('Keith', 'Lawful-Evil')
    assert Character1.attack(20, Character2) == "CRIT"

def test_character_damaged():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    Character2 = Character('Keith', 'Lawful-Evil')
    Character1.attack(20, Character2)
    assert Character2.hitpoints == 3

    