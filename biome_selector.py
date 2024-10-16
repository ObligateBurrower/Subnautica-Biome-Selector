import os
import random
import subprocess
import sys

# List of biomes for selection
biomes = ["Blood Kelp Zone", "Bulb Zone", "Crag Field", "Crash Zone", "Crater Edge", "Dunes", "Grand Reef",
          "Grassy Plateaus", "Kelp Forest", "Mountains", "Mushroom Forest", "Safe Shallows", "Sea Treader's Path",
          "Sparse Reef", "Underwater Islands", "Floating Island", "Mountain Island", "Blood Kelp Caves",
          "Bone Fields Caves", "Bulb Zone Caves", "Deep Sparse Reef", "Deep Grand Reef", "Dunes Caves",
          "Grand Reef Caves", "Grassy Plateaus Caves", "Inactive Lava Zone", "Jellyshroom Cave", "Kelp Forest Caves",
          "Lava Lakes", "Lost River", "Mountains Caves", "Mushroom Forest Caves", "Safe Shallows Caves",
          "Sea Treader's Tunnel Caves", "Underwater Islands Caves", "Crash Zone Mesas", "Lava Geyser", "Lava Castle",
          "Inactive Lava Zone Corridor"]


def select_biome(num_of_base):
    # Randomly select a specified number of biomes
    return random.choices(biomes, k=num_of_base)


def write_to_file(num_of_base):
    # Get the selected biomes and write them to a file
    selected_biomes = select_biome(num_of_base)
    with open('selected_biomes.txt', 'w') as f:
        f.write("\n".join(selected_biomes))


def open_file(file_name):
    print(file_name)
    if os.name == 'nt':
        os.startfile(file_name)
    else:
        subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open', file_name])
    pass


def main():
    # Main loop for user input and processing
    while True:
        input_num = input("How many bases are you planning on building? ")
        try:
            # Attempt to convert input to an integer
            input_num = int(input_num)
            # Write the selected biomes to a file
            write_to_file(input_num)
            break
        except ValueError:
            # Handle non-integer inputs
            print("Please enter an integer.")

    open_file('selected_biomes.txt')


# Entry point of the script
if __name__ == "__main__":
    main()
