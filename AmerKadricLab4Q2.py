import random
import simpleaudio as sa
import matplotlib.pyplot as plt

def play_sound(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def spin_treasure_chest(bank, wager, spin_results):
    if bank <= 0:
        print("You're out of funds! Game Over.")
        return bank

    print("\nSpinning the treasure chest...")

    treasure_chest = ['Gold Coin', 'Silver Coin', 'Diamond', 'Ruby', 'Sapphire', 'Emerald']
    chosen_item = random.choice(treasure_chest)
    print(f"You got: {chosen_item}")

    winnings = 0  

    if chosen_item in ['Diamond', 'Ruby', 'Sapphire', 'Emerald']:
        winnings = wager * 2
        print(f"Congratulations! You won {winnings} coins!")
        play_sound('win.wav')
    
    elif chosen_item == 'Gold Coin':
        winnings = wager
        print(f"You won {winnings} coins!")
        play_sound('decent.wav')
    
    else:
        print("No luck this time. Try again!")
        play_sound('sorry.wav')

    bank += winnings  
    bank -= wager  

    # Record the result for visualization
    spin_results.append(chosen_item)

    print(f"Current bank balance: {bank} coins")
    return bank

def visualize_treasure_chest(spin_results):
    unique_items = list(set(spin_results))
    item_counts = [spin_results.count(item) for item in unique_items]

    plt.bar(unique_items, item_counts)
    plt.xlabel('Treasure Chest Items')
    plt.ylabel('Number of Occurrences')
    plt.title('Treasure Chest Item Distribution')
    plt.show()


bank = 1000
spin_results = []

while bank > 0:
    wager = int(input("\nEnter your wager (or 0 to quit): "))
    
    if wager == 0:
        print("Thanks for playing! Final bank balance:", bank)
        break

    bank = spin_treasure_chest(bank, wager, spin_results)

visualize_treasure_chest(spin_results)
print("Game Over.")

