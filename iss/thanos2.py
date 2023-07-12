import random

def pause():
    input("Press Enter to continue...")

def infinity(world_choice, character_power): #random shuffle thanos on worlds (random.shuffle worlds() ?
    stones = ["Soul"]
    

    if world_choice in ["AsgardianShip", "Knowhere", "Vormir", "Wakanda", "Titan", "Xandar"]:
        for stone in stones:
            print("You found", stone, "stone on", world_choice)

            
            thanos_present = random.choice([True, False])

            if thanos_present:# is this correct using character powers to determine result
                print("Thanos is here on", world_choice + "!")
                fight_result = fight(character_power)
                if fight_result:
                    print("You defeated Thanos and saved the universe!")
                else:
                    print("You failed, Snap destroyed half the universe.")
                break
        world_choice = Thanos
    else:
        print("He beat you to the" stone + "!")

def character_select():#works, may need to remove keys and recreate as charater power level i.e fight function
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

    return character_power

def fight(character_power): # need to add charater poweres for avengers
    character_health = 150
    thanos_health = 150

    while character_health > 0 and thanos_health > 0:
        character_damage = random.randint(10, 20)
        thanos_damage = random.randint(5, 15)
        character_health -= thanos_damage
        thanos_health -= character_damage

    return character_health > 0

def world(): #works!
    b = input("Find the soul stone on one of these worlds: \nAsgardianShip, Knowhere, Vormir, Wakanda, Titan, Xandar ")
    print("Entering warp seed to", b)
    pause()

    for num in range(5, 0, -1):
        print(num)

    print("You have arrived at", b)

    character_power = character_select()
    infinity(b, character_power)

def main():
    character_power = character_select()
    world()
    infinity()
    fight()

main()
