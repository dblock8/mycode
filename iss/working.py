import random

def character_select():
    with open("hero.txt") as char:
        char_list = char.readlines()
    #return list
    #main() ?
    while True:
        a = input("Choose your Avenger! ").lower()
        best = ["hulk", "thor", "blackpanther", "ironman"]
        if a in best:
            print("You have chosen well, my friend.")
            break
            elif a not in char_list:
            c = input("Do you need help choosing? Yes or No? ")
            if c.lower() == "no":
                print("Please select a valid Avenger.")
            else:
                print("Here are the available Avengers:")
                print(*char_list, sep="\n")
        else:
            print("Please select a valid Avenger.")
def world():
    b = input("Find the soul stone on one of these worlds: \nAsgradianShip, Knowhere, Vormier, Wakanda, Titan, Xandar ")
    print("Entering warp seed to" + b)
   
    for num in range(5, 0, -1):
         print(num)
   
    print("You have arrived to " + b)

#def main ():
#    """runtime function"""


#create stone item
  #randommize world itme is on
character_select()        
world()

