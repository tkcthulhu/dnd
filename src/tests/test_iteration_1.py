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
    assert Character1.base_hp == 5

def test_character_attack():
    Character1 = Character('Cuck', 'Lawful')
    Character2 = Character('Keith', 'Lawful-Evil')    
    assert Combat.attack(Character1, 5, Character2) == 'MISS'

def test_character_hit_EAC():
    Character1 = Character('Cuck', 'Lawful')
    Character2 = Character('Keith', 'Lawful-Evil')
    assert Combat.attack(Character1, 15, Character2) == "HIT"

def test_character_nat_20():
    Character1 = Character('Skisgaar', 'Chaotic-good')
    Character2 = Character('Keith', 'Lawful-Evil')
    assert Combat.attack(Character1, 20, Character2) == "CRIT"

def test_character_damaged():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    Character2 = Character('Keith', 'Lawful-Evil')
    Combat.attack(Character1, 20, Character2)
    assert Character2.current_HP == 3

def test_character_stats_present():
    Character2 = Character('Keith', 'Lawful-Evil')
    assert Character2.strength == 10

def test_character_modifier():
    Character1 = Character('SpaceBun', 'Chaotic-goood', strength = 17)
    Str = Character1.strength
    assert Str == 17
    assert Character1.str_mod == 3

def test_const_modifier():
    Character1 = Character('SpaceBun', 'Chaotic-goood')
    assert Character1.const_mod == 0


def test_dex_modifier():
    Character1 = Character('SpaceBun', 'Chaotic-goood', dexterity=17)
    assert Character1.dex_mod == 3
    assert Character1.armor_class == 13

def test_str_mod():
    Character1 = Character('SpaceBun', 'Chaotic-goood', strength=15)
    Character2 = Character('Keith', 'Lawful-Evil')
    Combat.attack(Character1, 20, Character2)
    assert Character2.current_HP == -1

def test_character_hit():
    Character1 = Character('SpaceBun', 'Chaotic-goood', strength=15)
    # str mod +2
    Character2 = Character('Keith', 'Lawful-Evil', dexterity=7)
    # dex mod -2
    Combat.attack(Character1, 9, Character2)

    assert Character2.current_HP == 2

def test_str_mod_roll():

    Character1 = Character('Morgan', 'Chaotic-good-ish', strength=15)
    # str mod = +2 dc=12
    Character2 = Character('Keith', 'Lawful-Evil')
    # ac mod = +10 ac=10
    assert Combat.attack(Character1, 10, Character2) == 'HIT'

def test_str_mod_roll2():

    Character1 = Character('Morgan', 'Chaotic-good-ish', dexterity=15)
    # ac mod = +2 ac=12
    Character2 = Character('Keith', 'Lawful-Evil', strength=1)
    # str mod = -5 dc
    assert Combat.attack(Character2, 15, Character1) == 'MISS'

def test_character_has_xp():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    assert Character1.xp == 0


def test_charcater_gain_xp():
    Character1 = Character('Morgan', 'Chaotic-good-ish', strength=15)
    # str mod = +2 dc=12
    Character2 = Character('Keith', 'Lawful-Evil')
    # ac mod = +0 ac=10
    Combat.attack(Character1, 10, Character2)
    assert Character1.xp == 10

def test_charcater_gain_xp_two_times():
    Character1 = Character('Morgan', 'Chaotic-good-ish', strength=15)
    # str mod = +2 dc=12
    Character2 = Character('Keith', 'Lawful-Evil')
    # ac mod = +0 ac=10
    Character1.xp = 980

    Combat.attack(Character1, 10, Character2)
    Combat.attack(Character1, 20, Character2)

    assert Character1.xp == 1000

def test_character_has_level():
    Character1 = Character('Morgan', 'Chaotic-good-ish')
    assert Character1.player_level

def test_character_can_level_up():
    Character1 = Character('Morgan', 'Chaotic-good-ish', strength=15)

    Character2 = Character('Keith', 'Lawful-Evil')

    Character1.xp = 990

    Combat.attack(Character1, 20, Character2)

    assert Character1.xp == 1000
    assert Character1.player_level == 2

def test_character_can_level_up2():
    Character1 = Character('Morgan', 'Chaotic-good-ish', strength=15)


    Character2 = Character('Keith', 'Lawful-Evil')


    Character1.xp = 1990

    Combat.attack(Character1, 20, Character2)

    assert Character1.xp == 2000
    assert Character1.player_level == 3

def test_character_level_scales():
    Character1 = Character('Morgan', 'Chaotic-good-ish', constitution=15, player_level=2)
    assert Character1.max_HP == 14

def test_new_dex():
    Character1 = Character('Dumb', 'align')
    Character1.dexterity = 20
    assert Character1.strength == 10
    assert Character1.dexterity == 20

def test_character_death():
    Character2 = Character('Keith', 'Lawful-Evil')
    Character2.current_HP = 0
    Character2.current_condition()
    assert Character2.death == True

def test_morgan_vs_keith():
    Morgan = Character('Morgan', 'Chaotic-Good', strength=30)
    Keith = Character('Keith', 'Lawful-Evil')

    Combat.attack(Morgan, 20, Keith)

    assert Keith.death == True

def test_ability_loop():
    T = Test('T', 'Q')
    assert T.strength == 10

def test_overwrite_loop():
    T = Test('T', 'Q', strength = 15)
    assert T.strength == 15