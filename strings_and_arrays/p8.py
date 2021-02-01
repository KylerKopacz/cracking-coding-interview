'''
 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.

ANALYSIS:
    - Runtime Complexity:
    - Space Complexity:
    - Best Case Runtime:
'''

def solver(input):
    # seems kinda easy. First we search for all the zeros, noting thier rows and columns.
    # then we just go and zero out all the rows and columns that we come across
    m = len(input)
    n = len(input[0])

    rows = {}
    cols = {}

    for row in range(len(input)):
        for column in range(len(input[row])):
            if input[row][column] == 0:
                if row not in rows:
                    rows[row] = 1
                if column not in cols:
                    cols[column] = 1
    
    # now that we have all rows and columns to zero, just go and zero them.
    # we could make sure that we don't zero something twice, by keeping track
    # of all the coords we have been to so far
    for key, value in rows.items():
        for x in range(n):
            input[key][x] = 0
    
    # do the same thing for cols
    for key, value in cols.items():
        for x in range(m):
            input[x][key] = 0

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
    m1 = [[1,2,3],
          [4,0,5],
          [6,7,8]]
    s1 = [[1,0,3],
          [0,0,0],
          [6,0,8]]
    m2 = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,0]]
    s2 = [[1,2,3,4,0],
          [6,7,8,9,0],
          [0,0,0,0,0]]
    m3 = [[0,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,0]]
    s3 = [[0,0,0,0,0],
          [0,7,8,9,0],
          [0,0,0,0,0]]
    inputs = [m1, m2, m3] # THE INPUTS FOR THE SOLVER
    expected = [s1, s2, s3] # THE EXPECTED ANSWERS FOR THE SOLVER
    outputs = [solver(x) for x in inputs] # THE GENERATED ANSWERS FROM THE SOLVER

    # check the solutions
    check_solutions(outputs, expected, inputs)
