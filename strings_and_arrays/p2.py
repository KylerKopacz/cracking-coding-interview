'''
Given two strings, write a method to decide if one is a permutation of the
other.

ANALYSIS:
    - Runtime: O(n)
        - This is because we have to iterate over both of the input strings exactly one time
    - Space complexity: O(n)
        - This is because we have to hash all of the values within the first input.
    - Best Case runtime: O(n)
        - I think this is the case because you have to know what characters are in your string
        in order to see if you have the same number in another.
'''

def solver(input):
    
    # if the lengths of the strings are not the same, then we already know that we don't have a permutation
    if len(input[0]) != len(input[1]):
        return False

    # input format is a tuple (first string, second string)
    chars = {}

    # Hash all the characters in the first string, and then iterate through the second
    for c in input[0]:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    
    # now that all the characters from the first string are hashed, iterate through the second string.
    # while iterating, if a count goes negative, then we know that it's not the same
    # and if there are any characters left, then we know it also is not a permutation
    for c in input[1]:
        # if we have a character that we have never seen, return False
        if c not in chars:
            return False

        # if the above does not return, then we can subtract one from the current value
        if chars[c] - 1 < 0:
            return False
        else:
            chars[c] -= 1
        
    # if we have made it this far then we can just return True
    return True

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
    inputs = [('tacocat', 'catotac'), ('kyler', 'kylerr'), ('race car', 'rac care'), ('kyler', 'rxelyk')] # THE INPUTS FOR THE SOLVER
    expected = [True, False, True, False] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)