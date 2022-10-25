from evercraft.character import Character

def test_character_exists():
    assert Character('Doug')

def test_character_name():
    Character1 = Character('Bill')
    assert Character1.name == 'Bill'

def test_character_alignment():
    Character1 = Character('Charles', 'Chaotic-Neutral')
    assert Character1.alignment == 'Chaotic-Neutral'

def test_armor_hit():
    Character1 = Character('Chuck', 'Lawful')
    assert Character1.armor == 10
    
def test_character_hit():
    Character1 = Character('Cuck', 'Lawful')
    assert Character1.hit == 5