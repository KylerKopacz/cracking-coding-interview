'''
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

ANALYSIS:
    - Runtime Complexity: Probably O(n)
        - I am really unsure about this runtime because the actual function that is doing all the work
        is a built in function. This function is built into Java, JavaScript, and Python, so honestly
        if I am asked about this I would just use the built in function. If they say I cannot then 
        I'll worry about it when I get to it.

    - Space Complexity: O(n)
        - I think this is the case because we are just using the input string. I guess since we are not
        editing it, it might just be the case that it's just O(1) because we aren't really using any additional
        space, just the string that is given to us.

    - Best Case Runtime: O(n)
        - I think this is the case because like all the other string problems, you have to know what you're 
        working with. I can not see a faster way than iterating through the string, and just replacing 
        every space with the '%20'. I suppose that if you were going to do this in place, it would be
        something like O(n^2) because you would have to copy and paste the ending of the array everytime
        that you run into a space.
    
'''

def solver(input):
    # This is made really simple in python, but how would I do this if it was an array?
    x = input[0]
    x = x.replace(" ", "%20")

    return x

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
    inputs = [("Mr John Smith", 13)] # THE INPUTS FOR THE SOLVER
    expected = ['Mr%20John%20Smith'] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)