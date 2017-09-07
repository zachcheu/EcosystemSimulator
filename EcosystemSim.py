'''Missionaries.py
("Missionaries and Cannibals" problem)
A SOLUZION problem formulation.
The XML-like tags used here may not be necessary, in the end.
But for now, they serve to identify key sections of this 
problem formulation.  It is important that COMMON_CODE come
before all the other sections (except METADATA), including COMMON_DATA.

This version includes a check for the use of the Tk graphics client.
If this client is being used, then it loads the visualization module:
Missionaries_Array_VIS_FOR_TK.py.

'''
#<METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Ecosystem Simulator"
PROBLEM_VERSION = "1.1"
PROBLEM_AUTHORS = ['Z. Cheung, V. Gupta, E. Song, D., R. Mukai']
PROBLEM_CREATION_DATE = "06-SEP-2017"

# The following field is mainly for the human solver, via either the Text_SOLUZION_Client.
# or the SVG graphics client.
PROBLEM_DESC=\
 '''The <b>"Ecosystem Simulator"</b> An ecosystem simulator/
game made with python that addresses
the wicked problem of bio extinction."
'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
turn = 12
animal = [3,3,3,3,3]#1-extinct, 2-endangered, 3-balanced, 4-overpopulated, 5-dangerously overpopulated
#hawk,snake,rabbit,mouse,flowers
currency = 100000


class card:
  def __init__(self,ques,stat1,stat2,curr,dia1,dia2,card,choiceList):
    self.ques = ques#question
    self.yesStat = stat1#change animal1
    self.noStat = stat2#change animal2
    self.curr = curr#change currency
    self.dia1 = dia1#print after choice1
    self.dia2= dia2#print after choice2
    self.card = card#card number
    self.choiceList = choiceList#list of number to indicate choices
  

def copy_state(s):
  news = {}
  news['turn'] = s['turn']
  news['animal']=s['animal']
  news['currency'] = s['currency']
  news['card'] = s['card']
  return news

def can_move(s,m,c):
  '''Get the card for the state and from that get the listed choices'''
  return True
def changeStat(s,change):
  if change[0] == "h":
    s['animal'][0] += change[1]
  elif change[0] == "s":
    s['animal'][1] += change[1]
  elif change[0] == "r":
    s['animal'][2] += change[1]
  elif change[0] == "m":
    s['animal'][3] += change[1]
  elif change[0] == "f":
    s['animal'][4] += change[1]

def newCard(s):
  
def move(olds,x):
  '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the boat carrying
     m missionaries and c cannibals.'''
  s = copy_state(olds) # start with a deep copy.
  if x == "Yes":
    changeStat(s,s['card'].yesStat)
  elif x == "No":
    changeStat(s,s['card'].noStat)
  s['card'] = newCard()
  
  return s

def describe_state(s):
  # Produces a textual description of a state.
  # Might not be needed in normal operation with GUIs.
  
def goal_test(s):
  '''If all Ms and Cs are on the right, then s is a goal state.'''
  return turn == 0

def goal_message(s):

  return "Congratulations on successfully guiding the missionaries and cannibals across the river!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
#INITIAL_STATE = {'animal':[[3, 0], [3, 0]], 'boat':LEFT }
#</INITIAL_STATE>

#<OPERATORS>
Ecosystem_Operators = ["Yes", "No"]

OPERATORS = [Operator(
  x,
  lambda s, x1 = x: can_move(s,x1),
  lambda s, x1 = x: move(s,x1) ) 
  for x in Ecosystem_Operators]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
render_state = None
  
def use_BRIFL_SVG():
  global render_state
  #from  Missionaries_SVG_VIS_FOR_BRIFL import render_state as rs
  #render_state = rs
  from  Missionaries_SVG_VIS_FOR_BRIFL import render_state
#</STATE_VIS>

