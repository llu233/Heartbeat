import time
import os

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the heart at different sizes
def display_heart(size):
    if size == 1:
        print("  **   **  ")
        print(" ****** ** ")
        print("  ******   ")
        print("   ****    ")
        print("    **     ")
    else:
        print("   **     **   ")
        print(" ****** ****** ")
        print("**************")
        print(" ************ ")
        print("  **********  ")
        print("    ******    ")
        print("     ****     ")
        print("      **      ")

# Function to simulate the beating heart
def beat_heart():
    while True:
        clear_screen()
        display_heart(1)
        time.sleep(0.5)

        clear_screen()
        display_heart(2)
        time.sleep(0.5)

# Start the heart beat simulation
beat_heart()
