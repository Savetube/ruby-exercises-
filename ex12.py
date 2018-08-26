# Subtitle: MODULES and PACKAGES
# this is one of the exercises following the website: www.learnpython.org

# game.py
# import the draw module
import draw

# alternatively import command
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)
    
    
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)
    

# Custom import name

# game.py
# import tge draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)

#print("\n         =====\n")

