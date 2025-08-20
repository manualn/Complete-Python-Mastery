# 4. Print a Grading Report
# 1)Start
# 2)Ask for input 5 comma seperated numbers and store
#  it in variable input
# 3)Convert the input numbers into a list by splitting it at ","
#  and store it in a variable called marks
# 4)Define a function called grading_reports
# 5)Create an empty list in the name grades
# 6)Create a for loop that goes through each mark in the marks list
# 7)Set an if condition if mark is greater than or equal to 90, 
#  then add "A" to grades list
# 8)Similarly for 75, 60, 50 and rest of the numbers
# 9)Return grades list
# 10)Call the function and pass the marks through it and store it
#  in a variable called grade_list
# 11)Print grade_list


number = input("Enter 5 comma-separated numbers: ")

marks = list(map(int, number.split(",")))

def grading_report(marks):
    grades = []
    for mark in marks:
        if mark >= 90:
            grades.append("A")
        elif mark >= 75:
            grades.append("B")
        elif mark >= 60:
            grades.append("C")
        elif mark >= 50:
            grades.append("D")
        else:
            grades.append("F")
    return grades

grade_list = grading_report(marks)
print(f"Grades: {grade_list}")
