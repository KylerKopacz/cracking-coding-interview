'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

ANALYSIS:
    - Runtime Complexity: O(n)
        - this has to be O(n) because you are iterating through the strings only one time
    - Space Complexity: O(1)
        - There really is nothing that we are storing here
    - Best Case Runtime: O(n)
        - You gotta know the contents of both strings to compare them
'''
def checkOneInsertion(input):
    # assign s1 to be larger of the two strings inputted
    s1 = input[0] if len(input[0]) > len(input[1]) else input[1]
    s2 = input[1] if len(input[1]) > len(input[0]) else input[0]

    # indices to traverse the two strings
    idx1, idx2 = 0, 0
    diffFound = False
    while(idx1 < len(s1) and idx2 < len(s2)):
        if s1[idx1] != s2[idx2]:
            if diffFound:
                return False
            else:
                diffFound = 1
                idx2 += 1
        else:
            idx1 += 1
            idx2 += 1
    
    # If we have made it this far, then we can return True
    return True

def solver(input):
    # The lengths tell us which comparison we have to do.
    if len(input[0]) == len(input[1]):
        # if they are the same, then check and see if we are one replace away
        foundDiff = False
        for x in range(len(input[0])):
            if input[0][x] != input[1][x]:
                if foundDiff:
                    return False
                else:
                    foundDiff = True
        
        return True
    else:
        return checkOneInsertion(input)

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
    inputs = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('pale', 'bake'), ('kyler', 'kylers'), ('kyler', 'relyk')] # THE INPUTS FOR THE SOLVER
    expected = [True, True, True, False, True, False] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)
