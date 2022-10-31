from evercraft.character import *
from evercraft.test_class import *

def test_character_has_weapon():
    Morgan = Character('Morgon', 'Mod Decent', 0)
    assert Morgan.weapon == 'Fists'

def test_weapon_damage_modifier():
    Morgan = Character('Morgon', 'Mod Decent', 1)
    Keith = Character('Keith', 'Hotdog is a Sandwich', 0)

    Combat.attack(Morgan, 15, Keith)

    assert Keith.current_hp == 3

def test_weapon_greataxe_barbarian():
    Tyler = Barbarian('Tyler', 'Violence for Barbarians', weapon = 3)
    assert Tyler.weapon == 'Great Axe'
    assert Tyler.class_type == 'Barbarian'

def test_great_axe_barbarian(): 
    Tyler = Barbarian('Tyler', 'Violence for Barbarians', weapon = 3, player_level = 3)
    Keith = Character('Keith', 'Hotdog is a Sandwich', 0)
    Combat.attack(Tyler, 15, Keith)
    assert Keith.current_hp == -2

def test_great_axe_barbarian(): 
    Tyler = Barbarian('Tyler', 'Violence for Barbarians', weapon = 3)
    Keith = Character('Keith', 'Hotdog is a Sandwich', weapon = 3)
    Combat.attack(Keith, 15, Tyler)
    assert Tyler.current_hp == 11

def test_how_hard_does_orc_barbarian_hit():
    Morgan = Barbarian('Morgan', 'Hotdog is a Taco', weapon=3, race='Orc', player_level=15)
    Keith = Character('Keith', 'Hotdog is a Sandwich')
    Combat.attack(Morgan, 20, Keith)
    assert Keith.current_hp == -47