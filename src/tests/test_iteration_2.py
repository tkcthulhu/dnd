from evercraft.character import *
from evercraft.test_class import *

def test_class_barbarian():
    assert Barbarian('Dave', 'Mad Decent')

def test_class_adds_hp():
    Dave = Barbarian('Dave', 'Mad Decent')
    assert Dave.base_hp == 12
    assert Dave.strength.level == 10

def test_class_adds_hp2():
    Dave = Barbarian('Dave', 'Mad Decent')
    assert Dave.base_hp == 12
    assert Dave.max_hp == 12
    assert Dave.current_hp == 12

def test_barb_attack():
    Dave = Barbarian('Dave', 'Mad Decent')
    Morgan = Character('Morgan', 'Meh')
    Combat.attack(Dave, 20, Morgan)
    assert Morgan.current_hp == 1

def test_level_up_hp():
    Dave = Barbarian('Dave', 'Mad Decent', player_level = 2)
    assert Dave.max_hp == 19

def test_leveled_hp_with_modifier():
    Dave = Barbarian('Dave', 'Mad Decent', player_level = 2, constitution=15)
    assert Dave.max_hp == 23

