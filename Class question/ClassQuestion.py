'''
ClassQuestion.py


TOTAL POINTS AVAILABLE: 50


12 points per method, 42 across whole class, 8 points for the creation of the students and the task.

--------------------------------------
Marking for methods:
--------------------------------------

12 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

9-11 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

7-8 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

3-6 points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1-2 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

--------------------------------------
Marking for the creation of students:
--------------------------------------

8 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

6-7 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

4-5 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

2-3points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

'''



# Create a class called Student with one instance attribute called "courses"
# that is created in the constructor.
#   
#   - "courses" will be a dictionary and will start empty in the constructor 
#        but when populated later by other methods: 
#         - the keys will be string describing the name of the course (e.g. 'computing') 
#         - and the values will be a dictionary of two items
#                   1. the first item is 'year' in which the course takes place (an integer from 1 to 4)
#                   2. the second item is 'grade' (expressed with a float from 1 to 100)
#                   (e.g. {'computing': {'year': 1, 'grade': 87.5})

class Student:

# initialising an empty dictionary called courses
# if the attribute is in in ___init___ method then reference the attributes using self.(name of attribute)
    def __init__(self,courses):

        self.courses = courses

# Create a method called add_course(). It should:
#   - have 3 parameters: 'course_name', 'year' and grade
#   - 'grade' has a default value of "None"
#   - it should change the grade of the corresponding course in the "courses" attribute
#        - if the course exists already ask the user (via terminal) if they want to change the existing course.
#           if the user says "yes" or "y", change the grade and the year accordingly. If the grade was not specified, ask the user (via terminal) for the grade
#           if the user writes "no" or "n", ignore it. 
#           keep asking the question until the user inputs either yes/y or no/n
#        - if the course does not already exist in the dictionary, add a new entry

    def add_course(self, course_name, year, grade = None):

# checking if the course_name already exists in the names 
        if course_name in self.courses:

            # providing that the name already exists the user is asked if they would
            # like to change the existing data
            print("Course was found!")
 
            valid_response = False
            
            while valid_response == False:

                response = str(input("Would you like to change the existing course? "))

            # validating the response

                if response == "yes".lower() or response == "y".lower() or response == "no".lower() or response == "n".lower():

                    valid_response = True

                    if response == "yes".lower() or response == "y".lower():

                        # checking if a grade has been provided
                        if grade == None: 
                            
                            print("Grade was not specified!")
                            new_grade = int(input("Please enter the grade: "))

                            new_year = int(year)
                            
                            self.courses[course_name] = {'year': new_year, 'grade': new_grade}
                        

                        else:    
                            new_grade = float(grade)
                            new_year = int(year)

                            self.courses[course_name] = {'year': new_year, 'grade': new_grade}

                        print("Change was sucessful!")
                        print(f"The updated value is {course_name} = {self.courses[course_name]}")


                    # if they would not like to enter any new data "end" is printed
                    elif response == "no" or response == "n":

                        print("End")

            # if the course name dose not already exist in the course names then a new course_name is added 
            # using the adding_values function defined above 
        

        else: 
            print("course was not found so a new one was added")
            self.courses[course_name] = {'year': year, 'grade': grade}
            print("adding sucessful :)")

        
# Create a method called change_grade(). It should:
#   - have 2 parameters: 'course', grade
#   - it should change the grade of the course
#        - if the course exists already, change the grade accordingly
#        - if the course doesn't exist, notify the user that the course doesn't exist and ask them if they want to create one (via terminal).
#          if the user says "yes" or "y", ask for the year of the course and then add the new course accordingly,
#          if the user writes "no" or "n", ignore it. 
#           keep asking the question until the user inputs either yes/y or no/n

    def change_grade(self,course,grade):

        # checking if the couse already exists in the stored names
        if course in self.courses:
            print("Course was found")

            # recieving a grade input if the course already exits
            new_grade = float(grade)

            self.courses = {"grade":new_grade}
            print("Grade sucessfully changed")

        else: 
            print("This course does not exist")

            # providing that the course doesn't already exist the user is asked if they 
            # would like to create a course 

            valid_input = False

            answer = str(input("Would you like to create a course? "))

            while valid_input == False: 

                if answer == "yes" or answer == "y":
                    valid_input = True

                    new_grade = grade
                
                    self.courses = {"grade":new_grade}

                    print(f"The new course is {course} = {self.courses} ")
                
                elif answer == "no" or answer == "n": 

                    valid_input = True
                    print("End") 

# Create a method called calculate_mean(). It should: 
#   - have one parameter, either a list of strings or a year (from 1 to 4):
#   - if the parameter is the year, the method returns the average of all the courses for that specific year. If there are no courses for that year, the method
#     will return "None" and print "No courses added for year {year}"
#   - if the parameter is a list of strings, the method returns the average for all courses in that string. 
#        if any of the courses in the string are not present in the attribute "courses", the method will ignore them and just return
#        the mean for the ones that are present. If none of the courses are present the method will return "None" and print "The student "

    def calculate_mean(self,parameter):

        # defining variables use dto calculate the average 
        year_list = [1,2,3,4]
        grade_total = 0 
        grade_to_calculate = []

        # checking if the parameter is a year
        if parameter in year_list:

            for course in self.courses.keys():

                if self.courses[course]["year"] == parameter:
                    grade_to_calculate.append(self.courses[course]["grade"])

                for i in range(0,len(grade_to_calculate)):
                    grade_total += grade_to_calculate[i]

                # checking if there were any entries for that year
                if len(grade_to_calculate) == 0:
                    
                    print(f"No courses for the year {parameter}")

                    return "None"
                
                # calculating the average if there were any entries
                else:
                    grade_average = grade_total/len(grade_to_calculate)

            print(f"The total grade for the year was {grade_total}")  
            print(f"The number of courses for the year was {len(grade_to_calculate)}")  
            print(f"The grade average for the year was {grade_average}")

        # if the input is not an integer (year) then it is a list of strings representing different courses
        else: 
            courses_to_calculate = []
            course_average = 0

            for i in range(0,len(parameter)):

                # if the course is in the parameter (the input) and is in courses then it is added to another variable called courses_to_calculate
                if parameter[i] in self.courses: 
                    courses_to_calculate.append(parameter[i])
            
            # for each course name in the list courses_to_calculate the grade is extracted and added to a grade total
            for j in range(0,len(courses_to_calculate)):

                grade_total += self.courses[courses_to_calculate[j]]["grade"]
            
            # checking if any of the strings in the parameter were in the student's courses
            if len(courses_to_calculate) > 0: 
                # average for the courses is calculated
                course_average = grade_total/len(courses_to_calculate)
                
                print(f"The average is {course_average}")
            
            # if none were present "The student" is printed as specified
            else: 
                print("None of the entries of the parameter are courses that the student took!")
                print("The student")

                return "None"

# Create 10 instances of the class Student and to each one of them assign a course "computing I" and a
# course "Mathematics". 
#   - Both of them have year 1 as the year and a random grade between 1 and 100.
#   - Write a function called "calculate_overall_mean()" that takes as input any list of students and an optional argument "course" (default None).
#       
#       -If course is not specified the function will return a dictionary with, as keys, all the courses that the students have
#        (mathematics and computing in this example, but there could be more) and as value the mean across the list students.
#       - If course is specified, the function will return the mean for that specific course across the list of students.


student_list = []

def New_student():

    # instances of the class
    from random import randint 

    for i in range(0,10):
        new_student = Student({"computing":{"year":1,"grade":randint(0,100)},
            "mathematics": {"year": 1, "grade":randint(0,100)}
            })

        student_list.append(new_student)

    return student_list


def calculate_overall_mean(self, student_list, course = None):

    dictionary_counting = {}
    dictionary_calculating_means = {}
    total_grade = 0 
    number_of_students = 0

    if course == None: 

        for student in student_list:
            for course in student.courses.keys():

                if course in dictionary_counting:
                    dictionary_counting[course] += 1

                else: 
                    dictionary_counting[course] = 1 

                if course in dictionary_calculating_means: 
                    dictionary_calculating_means[course] += student[course]["grade"]

                else:
                    dictionary_calculating_means.keys.append(course)
                    dictionary_calculating_means[course] += student[course]["grade"]

            for i in dictionary_calculating_means:

# calculating the mean from the total grade currently stored in dictionary_calculating_means[course]
                dictionary_calculating_means[i] = dictionary_calculating_means[course]/dictionary_counting[course]

            return dictionary_calculating_means


    for i in range(0,len(dictionary.keys())):
        if student_list.course == i:

            total_grade += student_list[course]["grade"] 
            number_of_students += 1 



#  New_student()

#for i in student_list:

    #print(i.courses)   
    

student1 = Student({"computing":{"year":1,"grade":5},
            "mathematics": {"year": 1, "grade":3}
            })

#student1.add_course("art",5,6)

#student1.change_grade("pe",6)

#student1.calculate_mean(["french"])


print(calculate_overall_mean(student_list))