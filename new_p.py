import requests

def get_spirit_animal(name):
    url = f"https://api.spiritanimal.com/animals?text={name}"
    response = requests.get(url)
    if response.status_code == 200: i #api status code 200 is no errors
        data = response.json()
        if 'animals' in data:
            return data['animals']
    return None

def display_spirit_animals(animals):
    if animals:
        for animal in animals:
            print(f"Spirit Animal: {animal['name']}")
            print(f"Description: {animal['description']}")
            print('-' * 30)
    else:
        print("No spirit animals found for the given input.")

def main():
    name = input("Enter your name: ")
    spirit_animals = get_spirit_animal(name)
    display_spirit_animals(spirit_animals)

if __name__ == '__main__':
    main()

