'''Missionaries_Array_VIS_FOR_TK.py
Version of Aug. 5, 2017.

'''

from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font

myFont=None

WIDTH = 500
HEIGHT = 500
TITLE = 'Ecosystem Simulator'

def initialize_vis():
  initialize_tk(WIDTH, HEIGHT, TITLE)
  
def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    # Create the default array of colors
    tan = (200,190,128)
    blue = (100,100,255)
    brown = (100, 80, 0)
    purple = (128, 0, 192)
    cyan = (100, 200, 200)
    
    row = [tan]*5
    the_color_array = [row]
    # Now create the default array of string labels.
    row = ['' for i in range(5)]
    the_string_array = [row]

    # Adjust colors and strings to match the state.
    animals = s.animal
    for count,i in enumerate(animals):
      the_string_array[0][count]=i

    caption="Current state of the puzzle. Textual version: "+str(s)        
    the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    print("the_state_array is: "+str(the_state_array))
    the_state_array.show(s)

    
    

    
