'''
GeneralProgramming.py



Functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 40 (notice that each exercise has its own weight)


1 * weight points -  The program works flawlessly and the appropriate ideas to solve it, have been used.

0.75 * weight points - The student has understood the logic and the program works for most inputs.
The code could use some improvement or it is very hard to read. The appropriate ideas to solve the problem have been used.

0.5 * weight points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

0.25 * weight points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

'''
# Write a function with two inputs, one matrix (a list of lists, in which every sublist is the same dimension)
# and a single character. The function will return true if it can find, within the matrix, a 2x2 submatrix made
# with the single character.
#
# Example: Consider the following list, myList = [[1,2,"a","a"], ["a", 3, "a", "a"], [1, 4, 6, 8], [5, 2, 6, 6]]
# that corresponds to the following matrix
# 
#
#
# |  1   2  "a" "a"  |
# | "a"  3  "a" "a"  |
# |  1   4   6   8   |
# |  5   2   6   6   |
#
# in which case the function would return True, if the character was "a" and false otherwise.
# weight = 15

matrix = [[1,2,"a","a"],["a", 3, "a", "a"],[1, 4, 6, 8], [5, 2, 6, 6]]
charecter = "a"

import numpy as np

def find_letter(matrix_input, charecter_input):

    numpy_matrix = np.array(matrix_input)

    for i in range(0,len(numpy_matrix)+1):
        for j in range(0,len(numpy_matrix[i])):

            if i+1 < 4 and j+1 < 4: 

                if numpy_matrix[i][j] == charecter_input and numpy_matrix[i][j+1] == charecter_input: 
                    row = i 
                    column = j 
                    
                    if numpy_matrix[row+1][column] == charecter_input and numpy_matrix[row+1][column+1] == charecter_input: 
                        return "True"

                    else: 
                        return "False"

            else: 
                return "False"

print(find_letter(matrix,charecter))


                    




