import requests

def get_space_stations(state):
    url = f"https://data.nasa.gov/resource/gvk9-iz74.json?state={state}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve space station data.")
        return None

def display_space_stations(space_stations):
    if space_stations:
        for station in space_stations:
            print(f"Space Station: {station['station_name']}")
            print(f"Location: {station['location']}")
            print(f"Description: {station['description']}")
            print('-' * 30)
    else:
        print("No space station data available for the selected state.")

def main():
    state = input("Enter a state: ")
    space_stations = get_space_stations(state)
    display_space_stations(space_stations)

if __name__ == '__main__':
    main()

    
