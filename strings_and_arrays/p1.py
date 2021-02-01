'''
Check to see if a string has all different characters or not.
'''

def solver(input):
    '''
    WRITE SOLVER FOR PROBLEM HERE. CAN CHANGE INPUTS!
    '''
    # Just hash all of the characters, and see if we run into a character more than one
    # time
    charMap = {}

    # The boolean that we can flip to return whether we have seen different characters
    # or not.
    toReturn = True

    # For every character in the string, see if we have seen it before
    for letter in input:
        if letter in charMap:
            toReturn = False
            break
        else:
            charMap[letter] = 1

    return toReturn

def check_solutions(outputs, expected, inputs):
    # Check that they are the same size
    if len(outputs) != len(expected):
        print("Length Mismatch: size of outputs ({}) doesn't match expected ({})"
            .format(len(outputs, len(expected))))
        return
    
    # Run through all the solutions, and see what's up
    counter = 0
    for ans, exp, inp in zip(outputs, expected, inputs):
        if ans == exp:
            counter += 1
        else:
            print("======================================================")
            print("Wrong Answer: {} should equal {}".format(ans, exp))
            print("Input: {}".format(inp))
            print("======================================================\n")

    # print the final score
    print("FINAL SCORE: {}/{}".format(counter, len(inputs)))

if __name__ == "__main__":
    inputs = ['abcdefg', 'hello', 'true, falsE'] # THE INPUTS FOR THE SOLVER
    expected = [True, False, True] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)
