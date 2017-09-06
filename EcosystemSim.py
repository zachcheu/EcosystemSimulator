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

animal = [3,3,3,3,3]#1-extinct, 2-endangered, 3-balanced, 4-overpopulated, 5-dangerously overpopulated
currency = 100000

class card:
  def __init__(self,ques,stat1,stat2,dia1,dia2,card):
    self.ques = ques
    self.stat1 = stat1
    self.stat2 = stat2
    self.dia1 = dia1
    self.dia2= dia2
    self.card = card
  

def copy_state(s):
  news = {}
  news['animal']=s['animal']
  news['currency'] = s['currency']
  news['card'] = s['card']
  return news

def can_move(s,m,c):
  '''Tests whether it's legal to move the boat and take
     m missionaries and c cannibals.'''
  side = s['boat'] # Where the boat is.
  p = s['people']
  if m<1: return False # Need an M to steer boat.
  m_available = p[M][side]
  if m_available < m: return False # Can't take more m's than available
  c_available = p[C][side]
  if c_available < c: return False # Can't take more c's than available
  m_remaining = m_available - m
  c_remaining = c_available - c
  # Missionaries must not be outnumbered on either side:
  if m_remaining > 0 and m_remaining < c_remaining: return False
  m_at_arrival = p[M][1-side]+m
  c_at_arrival = p[C][1-side]+c
  if m_at_arrival > 0 and m_at_arrival < c_at_arrival: return False
  return True

def move(olds,m,c):
  '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the boat carrying
     m missionaries and c cannibals.'''
  s = copy_state(olds) # start with a deep copy.
  side = s['boat']
  p = s['people']
  p[M][side] = p[M][side]-m     # Remove people from the current side.
  p[C][side] = p[C][side]-c
  p[M][1-side] = p[M][1-side]+m # Add them at the other side.
  p[C][1-side] = p[C][1-side]+c
  s['boat'] = 1-side            # Move the boat itself.
  return s

def describe_state(s):
  # Produces a textual description of a state.
  # Might not be needed in normal operation with GUIs.
  p = s['people']
  txt = "M on left:"+str(p[M][LEFT])+"\n"
  txt += "C on left:"+str(p[C][LEFT])+"\n"
  txt += "  M on right:"+str(p[M][RIGHT])+"\n"
  txt += "  C on right:"+str(p[C][RIGHT])+"\n"
  side='left'
  if s['boat']==1: side='right'
  txt += " boat is on the "+side+".\n"
  return txt

def goal_test(s):
  '''If all Ms and Cs are on the right, then s is a goal state.'''
  p = s['people']
  return (p[M][RIGHT]==3 and p[C][RIGHT]==3)

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
INITIAL_STATE = {'people':[[3, 0], [3, 0]], 'boat':LEFT }
#</INITIAL_STATE>

#<OPERATORS>
MC_combinations = [(1,0),(2,0),(3,0),(1,1),(2,1)]

OPERATORS = [Operator(
  "Cross the river with "+str(m)+" missionaries and "+str(c)+" cannibals",
  lambda s, m1=m, c1=c: can_move(s,m1,c1),
  lambda s, m1=m, c1=c: move(s,m1,c1) ) 
  for (m,c) in MC_combinations]
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

