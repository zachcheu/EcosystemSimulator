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
# <METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Ecosystem Simulator"
PROBLEM_VERSION = "1.1"
PROBLEM_AUTHORS = ['Z. Cheung, V. Gupta, E. Song, D., R. Mukai']
PROBLEM_CREATION_DATE = "06-SEP-2017"

# The following field is mainly for the human solver, via either the Text_SOLUZION_Client.
# or the SVG graphics client.
PROBLEM_DESC = \
    '''The <b>"Ecosystem Simulator"</b> An ecosystem simulator/
   game made with python that addresses
   the wicked problem of bio extinction."
   '''


# </METADATA>

# <COMMON_DATA>
# </COMMON_DATA>

# <COMMON_CODE>
class Game_State:
    def __init__(self, turn=15, animal=[250, 250, 500, 250, 250], currency=10000, score=0):  # Change parameters as needed for your game.
        self.turn = turn
        self.animal = animal
        self.currency = currency
        self.score = score

    def __copy__(self):
        news = Game_State(self.turn, self.animal, self.currency)  # Change to be consistent with constructor
        return news

    def __str__(self):
        # Produces a textual description of a state.
        txt = "State is on " + str(self.turn) + ". Player has " + str(self.currency) + " dollars. There are " + str(
            self.animal[0]) + " hawk(s), " + str(self.animal[1]) + " snake(s), " + str(self.animal[2]) \
              + " rabbit(s), " + str(self.animal[3]) + " mouse(s), " + str(self.animal[4]) + " flowers. " + "Score is " + str(self.score)
        return txt

    def __eq__(self, other):
        if self is other: return True
        if self is None: return False
        if other is None: return False

        if self.turn != other.turn:
            return False
        elif self.animal != other.animal:
            return False
        elif self.currency != other.currency:
            return False
        return True

    def __hash__(self):
        # This could be as simple as 
        return (str(self)).__hash__()


global turn
turn = 12
animal = [3, 3, 3, 3, 3]  # 1-extinct, 2-endangered, 3-balanced, 4-overpopulated, 5-dangerously overpopulated
# hawk,snake,rabbit,mouse,flowers
currency = [100000]


class card:
    def __init__(self, ques, stat1, stat2, curr, specific, card, choiceList):
        self.ques = ques  # question
        self.yesStat = stat1  # change animal1
        self.noStat = stat2  # change animal2
        self.currency = curr  # change currency
        self.specific = specific
        self.card = card  # card number
        self.choiceList = choiceList  # list of number to indicate choices


# 20 yes-no cards
# 10 - range cards
# 3 - animal cards
cardList = []

# yes-no
cardList.append(card("Do you want to deploy trained hawks to control the snake population?", [("s", -100), ("m", +50)], [],[-550, 0], [], 1, [0, 1]))
cardList.append(card("Do you want to encourage the use of fertilizer created from waste and compose on growing plants?",[("f", 70), ("r", 50), ("m", 50)], [], [-120, 0], "", 2, [0, 1]))
cardList.append(card("Do you want to build a steel factory next to the wildflowers gardens. Toxic waste might leak",[("f", -150), ("r", -60), ("m", -70)], [], [-200, 200], "", 3, [0, 1]))
cardList.append(card("Do you want to legalize the hunting of rabits as game? ", [("r", -90), ("f", 30)], [], [400, 0], "",4,[0, 1]))
cardList.append(card("Do you want to plant and maintain trees to improve the habitat for hawks?", [("h", 90)], [("h", -30)],[-200, 200], "", 5, [0, 1]))
cardList.append(card("Do you want to cut down some trees for wood? It will affect the habitat of hawks.", [("h", -90)],[("h", -30)], [500, -200], "", 6, [0, 1]))
cardList.append(card("Do you want to pass stricter anti-littering laws? Food will increase grass and wildflowers in the area.",[("f", 50)], [("f", -75)], [25, -25], "", 7, [0, 1]))
cardList.append(card("Do you want to approve plans for urban development? This will increase tax revenues, but decrease habitat space.",[("h", -100), ("s", -100), ("r", -100), ("m", -100), ("f", -100)],[("h", 50), ("s", 50), ("r", 50), ("m", 50), ("f", 50)], [1000, -150], "", 8, [0, 1]))
cardList.append(card("Do you want to spray herbicides on the flowers?", [("f", -50)], [("f", -75)], [25, -25], "", 90, [0, 1]))

# range
cardList.append(card("How many endangered rabbit endangered advertisements would you like to put up around the city?", [], [],[-200, 200], ("r", "+", -2), 11, list(range(8, 29))))
cardList.append(card("How many hawk shelters would you like to create?", [], [], [-200, 200], ("h", "+", -3), 12,list(range(8, 29))))

# animal cards
cardList.append(card("What animal would you like to put on the endangered list?", [], [], [-200], [200], 7, list(range(2, 8))))
cardList.append(card("What animal would you like to put on the overpopulated/hunting list?", [], [], [-200], [-200], 8,list(range(2, 8))))


def copy_state(s):
    news = Game_State(s.turn, s.animal, s.currency, s.score)
    return news


def can_move(s, x, i):
    currentCard = newCard(s)
    for l in currentCard.choiceList:
        if l == i:
            if l > 7:
                pop = 0
                if currentCard.specific[0] == "h":
                    pop = s.animal[0]
                elif currentCard.specific[0] == "s":
                    pop = s.animal[1]
                elif currentCard.specific[0] == "r":
                    pop = s.animal[2]
                elif currentCard.specific[0] == "m":
                    pop = s.animal[3]
                elif currentCard.specific[0] == "f":
                    pop = s.animal[4]
                return (int(x) <= pop)
            return True
    return False


def getRangeChange(s, x):
    card = newCard(s)
    if card.specific[0] == "h":
        return [("h", -int(x) * card.specific[2])]
    elif card.specific[0] == "s":
        return [("s", -int(x) * card.specific[2])]
    elif card.specific[0] == "r":
        return [("r", -int(x) * card.specific[2])]
    elif card.specific[0] == "m":
        return [("m", -int(x) * card.specific[2])]
    elif card.specific[0] == "f":
        return [("f", -int(x) * card.specific[2])]


def getAnimalChange(s, x):
    card = newCard(s)
    if x == "hawk":
        return [("h", card.specific[0])]
    if x == "snake":
        return [("s", card.specific[0])]
    if x == "rabbit":
        return [("r", card.specific[0])]
    if x == "mouse":
        return [("m", card.specific[0])]
    if x == "flowers":
        return [("f", card.specific[0])]


def changeStat(s, listChange):
    animals = s.animal
    for change in listChange:
        if change[0] == "h":
            if animals[0] + change[1] > 0 and animals[0] + change[1] < 500:
                animals[0] += change[1]
            elif animals[0] + change[1] <= 0:
                animals[0] = 0
            elif animals[0] + change[1] > 500:
                animals[0] = 500
        elif change[0] == "s":
            if animals[1] + change[1] > 0 and animals[1] + change[1] < 500:
                animals[1] += change[1]
            elif animals[1] + change[1] <= 0:
                animals[1] = 0
            elif animals[1] + change[1] > 500:
                animals[1] = 500
        elif change[0] == "r":
            if animals[2] + change[1] > 0 and animals[2] + change[1] < 500:
                animals[2] += change[1]
            elif animals[2] + change[1] <= 0:
                animals[2] = 0
            elif animals[2] + change[1] > 500:
                animals[2] = 500
        elif change[0] == "m":
            if animals[3] + change[1] > 0 and animals[3] + change[1] < 500:
                animals[3] += change[1]
            elif animals[3] + change[1] <= 0:
                animals[3] = 0
            elif animals[3] + change[1] > 500:
                animals[3] = 500
        elif change[0] == "f":
            if animals[4] + change[1] > 0 and animals[4] + change[1] < 500:
                animals[4] += change[1]
            elif animals[4] + change[1] <= 0:
                animals[4] = 0
            elif animals[4] + change[1] > 500:
                animals[4] = 500


def scoreCalc(s):
    for i in s.animal:
      dif = 0
      if i > 250:
        dif = i - 250
      else:
        dif = 250 - i
      s.score += 50
      while dif > 25:
        s.score -= 5
        dif -= 25
    


def automatePop(s):
    # hawk,snake,rabbit,mouse,flowers
    animal = s.animal[:]
    listChange = [("h", (animal[1] - 250) * 0.1 + (animal[2] - 250) * 0.1 + (animal[3] - 250) * 0.1), \
                  ("s", (animal[2] - 250) * 0.1 + (animal[3] - 250) * 0.1 - (animal[0] - 250) * 0.1), \
                  ("r", (animal[4] - 250) * 0.1 - (animal[0] - 250) * 0.1 - (animal[1] - 250) * 0.1), \
                  ("m", (animal[4] - 250) * 0.1 - (animal[0] - 250) * 0.1 - (animal[1] - 250) * 0.1), \
                  ("f", -(animal[2] - 250) * 0.1 - (animal[3] - 250) * 0.1 + 10)]
    changeStat(s, listChange)


def newCard(s):
    return cardList[s.turn % len(cardList)]


def move(olds, x, i):
    s = copy_state(olds)  # start with a deep copy.
    currentCard = newCard(s)
    if x == "None":
        s.turn -= 1
        return s
    if x == "Yes":
        changeStat(s, currentCard.yesStat)
        s.currency -= currentCard.currency[0]

    elif x == "No":
        changeStat(s, currentCard.noStat)
        s.currency -= currentCard.currency[1]
    elif i > 6:
        changeStat(s, getRangeChange(s, x))
    elif i > 1:
        changeStat(s, getAnimalChange(s, x))
    automatePop(s)
    scoreCalc(s)
    s.turn -= 1
    return s


def describe_state(s):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    return "describing the state"


def goal_test(s):
    '''If all Ms and Cs are on the right, then s is a goal state.'''
    if 0 in s.animal:
        return True
    return (s.turn == 0)


def goal_message(s):
    return "Congratulations on successfully guiding the missionaries and cannibals across the river!"


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s, change=0):
        return self.state_transf(s)


# </COMMON_CODE>

# <INITIAL_STATE>
INITIAL_STATE = Game_State()
# </INITIAL_STATE>

# <OPERATORS>
Ecosystem_Operators = ["Yes", "No", \
                       "hawk", "snake", "rabbit", "mouse", "flowers", "None", \
                       "0", "25", "50", "75", \
                       "100", "125", "150", "175", \
                       "200", "225", "250", "275", \
                       "300", "325", "350", "375", \
                       "400", "425", "450", "475", "500"]

OPERATORS = [Operator(
    x,
    lambda s, x1=x: can_move(s, x1, Ecosystem_Operators.index(x1)),
    lambda s, x1=x: move(s, x1, Ecosystem_Operators.index(x1)))
    for x in Ecosystem_Operators]
# </OPERATORS>

# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>

# <STATE_VIS>
render_state = None


def use_BRIFL_SVG():
    global render_state
    # from  Missionaries_SVG_VIS_FOR_BRIFL import render_state as rs
    # render_state = rs
    from  Missionaries_SVG_VIS_FOR_BRIFL import render_state

# </STATE_VIS>

