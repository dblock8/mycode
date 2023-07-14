import random

def pause():
    input("Press Enter to continue...")

def infinity(world_choice):
    stones = ["Soul"]
    world_list = ["AsgardianShip", "Knowhere", "Vormir", "Wakanda", "Titan", "Xandar"]

    random.shuffle(world_list)
    if world_choice in world_list:
        for stone in stones:
            print("You found", stone, "stone on", world_choice)

            thanos_present = random.choice([True, False])

            if thanos_present:
                print("Thanos is here on", world_choice + "!")
                character_power = character_select()
                fight_result = fight(character_power)
                if fight_result:
                    print("You defeated Thanos and saved the universe!")
                else:
                    print("You failed, Snap destroyed half the universe.")
                break

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
            pause()
            break
        else:
            c = input("Do you need help choosing? Yes or No? ")
            if c.lower() == "no":
                print("Please select a valid Avenger.")
            else:
                print("Here are the available Avengers:")
                print(*avengers.keys(), sep="\n")

    return a, character_power

def fight(character_info):
    character = character_info[0]
    character_power = character_info[1]
    character_health = 150
    thanos_health = 150

    while character_health > 0 and thanos_health > 0:
        character_damage = random.randint(10, 20)
	thanos_damage = random.randint(5, 15)
        character_health -= thanos_damage
        thanos_health -= character_damage

        print("Your health:", character_health)
        print("Thanos health:", thanos_health)
        pause()

        # Determine the type of attack based on the character
        if character == "hulk":
            print("Hulk smash!")
        elif character == "thor":
            print("Thunder strike!")
        elif character == "blackpanther":
            print("Slash!")
        elif character == "ironman":
            print("Plasma Beam!")

        # Determine the type of attack for Thanos
        thanos_attack = random.choice(["Crush", "Use_stone", "Punch"])
        print("Thanos used", thanos_attack)

    return character_health > 0

def world():
    b = input("Find the soul stone on one of these worlds: \nAsgardianShip, Knowhere, Vormir, Wakanda, Titan, Xandar ")
    print("Entering warp speed to", b)
    pause()

    for num in range(5, 0, -1):
        print(num)

    print("You have arrived at", b)
    return b

def main():
    character_info = character_select()
    b = world()
    infinity(b)
    fight_result = fight(character_info)
    if fight_result:
        print("You defeated Thanos and saved the universe!")
    else:
        print("You failed, Snap destroyed half the universe.")

main()
