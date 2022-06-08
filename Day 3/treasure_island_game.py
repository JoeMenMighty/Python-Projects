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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("welcome to Mighty Man's Treasure Island. \nYour mission is to find the treasure.")

way = (input("Which way do you want to go? 'left' or 'right'\n")).lower()
if way == "left":
  stay_status = (input("You are at the lake now. Type 'wait' to wait for the boat or 'swim' to swim across the lake.\n")).lower()
  if stay_status == "wait":
    door_choice = (input("You arrive at the island unharmed.\nThere's a house with three doors, 'red', 'yellow' and 'blue'. \nWhich door will you enter?\n")).lower()
    if door_choice == "yellow":
      print("Congratulations !!!!!!!!!.............\nYou found the Treasure \nGobe for you !!!!!!")
    elif door_choice == "blue":
      print("Aoooooo, You opened the room with beasts. You die!!!\n Game over!!!")
    elif door_choice == "red":
      print("Chechekule, You opened the door with fire. You die!!!\n Game over!!!")
    else:
      print("Game Over. SagaaaaaaWele")
  else:
    print("Isssshhhh, you were attacked by a crocrodile\n Game over!!!")
else:
  print("Oops, you fell into a hole\n Game over!!!.")
