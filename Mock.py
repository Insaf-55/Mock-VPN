# Import necessary modules
import random
import time

# Function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

# Function to simulate a coin flip
def flip_coin():
    return random.choice(['Heads', 'Tails'])

# Main function to execute the simulations
def main():
    # Print the website address
    print("Welcome to the Simulation Program!")
    print("For more information, visit: https://sololearn.com/compiler-playground/W60KujHfIfFP/?ref=app")
    
    # Simulate dice rolls
    print("\nRolling the dice 5 times:")
    for i in range(5):
        result = roll_dice()
        print(f"Roll {i+1}: {result}")
        time.sleep(1)  # Pause for 1 second between rolls
    
    # Simulate coin flips
    print("\nFlipping the coin 5 times:")
    for i in range(5):
        result = flip_coin()
        print(f"Flip {i+1}: {result}")
        time.sleep(1)  # Pause for 1 second between flips
    
    print("\nSimulation complete. Thank you for participating!")

# Entry point of the script
if __name__ == "__main__":
    main()