'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

ANALYSIS:
    - Runtime Complexity: O(n)
        - Interestingly, this was pretty straight forward with strings, but the runtime actually went to
        O(n^2) when using string concatination. So i changed the implementation to use a list instead,
        which adds some space complexity, but reduces the time complexity to O(n)
    - Space Complexity: O(n)
        - The worst case is that the created list is just as big as the input string
    - Best Case Runtime: O(n)
        - You have to iterate through the string and create the counts to see if the ending
        string that you made is going to be longer than the input, so you have to check every
        value I believe.
'''

def solver(input):
    # if the length is 1, then we know what we make is going to be longer no matter what
    if len(input) == 1:
        return input
    
    # Create a new string, and just iterate over the string now
    newString = []
    currChar = input[0]
    currCount = 1
    idx = 1
    while (idx < len(input)):
        if currChar == input[idx]:
            currCount += 1
        else:
            # Add the current count and character to the string
            newString.append(currChar)
            newString.append(str(currCount))

            # reset the variables to their starting state
            currChar = input[idx]
            currCount = 1
        # Always incremement the counter
        idx += 1

    # add the trailing value as well
    newString.append(currChar)
    newString.append(str(currCount))

    # once we have built the string, then we can compare the lengths and return
    return "".join(newString) if len(newString) < len(input) else input

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
    inputs = ['aabcccccaaa', 'aaaaaaaaaab', 'a', 'abcdefgh', 'abcdefghhhhhhhhhhhh', 'aa'] # THE INPUTS FOR THE SOLVER
    expected = ['a2b1c5a3', 'a10b1', 'a', 'abcdefgh', 'a1b1c1d1e1f1g1h12', 'aa'] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)
