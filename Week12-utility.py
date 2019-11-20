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
############     Function Tests    #############
################################################


print("Testing PrintOutput ...")
PrintOutput("This is a test string")

print("\nTesting LoadFile ...")
print(LoadFile('test.txt'))
