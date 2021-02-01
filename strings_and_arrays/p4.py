'''
Given a string, write a function to check if it is a permutation of a palin­drome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words

ANALYSIS:
    - Runtime Complexity: O(n)
        - You have to know what you're working with once again. You don't know the final character counts
        to run the palindrome analysis until you hash all the values so.
    - Space Complexity: O(n)
        - You have to hold a hash table with all the values that come with the string that you're looking at
    - Best Case Runtime: O(n)
        - I should really verify these with the book.
'''

def solver(input):
    # The first thing that we want to do is strip all spaces from the string so we can only work with characters
    x = input.lower().replace(' ', "")

    # Hash all the values of the string
    chars = {}
    
    # Do that hashing thing
    for c in x:
        if c in chars: 
            chars[c] += 1
        else:
            chars[c] = 1

    # Now that all the characters are hashed, we know that only 1 character can have an odd count, 
    # because palindromes have to be symmetrical
    oddFound = False
    for key, value in chars.items():
        if value % 2 == 1:
            if oddFound:
                return False
            else: 
                oddFound = True

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
    inputs = ['tact coa', 'jeffrrey', 'jeffrreyy', 'race car'] # THE INPUTS FOR THE SOLVER
    expected = [True, False, True, True] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)
