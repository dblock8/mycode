import random

def pause():
    input("Press any key to continue...")

def infinity(world_choice):
    stones = ["Soul", "Reality", "Mind", "Power", "Space", "Time"]
    random.shuffle(stones)

    if world_choice in ["AsgardianShip", "Knowhere", "Vormir", "Wakanda", "Titan", "Xandar"]: #my need to change
        for stone in stones:
            print("You found", stone, "stone on", world_choice)
            #random function for which world Thanos is on
            # Compare power level with Thanos
            thanos_power = 95
            if character_power > thanos_power:
                print("You defeated Thanos on", world () + "!")
                break
    else:
        print("He beat you to it!")

def character_select():
    avengers = {
        "hulk": 95,
        "thor": 90,
        "blackpanther": 50,
        "ironman": 70
    }

    while True:
        a = input("Choose your Avenger! ").lower()
        if a in avengers:
            character_power = avengers[a]
            print("You have chosen well, my friend. Power level:", character_power)
            break
        else:
            c = input("Do you need help choosing? Yes or No? ")
            if c.lower() == "no":
                print("Please select a valid Avenger.")
            else:
                print("Here are the available Avengers:")
                print(*avengers.keys(), sep="\n")
        pause()

def world():
    b = input("Find the soul stone on one of these worlds: \nAsgardianShip, Knowhere, Vormir, Wakanda, Titan, Xandar ")
    print("Entering warp seed to", b)
    pause()

    for num in range(5, 0, -1):
        print(num)

    print("You have arrived at", b)
    infinity(b)

def main():
    character_select()
    world()
    # Continue with the rest of your code...

# Call the main function
main()

