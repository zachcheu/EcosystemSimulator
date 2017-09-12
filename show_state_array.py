'''show_state_array.py
This Python module provides the means to use Tk graphics to display a
state visualization that consists of a 2D array of colored boxes, and
possibly some textual labels on them.

It is meant to be used together with the Tk_SOLUZION_Client.py program,
and an appropriately structured problem formulation file and visualization
file such as Missionaries.py and Missionaries_Array_VIS_FOR_TK.py


Version of Aug. 6, 2017.
S. Tanimoto

'''
import tkinter as tk

STATE_WINDOW = None


class state_array:

  def __init__(self, color_array=[], string_array=None, column_headers=[],
               column_footers=[],row_labels_left=[],row_labels_right=[],
               text_color="white",
               text_font=None,
               background=(128,128,128),
               caption="Current State"):
    self.color_array=color_array
    self.string_array=string_array
    self.column_headers=column_headers
    self.column_footers=column_footers
    self.row_labels_left=row_labels_left
    self.row_labels_right=row_labels_right
    self.text_color=text_color
    self.text_font=text_font
    self.background=background
    self.caption=caption
    self.ncols = len(self.color_array[0])
    self.nrows = len(self.color_array)

  def show(self,state):#####
    global STATE_WINDOW
    
    STATE_WINDOW.canvas.delete("all")
    a = state.animal
  
    x0 = 0; y0 = 0;
    cellw = STATE_WINDOW.width / self.ncols
    cellh = STATE_WINDOW.height / self.nrows
    i = 0
    for r in self.color_array:
      #j = 0
      s1 = a[0]
      s2 = a[1]
      s3 = a[2]
      s4 = a[3]
      s5 = a[4]

      hawk=tk.PhotoImage(file="hawk.gif")
      rabbit=tk.PhotoImage(file="rabbit.gif")
      snake=tk.PhotoImage(file="snake.gif")
      mouse=tk.PhotoImage(file="mouse.gif")
      flower=tk.PhotoImage(file="flower.gif")

      ty = -50#text shift y
      iy = 0#image shift y
      STATE_WINDOW.canvas.create_line(200,100,s1+200,100,width=30.0, fill = 'red')
      STATE_WINDOW.canvas.create_text(100,100+ty,text="HAWK")
      STATE_WINDOW.canvas.create_image(100,100+iy, image=hawk)
      hawk.image = hawk
      
      STATE_WINDOW.canvas.create_line(200,220,s2+200,220,width=30.0, fill = 'brown')
      STATE_WINDOW.canvas.create_text(100,220+ty,text="SNAKE")
      STATE_WINDOW.canvas.create_image(100,220+iy, image=snake)
      snake.image = snake

      
      STATE_WINDOW.canvas.create_line(200,340,s3+200,340,width=30.0, fill = 'pink')
      STATE_WINDOW.canvas.create_text(100,340+ty,text="RABBIT")
      STATE_WINDOW.canvas.create_image(100,340+iy, image=rabbit)
      rabbit.image = rabbit
      
      STATE_WINDOW.canvas.create_line(200,460,s4+200, 460,width=30.0, fill = 'gray')
      STATE_WINDOW.canvas.create_text(100,460+ty,text="MOUSE")
      STATE_WINDOW.canvas.create_image(100,460+iy, image=mouse)
      mouse.image = mouse

      STATE_WINDOW.canvas.create_line(200,580,s5+200,580,width=30.0, fill = 'green')
      STATE_WINDOW.canvas.create_text(100,580+ty,text="FLOWER")
      STATE_WINDOW.canvas.create_image(100,580+iy, image=flower)
      flower.image = flower

      STATE_WINDOW.canvas.create_line(700,50,700,580+70,width=5.0, fill = 'black')#limit line

      STATE_WINDOW.canvas.create_text(100,600+50,text="REVENUE:   "+ str(state.currency))
      STATE_WINDOW.canvas.create_text(80,630+50,text="Turn:   "+ str(state.turn))
      
#      for c in r:
#        print(c, end=' ')
#        tk_rgb = "#%02x%02x%02x" % c
#        STATE_WINDOW.canvas.create_rectangle(x0+j*cellw, y0+i*cellh,
#                                             x0+(j+1)*cellw, y0+(i+1)*cellh,
#                                             fill=tk_rgb)
#        if self.string_array:
#          STATE_WINDOW.canvas.create_text(x0+(j+0.5)*cellw, y0+(i+0.5)*cellh,
#                                          text=self.string_array[i][j],
#                                          fill=self.text_color,
#                                          font=self.text_font)
#        j += 1
#      i += 1
#      print()
#    STATE_WINDOW.label.config(text=self.caption)


class state_display(tk.Frame):
  def __init__(self, parent, width=500, height=300):
    super(state_display, self).__init__(parent)
    self.width=width; self.height=height
    self.canvas = tk.Canvas(parent, width=self.width, height=self.height)
    self.canvas.pack()
    self.label = tk.Label(self, text="PopulationSimulator v.0.0.1")
    self.label.pack(padx=20, pady=20)
      

def initialize_tk(width=500, height=300, title='State Displa Window'):
  global STATE_WINDOW
  root = tk.Tk()
  root.title(title)
  the_display = state_display(root, width=width, height=height)
  the_display.pack(fill="both", expand=True)
  STATE_WINDOW = the_display
  print("VIS initialization finished")


def test():
  initialize_tk()
  two_by_two = state_array(color_array=[[(255,0,0),(0,255,0)],[(0,0,255),(255,0,0)]],
                           string_array=[["R","G"],["B","R"]],
                           background=(92,0,128))
  #two_by_two.show()
#test()
if __name__=="__main__":
  test()


