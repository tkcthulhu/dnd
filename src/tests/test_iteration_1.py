from evercraft.character import *

def test_test_class():
    t = Test('Josh', 'Evil', strength=10, dex=20)
    assert t.strength == 10

def test_character_exists():
    assert Character('Doug', 'Lawful-Evil')

def test_character_name():
    Character1 = Character('Bill', 'Lawful-Evil')
    assert Character1.name == 'Bill'

def test_character_alignment():
    Character1 = Character('Charles', 'Chaotic-Neutral')
    assert Character1.alignment == 'Chaotic-Neutral'

def test_armor_class_hit():
    Character1 = Character('Chuck', 'Lawful')
    assert Character1.armor_class == 10
    
def test_character_hit_points():
    Character1 = Character('Cuck', 'Lawful')
    assert Character1.baseHP == 5

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
    assert Character2.hit_points == 4

def test_character_nat_20():
    Character1 = Character('Skisgaar', 'Chaotic-good')
    Character2 = Character('Keith', 'Lawful-Evil')
    assert Character1.attack(20, Character2) == "CRIT"

def test_character_damaged():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    Character2 = Character('Keith', 'Lawful-Evil')
    Character1.attack(20, Character2)
    assert Character2.hit_points == 3

def test_character_stats_present():
    Character2 = Character('Keith', 'Lawful-Evil')
    Character2.stats(1, 2, 3, 4, 5, 6)
    assert Character2.Strength == 1

def test_character_modifier():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    Character1.stats(17, 15, 15, 15, 15, 15)
    Str = Character1.Strength
    assert Str == 17
    assert Character1.modifier(Str) == 3

def test_const_modifier():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    Character1.stats(17, 15, 15, 15, 15, 15)
    # Const = Character1.Constitution
    assert Character1.const_mod == 2
    assert Character1.hit_points == 7

def test_dex_modifier():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    Character1.stats(17, 1, 15, 15, 15, 15)
    assert Character1.armor_class == 5

def test_str_mod():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    Character2 = Character('Keith', 'Lawful-Evil')
    Character1.stats(15, 1, 15, 15, 15, 15)
    Character2.stats(17, 1, 15, 15, 15, 15)
    Character1.attack(20, Character2)
    assert Character2.hit_points == 1

def test_character_hit():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    Character2 = Character('Keith', 'Lawful-Evil')
    Character1.stats(21, 15, 15, 15, 15, 15)
    Character2.stats(17, 1, 15, 15, 15, 15)
    Character1.attack(15, Character2)
    assert Character2.hit_points == 1

def test_str_mod_roll():

    Character1 = Character('Morgan', 'Chaotic-good-ish')
    Character1.stats(15, 15, 15, 15, 15, 15)
    # str mod = +2 dc=12
    Character2 = Character('Keith', 'Lawful-Evil')
    Character2.stats(17, 10, 15, 15, 15, 15)
    # ac mod = +5 ac=10
    assert Character1.attack(10, Character2) == 'HIT'

def test_str_mod_roll2():

    Character1 = Character('Morgan', 'Chaotic-good-ish')
    Character1.stats(15, 15, 15, 15, 15, 15)
    # ac mod = +2 ac=12
    Character2 = Character('Keith', 'Lawful-Evil')
    Character2.stats(1, 10, 15, 15, 15, 15)
    # str mod = -5 dc
    assert Character2.attack(15, Character1) == 'MISS'

def test_character_has_xp():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    assert Character1.xp == 0


def test_charcater_gain_xp():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    Character1.stats(15, 15, 15, 15, 15, 15)
    # str mod = +2 dc=12
    Character2 = Character('Keith', 'Lawful-Evil')
    Character2.stats(17, 10, 15, 15, 15, 15)
    # ac mod = +5 ac=10
    Character1.attack(10, Character2)
    assert Character1.xp == 10

def test_charcater_gain_xp_two_times():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    Character1.stats(15, 15, 15, 15, 15, 15)
    # str mod = +2 dc=12
    Character2 = Character('Keith', 'Lawful-Evil')
    Character2.stats(17, 10, 15, 15, 15, 15)
    # ac mod = +5 ac=10
    Character1.xp = 980

    Character1.attack(10, Character2)
    Character1.attack(20, Character2)

    assert Character1.xp == 1000

def test_character_has_level():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    assert Character1.level

def test_character_can_level_up():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    Character1.stats(15, 15, 15, 15, 15, 15)

    Character2 = Character('Keith', 'Lawful-Evil')
    Character2.stats(17, 10, 15, 15, 15, 15)

    Character1.xp = 990

    Character1.attack(20, Character2)

    assert Character1.xp == 1000
    assert Character1.player_level == 2

def test_character_can_level_up2():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    Character1.stats(15, 15, 15, 15, 15, 15)

    Character2 = Character('Keith', 'Lawful-Evil')
    Character2.stats(17, 10, 15, 15, 15, 15)

    Character1.xp = 1990

    Character1.attack(20, Character2)

    assert Character1.xp == 2000
    assert Character1.player_level == 3

def test_character_level_scales():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    Character1.stats(15, 15, 15, 15, 15, 15)
    Character1.player_level = 2
    assert Character1.max_HP == 14

def test_defaults():
    Character1 = Character('Morgan', 'CE', Character.DEFAULT_ATTRIBUTES)