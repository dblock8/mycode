import random

def infinity(world_choice):
    stones = ["Soul"]
    random.shuffle(stones)

    if world_choice in ["AsgardianShip", "Knowhere", "Vormir", "Wakanda", "Titan", "Xandar"]:
        for stone in stones:
            print("You found", stone + "stone", "on", world_choice)
    else:
        print("He beat you to it!")
def character_select():
    avengers = {
        "hulk": 50,
        "thor": 80,
        "blackpanther": 70,
        "ironman": 90
    }

    while True:
        a = input("Choose your Avenger! ").lower()
        if a in avengers:
            print("You have chosen well, my friend. Power level:", avengers[a])
            break
        else:
            c = input("Do you need help choosing? Yes or No? ")
            if c.lower() == "no":
                print("Please select a valid Avenger.")
            else:
                print("Here are the available Avengers:")
                print(*avengers.keys(), sep="\n")
    # Rest of the code...

#def character_select():
  #  with open("hero.txt") as char:
   #     char_list = char.readlines()
        
   # while True:
    #    a = input("Choose your Avenger! ").lower()
     #   best = ["hulk", "thor", "blackpanther", "ironman"]
      #  if a in best:
       #     print("You have chosen well, my friend.")
        #    break
       # elif a not in char:
        #    c = input("Do you need help choosing? Yes or No? ")
          #  if c.lower() == "no":
         #       print("Please select a valid Avenger.")
        #    else:
       #         print("Here are the available Avengers:")
      #          print(*char_list, sep="\n")
     #   else:
    #        print("Please select a valid Avenger.")

def world():
    b = input("Find the soul stone on one of these worlds: \nAsgardianShip, Knowhere, Vormir, Wakanda, Titan, Xandar ")
    print("Entering warp seed to", b)

    for num in range(5, 0, -1):
        print(num)

    print("You have arrived at", b)
    infinity(b)

character_select()
world()

