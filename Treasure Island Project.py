print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. You're at a cross road. Where do you want to go?")
c1 = input('Type "Left" or "Right"?: ').lower()
if c1 == "left":
    c2 = input('You\'ve come to a lake.'
                ' There is an island in the middle of the lake.'
                ' What do you do?'
                ' Type "Swim" or "Wait"?: ').lower()
    if c2 == "wait":
        c3 = input('You arrive at the island unharmed.'
            ' There is a house with 3 doors.'
            ' Which door? Black, Pink, or Green?: ').lower()
        if c3 == "black":
            print("The air in this room is poison. Game over.")
        elif c3 == "pink":
            print("The room is full of hungry wolves. Game Over.")
        elif c3 == "green":
            print ("You found the treasure! You win!")
        else:
            print("Game over.")
    else:
       print("The water is too cold and you succumb to hypothermia. Game over.")
else:
    print("Fall off a cliff. Game over.")
