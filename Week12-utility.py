# https://github.com/legoarf/Week12-csci102
# Author: Alexander Fryer
# Date: 11/20/19
# Week12-utility.py
# Course: CSCI102 - Section B

################################################
########   Function 1 : PrintOutput    #########
################################################


def PrintOutput(input_str):
    print("OUTPUT {}".format(input_str))

################################################
########   Function 2 : LoadFile       #########
################################################


def LoadFile(input_file):
    # Open the file
    with open(input_file, 'r') as fin:
        # Return list of lines without newline character
        return [line[:-1] for line in fin]

################################################
########   Function 3 : UpdateString   #########
################################################

def UpdateString(input_str, input_str2, index):
    # Print input_str with input_str2 repaced at given index
    PrintOutput(input_str[:index] + input_str2 + input_str[index+1:])

################################################
########   Function 4 : FindWordCount  #########
################################################

    
def FindWordCount(input_list, input_str):
    # Return Num occurances of input_str in input_list
    return len([x for x in input_list if x == input_str])

################################################
########   Function 5 : ScoreFinder    #########
################################################

    
def ScoreFinder(players, scores, name):
    # Make names uniform
    players_lower = [x.lower() for x in players]

    # Find index of name if exits
    try:
        index = players_lower.index(name.lower())
        # Print Output
        PrintOutput("{} got a score of {}".format(players[index],scores[index]))
    except:
        # Print not found if name does not exist
        PrintOutput("player not found")

################################################
########   Function 6 : Union          #########
################################################


def Union(input_list, input_list2):
    # Return union of input lists
    return list({x for x in input_list + input_list2})

################################################
########   Function 7 : Intersection   #########
################################################

def Intersection(input_list, input_list2):
    # Return list of items in both input list
    return [x for x in input_list if x in input_list2]

################################################
########   Function 7 : Intersection   #########
################################################
    

def NotIn(input_list, input_list2):
    # Return list of items in both in first list but not the second
    return [x for x in input_list if x not in input_list2]
    

################################################
############     Function Tests    #############
################################################


##print("Testing PrintOutput ...")
##PrintOutput("This is a test string")
##
##print("\nTesting LoadFile ...")
##print("OUTPUT", LoadFile("test.txt"))
##
##print("\nTesting UpdateString ...")
##UpdateString("Hello World", "a", 3)
##
##print("\nTesting FindWordCount ...")
##a = ["Alice"]*5
##print(*a)
##PrintOutput(str(FindWordCount(a, "Alice")))
##
##print("\nTesting ScoreFinder ...")
##players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
##scores = [5, 8, 10, 6, 10, 4]
##ScoreFinder(players, scores, "jill")
##ScoreFinder(players, scores, "Manuel")
##
##print("\nTesting Union ...")
##players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
##print("OUTPUT", Union(scores, players2))
##
##print("\nTesting Intersection ...")
##print("OUTPUT", Intersection(players, players2))
##
##print("\nTesting NotIn ...")
##print("OUTPUT", NotIn(players2, players))





