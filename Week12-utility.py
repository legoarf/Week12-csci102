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
############     Function Tests    #############
################################################


print("Testing PrintOutput ...")
PrintOutput("This is a test string")

print("\nTesting LoadFile ...")
print("OUTPUT", LoadFile("test.txt"))

print("\nTesting UpdateString ...")
UpdateString("Hello World", "a", 3)







