import random


def color():

    BLUE = "\033[94m"
    RED = "\033[91m"
    END_COLOR = "\033[0m"

    print(f"{BLUE} \nYou are an Avenger seeking the Infinty stones on worlds within the Marvel Universe.\nChoose your hero and travel but be warned, Thanos too searches for the stones to recreate the universe by erasing half of it. Defeat him if you cross paths and save the citizens of the Universe\n {END_COLOR}")


def pause():
    input("Press Enter to continue...\n")

def infinity(world_choice): # user chosen world will have stones and thanos randomly placed in this function
    stones = ["Soul", "Mind", "Reality"]
    world_list = ["AsgardianShip", "Knowhere", "Vormir", "Wakanda", "Titan", "Xandar"]

    random.shuffle(world_list)
    if world_choice in world_list:
random.shuffle(stones)
       for stone in stones:
            print("You found", stones, "stone on", world_choice)

            thanos_present = random.choice([True, False])

            if thanos_present: #given random leveled attributes if present 
                print("Thanos is here on", world_choice + "!")
                character_power = character_select()
                fight_result = fight(character_power)

                if fight_result:
                    print("You defeated Thanos and saved the universe!")
                else:
                    print("You failed, Thanos snaps and destroyed half the universe.")
                break
            else:
                print("Nothing but dust and air, Soul stone not here")
                print("The search continues, empty-handed again!")
    return(stones)
def character_select(): #select a character, a key has been created to show power levels

    avengers = {
        "hulk": {"power": 95, "attacks": {"Hulk smash": 25, "Thunderclap": 30}},
        "thor": {"power": 90, "attacks": {"Mjölnir strike": 20, "Lightning blast": 35}},
        "blackpanther": {"power": 50, "attacks": {"Claw slash": 15, "Panther leap": 25}},
        "ironman": {"power": 70, "attacks": {"Repulsor beam": 25, "Uni-beam": 30}}
    }

    while True:
a = input("Choose your Avenger! ").lower()
        if a in avengers:
            character_info = avengers[a]
            print(f"You have chosen {a.capitalize()}, Power level: {character_info['power']}")
            pause()
            break

        else:
            c = input("Do you need help choosing a Hero? Yes or No?\n")
            if c.lower() == "no":
                print("Please select a valid Avenger.\n")
            else:
                print("Here are the available Avengers:\n")
                print(*avengers.keys(), sep="\n")

    return a, character_info

def fight(character_info):
    character = character_info[0]
    character_power = character_info[1]["power"]
    character_health = 150
    thanos_health = 150

    while character_health >= 0  and thanos_health >= 0: # fight contiues to loop until a character health reaches 0
        character_damage = random.randint(10, 20)
        thanos_damage = random.randint(15, 20)#randomly selects damge character can do
        character_health -= thanos_damage
        thanos_health -= character_damage

        print("Your health:", character_health)
 print("Thanos health:", thanos_health)
        pause()

        attacks = character_info[1]["attacks"]# calls on character keys to use attack and power of attack to deal damage
        print(f"Available attacks for {character.capitalize()}:")
        for i, attack in enumerate(attacks, 1): #the enumerate function is used to loop through the attacks dictionary, which contains the available attacks for the selected character.

            print(f"{i}. {attack}")

        attack_choice = int(input(f"Choose an attack (1-{len(attacks)}): "))
        if 1 <= attack_choice <= len(attacks):
            chosen_attack = list(attacks.keys())[attack_choice - 1]
            damage = attacks[chosen_attack]
            print(f"\nYou used {chosen_attack} and dealt {damage} damage.")
            thanos_health -= damage
        else:
            print("Invalid attack choice. Skipping turn.")

        if thanos_health > 0:
            thanos_attack = random.choice(["Crush", "Mind_stone", "Punch"])
            thanos_damage = random.randint(20, 30)
            character_health -= thanos_damage
    print(f"\nThanos used {thanos_attack} and dealt {thanos_damage} damage.")

    return character_health > 0

def world():
    b = input("Find the soul stone on one of these worlds:\nAsgardianShip, Knowhere, Vormir, Wakanda, Titan, Xandar\n")
print("Entering warp speed to", b)
    pause()

    for num in range(5, 0, -1):
        print(num)

    print("You have arrived to", b)
    print("\nThanos has followed you, defeat him or doom the universe!")


def main():
    color()
    character_info = character_select()
    b = world()
    infinity(b)
    fight_result = fight(character_info)
    if fight_result:
        print("\nYou DEFEATED Thanos and saved the universe!\n")
    else:
        print("\nYou FAILED, Thanos snaps and destroyed half the universe.\n")
main()
