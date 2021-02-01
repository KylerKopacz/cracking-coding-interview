'''
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

ANALYSIS:
    - Runtime Complexity: O(n^2)
        - I think this is the case because it's a 2D array, of size NxN. So yeah,
        naturally this is going to be an N^2 runtime.
    - Space Complexity: O(n^2)
        - Now here comes the problem with my implementation: This is kinda large for a space
        complexity. However, it really does help with the logic and the debugging process, and allows
        the implementation to be more clear IMO. However, I could see this being kinda slow and cumbersome
        as N increases...
    - Best Case Runtime: O(n^2)
        - You have to visit every value in the array. I could get the space requirement down if I actually
        did this "in place" and used a constant amount of memory everytime (like a single buffer), but that
        increases the complexity of the code a lot in my opinion.

For the sake of this potentially being in an interview, I am not going to do the in place
problem, because I think that would be a really good test of my ability during an interview,
and I don't want it to be disqualified because I have seen it before. #honesty
'''

def solver(input):
    # We have to remember where everything goes right? So lets hash everything.
    # The key is going to be a tuple of coords, and the value is going to be
    # the number stored there.
    table = {}
    
    for x in range(len(input)):
        for y in range(len(input)):
            table[(x, y)] = input[x][y]

    # now that we have all the values memorized, we can start swapping the values in the
    # array, technically in place.
    for x in range(len(input)):
        for y in range(len(input)):
            input[x][y] = table[(len(input) - y - 1, x)]
    
    return input

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
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    s1 = [[7,4,1],[8,5,2],[9,6,3]]
    m2 = [[1,2],[3,4]]
    s2 = [[3,1],[4,2]]
    m3 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    s3 = [[13,9,5,1], [14,10,6,2], [15,11,7,3], [16,12,8,4]]
    
    inputs = [m1, m2, m3] # THE INPUTS FOR THE SOLVER
    expected = [s1, s2, s3] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)
