# Amer Kadric
# begin

# Import necessary libraries
import random
import simpleaudio as sa
import matplotlib.pyplot as plt

# Function to play a sound from a file
def play_sound(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Function to simulate spinning a treasure chest and updating the player's bank
def spin_treasure_chest(bank, wager, spin_results):
    # Check if the player is out of funds
    if bank <= 0:
        print("You're out of funds! Game Over.")
        return bank

    # Display a message indicating the start of the spin
    print("\nSpinning the treasure chest...")

    # List of possible items in the treasure chest
    treasure_chest = ['Gold Coin', 'Silver Coin', 'Diamond', 'Ruby', 'Sapphire', 'Emerald']
    
    # Randomly select an item from the treasure chest
    chosen_item = random.choice(treasure_chest)
    
    # Display the result of the spin
    print(f"You got: {chosen_item}")

    # Initialize winnings to 0
    winnings = 0  

    # Check the type of item obtained and calculate winnings accordingly
    if chosen_item in ['Diamond', 'Ruby', 'Sapphire', 'Emerald']:
        winnings = wager * 2
        print(f"Congratulations! You won {winnings} coins!")
        # Play a winning sound effect
        play_sound('win.wav')
    elif chosen_item == 'Gold Coin':
        winnings = wager
        print(f"You won {winnings} coins!")
        # Play a sound effect for a decent win
        play_sound('decent.wav')
    else:
        print("No luck this time. Try again!")
        # Play a sound effect for a sorry outcome
        play_sound('sorry.wav')

    # Update the player's bank balance
    bank += winnings  
    bank -= wager  

    # Record the result for visualization
    spin_results.append(chosen_item)

    # Display the current bank balance
    print(f"Current bank balance: {bank} coins")
    return bank

# Function to visualize the distribution of items obtained from spins
def visualize_treasure_chest(spin_results):
    # Identify unique items and their occurrences
    unique_items = list(set(spin_results))
    item_counts = [spin_results.count(item) for item in unique_items]

    # Create a bar chart to visualize item distribution
    plt.bar(unique_items, item_counts)
    plt.xlabel('Treasure Chest Items')
    plt.ylabel('Number of Occurrences')
    plt.title('Treasure Chest Item Distribution')
    plt.show()

# Initialize the player's bank and spin results list
bank = 1000
spin_results = []

# Main game loop
while bank > 0:
    # Get the player's wager from user input
    wager = int(input("\nEnter your wager (or 0 to quit): "))
    
    # Check if the player wants to quit the game
    if wager == 0:
        print("Thanks for playing! Final bank balance:", bank)
        break

    # Perform a spin and update the player's bank balance
    bank = spin_treasure_chest(bank, wager, spin_results)

# Visualize the distribution of items obtained during the game
visualize_treasure_chest(spin_results)
print("Game Over.")

# end
