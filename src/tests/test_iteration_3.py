from evercraft.character import *
from evercraft.test_class import *

def test_race_applies():
    Morgan = Character('Morgan the human', 'Hotdog is not a sandwich')
    assert Morgan.strength.level == 10

def test_orc_attributes():
    Keith = Character("Keith the Kata Orc", "Hotdog is a sandwich", race = 'Orc')
    assert Keith.strength.level == 12
    assert Keith.wisdom.level == 9
    assert Keith.intelligence.level == 9
    assert Keith.charisma.level == 9
    assert Keith.armor_class == 12

def test_elf_attributes():
    Jude = Character("Spacebun the bunny elf", "Catdog", race = 'Elf')
    assert Jude.dexterity.level == 11
    assert Jude.constitution.level == 9
    assert Jude.charisma.level == 11

def test_violence_against_elfs():    
    Keith = Character("Keith the Kata Orc", "Hotdog is a sandwich", race = 'Orc')
    Jude = Character("Spacebun the bunny elf", "Catdog", race = 'Elf')
    Combat.attack(Keith, 11, Jude)
    assert Keith.strength.modifier == 1
    assert Jude.current_hp == 4

def test_dwarf_attributes():
    Mason = Character('Mason', 'The Bellowing Dwarf', race = 'Dwarf')
    assert Mason.constitution.level == 11
    assert Mason.charisma.level == 9

def test_dwarf_leveled_hp():
    Mason = Character('Mason', 'The Bellowing Dwarf', race = 'Dwarf', constitution = 12, player_level = 2) 
    assert Mason.max_hp == 13

def test_dwarf_attack_orc():
    Mason = Character('Mason', 'The Bellowing Dwarf', race = 'Dwarf') 
    Keith = Character("Keith the Kata Orc", "Hotdog is a sandwich", race = 'Orc')
    assert Combat.attack(Mason, 11, Keith) == 'HIT'

def test_dwarf_attack_orcs_hp():
    Mason = Character('Mason', 'The Bellowing Dwarf', race = 'Dwarf') 
    Keith = Character("Keith the Kata Orc", "Hotdog is a sandwich", race = 'Orc')
    Combat.attack(Mason, 11, Keith)
    assert Keith.current_hp == 2

def test_dwarf_attack_elf_hp():
    Mason = Character('Mason', 'The Bellowing Dwarf', race = 'Dwarf') 
    Jude = Character("Spacebun the bunny elf", "Catdog", race = 'Elf')
    Combat.attack(Mason, 11, Jude)
    assert Jude.current_hp == 3

def test_bellowing_dwarf_barbarian():
    Mason = Barbarian('Mason', 'The Bellowing Barbarian Dwarf', race = 'Dwarf', player_level = 15)
    Keith = Character("Keith the Kata Orc", "Hotdog is a sandwich", race = 'Orc')
    Combat.attack(Mason, 20, Keith)
    assert Keith.current_hp == -31
    assert Keith.death == True


