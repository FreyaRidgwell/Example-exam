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

# Write a function that returns the largest value that is also an even value in the
# input dictionary whose values are all whole numbers (values, not keys).
# # weight = 5 

def value_greatest_even(input_dictionary):

# declaring and initialising the variable greatest_value as 0 
    greatest_value = 0


# iterating through all of the values in the input_dictionary
    for value in input_dictionary.values(): 

        # checking if the current value is greater than the stored greatest value and if it is even
        if int(value) > greatest_value and int(value) % 2 == 0: 
            greatest_value = value


    return greatest_value

print(value_greatest_even({"hello":5, "yes":12,"england":21, "no": 512, "monkey": 513, "elephant":24}))
