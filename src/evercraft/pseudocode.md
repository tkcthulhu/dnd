#create an object class
#needs to take parameters/attributes for:
#   Name
#   [X] can we create a character
#   [x] can we name the character
#   Alignment
#   [] does the character have alignment
#   [] can you change
#   [] Armor Class
#   [] Hit points
#   [] can attack(method?)
#       pass in (roll, enemy)
#   [] attack can change
#   damage another character
#   [] can we prove damage was given
#       IF attack is successful
#           do damage
#       ELSE
#           no damage
#   [] can we define the damage (1 for regular, 2 for critical)
#   abilities scores applied
#   [] character has the 6 abilities
#   MODIFIER
#   [] create a dynamic modifier based on level
#   modifier(level) -> if level == 1 -> modifer == -5 ect
#   [] strength will change roll and damage delt
#   [] Dexterity will change armor
#   [] Constitution will change the hp
# Character xp
#   [] Character has xp
#   [] character can gain 10 xp with each hit
#   [] character will level up once xp >= 1000
#   [] each level will increase the constitution modifier by 5
#   [] 1 added to attack roll for each level

# Character Current Condition
-   current HP
-   status (poisoned, burned ect)
-   equipment
-   armor



# Barbarian
- HP is higher + 7 to base (12 start)
- Every level hp increases by 7 + const mod
- add two damage to each crit
- on level up barb gains 2 strength
- add one to roll modifier each 2 levels

# Wizard
- Starts with 6 hp
- hp goes up by four by level
- crit modifier is and roll modifier is affected by intelligence 
- wizards start with intelligence 13
- on level up wizard gains 2 intelligence 

# Fighter
- starts with 10 hp
- attacks roll is increased by 1 for every level instead of every other level
- crit modifier is affected by charisma
- roll modifier is affected by dexterity
- starts with 12 dex
- starts with 12 charisma
- dex levels with player level
- gains 10 hit points + const mod per level instead of 5


# Iteration 3

races
    -multiple sets of defualt attributes for different races
        -human
        -orc
        -elf
    - Inside an IF ELSE statement