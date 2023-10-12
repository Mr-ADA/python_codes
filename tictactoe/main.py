# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
"""

use 2d array to create the TicTacToe map

1+2+3
+++++
4+5+6
+++++
7+8+9

Note
a. 1-9 = number input for user to play with
b. 5x5 array => row 0, 2, 4 with each column 0,2,4 will be occupied with empty list
c. the empty list will later be placed by "X" and "O" symbol
d. player will only have to pick 0 - 9 to place their symbol in accordance with the array structure

"""

#Create a class to draw map

class MyMap:
    map = None
    def __init__(self):
        self.create_list()
        self.draw_map()

    def create_list(self):
        #Task: to create 5 x 5 list (2d list)

        #create tuples called rows and cols
        rows, cols = (5,5)

        self.map = [["+" for i in range(cols)] for j in range(rows)]
    def draw_map(self):
        #Function: to replace some dedicated spot for the players with whitespace
        if(self.map is not None):
            self.map[0][0] = " "
            self.map[0][2] = " "
            self.map[0][4] = " "
            self.map[2][0] = " "
            self.map[2][2] = " "
            self.map[2][4] = " "
            self.map[4][0] = " "
            self.map[4][2] = " "
            self.map[4][4] = " "

    def get_map(self):
        if map is not None:
            # for i in self.map:
            #     print (i)
            return self.map
        return None

#Create player (human)
class Human:

    """
    Ability:
        1. Determine winning status
    """

    achieved_steps = None
    map = None

    def __init__(self, game_map):
        self.map = game_map
        self.achieved_steps = list()

    def get_input(self):
        current_step = int(input("Step:"))
        return current_step

    def display_map(self):
        for rows in self.map:
            print(rows)

    def draw_symbols(self):


        # if the space is occupied by another symbol, repeat
        while True:
            input = self.get_input()
            # draw symbols in accordance with the input number given
            if input == 1:
                print(self.map[0][0] != " ")
                if (self.map[0][0] != " "): continue
                self.map[0][0] = "X"
                self.achieved_steps.append(input)
                break
            elif input == 2:
                if (self.map[0][2] != " "): continue
                self.map[0][2] = "X"
                self.achieved_steps.append(input)
                break
            elif input == 3:
                if (self.map[0][4] !=" "): continue
                self.map[0][4] = "X"
                self.achieved_steps.append(input)
                break
            elif input == 4:
                if (self.map[2][0] != " "): continue
                self.map[2][0] = "X"
                self.achieved_steps.append(input)
                break
            elif input == 5:
                if (self.map[2][2] != " "): continue
                self.map[2][2] = "X"
                self.achieved_steps.append(input)
                break
            elif input == 6:
                if (self.map[2][4] != " "): continue
                self.map[2][4] = "X"
                self.achieved_steps.append(input)
                break
            elif input == 7:
                if (self.map[4][0] != " "): continue
                self.map[4][0] = "X"
                self.achieved_steps.append(input)
                break
            elif input == 8:
                if (self.map[4][2] != " "): continue
                self.map[4][2] = "X"
                self.achieved_steps.append(input)
                break
            elif input == 9:
                if (self.map[4][4] != " "): continue
                self.map[4][4] = "X"
                self.achieved_steps.append(input)
                break
            else:
                print("Invalid Input!")
                continue

    def get_status(self):
        rules = Rules()
        winning_conditions = rules.get_winning_conditons()

        if len(self.achieved_steps) < 3:
            return False

        for condition in winning_conditions:
            if all(step in tuple(self.achieved_steps) for step in condition):
                return True

        return False

#Create player (human)
class Comp:

    """
    Ability:
        1. Determine winning status
    """

    achieved_steps = None
    map = None

    def __init__(self, game_map):
        self.map = game_map
        self.achieved_steps = list()

    def get_input(self):
        current_step = random.randrange(1,9)
        return current_step

    def display_map(self):
        for rows in self.map:
            print(rows)


    def draw_symbols(self):

        #if the space is occupied by another symbol, repeat
        while True:
            input = self.get_input()
            # draw symbols in accordance with the input number given
            if input == 1:
                if (self.map[0][0] != " "): continue
                self.map[0][0] = "O"
                self.achieved_steps.append(input)
                break
            elif input == 2:
                if (self.map[0][2] != " "): continue
                self.map[0][2] = "O"
                self.achieved_steps.append(input)
                break
            elif input == 3:
                if (self.map[0][4] != " "): continue
                self.map[0][4] = "O"
                self.achieved_steps.append(input)
                break
            elif input == 4:
                if (self.map[2][0] != " "): continue
                self.map[2][0] = "O"
                self.achieved_steps.append(input)
                break
            elif input == 5:
                if (self.map[2][2] != " "): continue
                self.map[2][2] = "O"
                self.achieved_steps.append(input)
                break
            elif input == 6:
                if (self.map[2][4] != " "): continue
                self.map[2][4] = "O"
                self.achieved_steps.append(input)
                break
            elif input == 7:
                if (self.map[4][0] != " "): continue
                self.map[4][0] = "O"
                self.achieved_steps.append(input)
                break
            elif input == 8:
                if (self.map[4][2] != " "): continue
                self.map[4][2] = "O"
                self.achieved_steps.append(input)
                break
            elif input == 9:
                if (self.map[4][4] != " "): continue
                self.map[4][4] = "O"
                self.achieved_steps.append(input)
                break
            else:
                print("Invalid Input!")
                continue

    def get_status(self):
        rules = Rules()
        winning_conditions = rules.get_winning_conditons()

        if len(self.achieved_steps) < 3:
            return False

        for condition in winning_conditions:
            if all(step in tuple(self.achieved_steps) for step in condition):
                return True

        return False

#Create a class called Rules which will contain all rules of winning and losing and validation
class Rules:
    winning_conditions = [(1,2,3),(1,4,7),(1,5,9),(4,5,6),(7,8,9),(3,5,7),(2,5,8),(3,6,9)]

    def get_winning_conditons(self):
        return self.winning_conditions


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    #create map and get map instance
    my_map = MyMap()
    game_map = my_map.get_map()

    #instantiate human player
    human = Human(game_map)
    human.display_map()
    #instantiate computer player
    comp = Comp(game_map)

    while True:
        #create human player
        print("========================== HUMAN TURNS ================================")

        human.draw_symbols()
        human.display_map()
        human_flag = human.get_status()
        print("Human Status: ", human_flag)

        #check if human is winning, if not continue to next player
        if human_flag:
            print("Human Wins")
            break

        #create comp player
        print("========================== COMP TURNS ================================")

        comp.draw_symbols()
        comp.display_map()
        comp_flag = comp.get_status()
        print("Comp Status: ", comp_flag)
        #check if computer is winning, if not continue to the next iteration
        if comp_flag:
            print("Comp Wins")
            break