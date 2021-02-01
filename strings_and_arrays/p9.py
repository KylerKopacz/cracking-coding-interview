'''
Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

ANALYSIS:
    - Runtime Complexity: O(N)
        - It will operate on exactly how many elements there are in the strings, and
        if we assume the lengths of the strings are the same, then it will touch 2N
        elements, which breaks down to N
    - Space Complexity: O(N)
        - we have to store the value of twice the first string, and that's it.
    - Best Case Runtime: O(N)
        - It's really based on the speed of the built in function that we are given.
'''
def isSubstring(word, another):
    return word in another

def solver(input):
    # Format of input:
    # (s1, s2)

    double = input[1] + input[1]

    return isSubstring(input[0], double)


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
    inputs = [('waterbottle', 'erbottlewat'), ('kyler', 'lerky'), ('waterbottle', 'erbottlewas')] # THE INPUTS FOR THE SOLVER
    expected = [True, True, False] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)
