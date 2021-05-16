print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.") 

this_way = input("You're at a cross road. Do you want to go left or right?\n")
this_way_lower = this_way.lower()

if this_way_lower != "left":
  print("A rabid dog bites you and you die of rabies.\nGame over!")
else:
  lake = input("You come to a lake. In the middle of the lake there's an island. Do you want to swim or wait?\n")
  lake_lower = lake.lower()

  if lake_lower != "wait":
    print("While swimming across the lake you encounter the monster of Loch Ness. Nessie fancies you and takes you back to her home in the depths of the lake. You drown as a result.\nGame over!")
  else:
    room = input("You arrive at the island unharmed. There's a house with three doors. One yellow, one red, one blue. Which do you choose?\n")
    room_lower = room.lower()

    if room_lower == "red":
      print("You open the red door and walk inside. The door closes behind you with a slam and then disappears. You look around and see you've arrived at the fiery pits of hell.\nGame over!")
    elif room_lower == "blue":
      print("You walk through the blue door and find yourself in the middle of the ocean. With no land in sight, you drown.\nGame over!")
    elif room_lower == "yellow":
      print("You open the yellow door and find the treasure chest inside. You open the chest and are blinded by the gold inside of it.\nYou win!")
    else:
      print("Unable to make a choice you go back home and return to your normal life.\nGame over.")



#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
