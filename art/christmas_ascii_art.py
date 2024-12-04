import colorama
from colorama import Fore, Style
import random

colorama.init(autoreset=True)  # Initialize colorama for color output

def __generate_christmas_tree(height):
    """Generate an ASCII Christmas tree with cohesive colors."""
    tree = []
    
    # Colors
    tree_color = Fore.GREEN
    ornament_colors = [Fore.RED, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
    trunk_color = Fore.LIGHTBLACK_EX

    # Generate the tree body
    for i in range(1, height + 1):
        spaces = " " * (height - i)  # Padding for the tree shape
        if i == 1:
            stars = [Fore.YELLOW + '!']
        else:
            stars = [
                random.choice(ornament_colors) + "o" if random.random() < 0.35 else tree_color + "*"
                for _ in range(2 * i - 1)
            ]
        tree.append(spaces + "".join(stars))

    # Generate the trunk
    trunk_width = max(3, height // 3)  # Trunk width scales with tree height
    trunk_height = max(1, height // 4)  # Trunk height scales with tree height
    trunk = [
        " " * ((height - trunk_width // 2)-1) + trunk_color + "|" * trunk_width
        for _ in range(trunk_height)
    ]

    return "\n".join(tree + trunk)

def print_random_ascii_art():
    ascii_art = [os.path.join(os.path.dirname(__file__), 'ascii_art\\santa_ascii.txt'), os.path.join(os.path.dirname(__file__), 'ascii_art\\snowman_ascii.txt'), 'tree']
    art = random.choice(ascii_art)
    if art == 'tree':
        ascii_tree = __generate_christmas_tree(height=8)
        print(ascii_tree)
    else:
        with open(art) as f:
            lines = []
            for line in f.readlines():
                current_line = []
                for char in line:
                    if char == 'D':
                        current_line.append(Fore.RED)
                    elif char == 'W':
                        current_line.append(Fore.WHITE)
                    elif char == 'B':
                        current_line.append(Fore.BLACK)
                    elif char == 'Y':
                        current_line.append(Fore.YELLOW)
                    else:
                        current_line.append(char)
                lines.append(''.join(current_line))
            print(''.join(lines))
            
