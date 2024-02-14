import random

def spin_treasure_chest(bank, wager):
    # Check if the player is out of funds
    if bank <= 0:
        print("You're out of funds! Game Over.")
        return bank

    # Display the spinning process
    print("\nSpinning the treasure chest...")

    # Define possible items in the treasure chest
    treasure_chest = ['Gold Coin', 'Silver Coin', 'Diamond', 'Ruby', 'Sapphire', 'Emerald']

    # Randomly choose an item from the treasure chest
    chosen_item = random.choice(treasure_chest)
    print(f"You got: {chosen_item}")

    # Initialize winnings
    winnings = 0  

    # Check the outcome based on the chosen item
    if chosen_item in ['Diamond', 'Ruby', 'Sapphire', 'Emerald']:
        winnings = wager * 2
        print(f"Congratulations! You won {winnings} coins!")
    
    elif chosen_item == 'Gold Coin':
        winnings = wager
        print(f"You won {winnings} coins!")
    
    else:
        print("No luck this time. Try again!")

    # Update bank balance by adding winnings and subtracting the wager
    bank += winnings  
    bank -= wager  

    # Display the current bank balance
    print(f"Current bank balance: {bank} coins")
    return bank

# Example usage:
bank = 1000

# Game loop
while bank > 0:
    wager = int(input("\nEnter your wager (or 0 to quit): "))
    
    # Check if the player wants to quit
    if wager == 0:
        print("Thanks for playing! Final bank balance:", bank)
        break

    # Spin the treasure chest and update the bank balance
    bank = spin_treasure_chest(bank, wager)

# End of the game
print("Game Over.")
