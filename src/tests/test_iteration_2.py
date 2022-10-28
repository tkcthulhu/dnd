from evercraft.character import *
from evercraft.test_class import *

def test_class_barbarian():
    assert Barbarian('Dave', 'Mad Decent')

def test_class_adds_hp():
    Dave = Barbarian('Dave', 'Mad Decent')
    assert Dave.base_hp == 12
    assert Dave.strength.level == 12

def test_class_adds_hp2():
    Dave = Barbarian('Dave', 'Mad Decent')
    assert Dave.base_hp == 12
    assert Dave.max_hp == 13
    assert Dave.current_hp == 13

def test_barb_attack():
    Dave = Barbarian('Dave', 'Mad Decent')
    Morgan = Character('Morgan', 'Meh')
    Combat.attack(Dave, 20, Morgan)
    assert Morgan.current_hp == -1

def test_level_up_hp():
    Dave = Barbarian('Dave', 'Mad Decent', player_level = 2)
    assert Dave.max_hp == 23

def test_leveled_hp_with_modifier():
    Dave = Barbarian('Dave', 'Mad Decent', player_level = 2)
    assert Dave.strength.modifier == 2
    assert Dave.max_hp == 23

def test_leveled_up_strength():
    Dave = Barbarian('Dave', 'Mad Decent', player_level = 4)
    assert Dave.strength.level == 18

def test_leveled_up_modifier():
    Dave = Barbarian('Dave', 'Mad Decent', player_level = 4)
    assert Dave.strength.level == 18
    assert Dave.strength.modifier == 4

def test_barb_roll_scale():
    Dave = Barbarian('Dave', 'Mad Decent', player_level = 2)
    assert Dave.strength.level == 14
    assert Dave.strength.modifier == 2
    assert Dave.roll_modifier == 3

def test_barb_scale_level_5():
    Dave = Barbarian('Dave', 'Mad Decent', player_level = 5)
    assert Dave.strength.level == 20
    assert Dave.strength.modifier == 5
    assert Dave.roll_modifier == 7
    assert Dave.max_hp == 65

def test_class_wizard():
    assert Wizard('Willie', 'Shy-Evil')

def test_class_wizard_is_smart():
    Willie = Wizard('Willie', 'Shy-Evil')
    assert Willie.intelligence.level == 12
    assert Willie.wisdom.level == 12
    assert Willie.intelligence.modifier == 1

def test_class_wizard_roll_up():
    Willie = Wizard('Willie', 'Shy-Evil')
    assert Willie.roll_modifier == 1

def test_class_wizard_int_scales_crit():
    Willie = Wizard('Willie', 'Shy-Evil')
    assert Willie.crit_modifier == 2

def test_class_wizard():
    Willie = Wizard('Willie', 'Shy-Evil', player_level=4)
    assert Willie.intelligence.level == 18
    assert Willie.intelligence.modifier == 4

def test_class_wizard_roll_scale():
    Willie = Wizard('Willie', 'Shy-Evil', player_level=2)
    assert Willie.intelligence.level == 14
    assert Willie.intelligence.modifier == 2
    assert Willie.roll_modifier == 3

def test_class_wizard_roll_scale_level_4():
    Willie = Wizard('Willie', 'Shy-Evil', player_level=4)
    assert Willie.intelligence.level == 18
    assert Willie.intelligence.modifier == 4
    assert Willie.roll_modifier == 6
    
def test_class_fighter():
    assert Fighter('Jackie', 'Chan')

def test_class_fighter_starting_stats():
    Jackie = Fighter('Jackie', 'Chan')
    assert Jackie.dexterity.level ==12
    assert Jackie.charisma.level ==12
    assert Jackie.base_hp == 10

def test_class_fighter_level_up_stats():
    Jackie = Fighter('Jackie', 'Chan', player_level=2)
    assert Jackie.charisma.level == 14
    assert Jackie.dexterity.level== 14
    assert Jackie.max_hp == 20

def test_class_fighter_charisma_modifiers():
    Jackie = Fighter('Jackie', 'Chan')
    assert Jackie.crit_modifier == 2

def test_class_fighter_dexterity_modifiers():
    Jackie = Fighter('Jackie', 'Chan')
    assert Jackie.roll_modifier == 1

def test_class_fighter_roll_scale():
    Jackie = Fighter('Jackie', 'Chan', player_level=2)
    assert Jackie.dexterity.level == 14
    assert Jackie.dexterity.modifier == 2
    assert Jackie.roll_modifier == 3

def test_class_fighter_roll_scale_level3():
    Jackie = Fighter('Jackie', 'Chan', player_level=3)
    assert Jackie.dexterity.level == 16
    assert Jackie.dexterity.modifier == 3
    assert Jackie.roll_modifier == 5

def test_classes_fight():
    Jackie = Fighter('Jackie', 'Chan')
    Willie = Wizard('Willie', 'Shy-Evil')
    Combat.attack(Jackie, 20, Willie)
    Combat.attack(Willie, 20, Jackie)
    assert Jackie.current_hp == 6
    assert Willie.current_hp == 2
