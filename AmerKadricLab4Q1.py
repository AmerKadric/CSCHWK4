#Amer Kadric
#end

import random

# Stores pet profile information
pet_profiles = {}

def add_pet_profile(profile_id):
    """
    Generates and stores a new pet profile with unique attributes.
    """
    # Attributes for pet profiles

    names = ["Buddy", "Bella", "Charlie", "Daisy", "Rocky", "Luna", "Max", "Lucy", "Bailey", "Molly"]

    passwords = ['4WoofWoof$', '9MeowMix!', '1BarkBark@', '5Squeak#', '2PurrPurr%', '6Quack^', '7Neigh&', '3Moo*', '8Cluck(', '0Oink-)']

    adoptionDates = ["01/06/2018", "12/11/2019", "23/07/2020", "04/02/2021", "15/03/2022", "26/09/2023", "07/01/2018", "18/05/2019", "29/10/2020", "10/04/2021"]

    favoriteParks = ["Yellowstone", "Yosemite", "Kruger", "Serengeti", "Banff", "Jiuzhaigou", "Plitvice", "Iguazu", "Komodo", "Galapagos"]

    microchips = ["981-00-0001", "982-00-0022", "983-00-0033", "984-00-0044", "985-00-0055", "986-00-0066", "987-00-0077", "988-00-0088", "989-00-0099", "990-00-0010"]

    accessories = ["Leash", "Collar", "Pet Bed", "Chew Toy", "Scratching Post", "Bird Cage", "Aquarium", "Rabbit Hutch", "Horse Saddle", "Hamster Wheel"]

    experts = ["James Herriot", "Temple Grandin", "Jane Goodall", "Marc Bekoff", "Patricia McConnell", "Ian Dunbar", "Lydia Hiby", "Roger Mugford", "Konrad Lorenz", "David Mech"]
    
    idx = random.randint(0, 9)
    
    profile = {

        "Name": names[idx],

        "Password": passwords[idx],

        "AdoptionDate": adoptionDates[idx],

        "Park": favoriteParks[idx],

        "Microchip": microchips[idx],

        "Accessory": accessories[idx],

        "Expert": experts[idx]
    }
    
    pet_profiles[str(profile_id)] = profile
    print(f"Profile added for Pet ID {profile_id}: {profile['Name']}")

def new_profile_id():
    """
    Generates a new unique profile ID.
    """
    return len(pet_profiles) + 1

def find_pet_profile(name):
    """
    Searches for a pet profile by name and prints the profile information.
    """
    found = False
    for id, details in pet_profiles.items():
        if details.get('Name') == name:
            print(f"Profile found: ID {id}, Details: {details}")
            found = True
            break
    if not found:
        print(f"No profile found for '{name}'.")

# Main interaction loop
while True:
    print("\n--- Pet Profile Manager ---")
    print("1 - Register new pet")
    print("2 - Lookup pet profile")
    print("3 - Quit")
    choice = input("Choose an option: ")

    if choice == '1':
        profile_id = new_profile_id()
        add_pet_profile(profile_id)
    elif choice == '2':
        pet_name = input("Enter pet's name to find: ")
        find_pet_profile(pet_name)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option.")

#end
