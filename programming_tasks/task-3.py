students = {}


while True:
    name = input("Enter student name (or 'done' to finish): ")
    
    if name.lower() == "done":
        break
    
    grade = int(input("Enter grade: "))
    
    students[name] = grade

if students:
    grades = list(students.values())
    average = sum(grades) / len(grades)
    
    highest = max(students, key=students.get)
    lowest = min(students, key=students.get)

    print(f"\nAverage Grade: {int(average)}")
    print(f"Highest Grade: {highest} ({students[highest]})")
    print(f"Lowest Grade: {lowest} ({students[lowest]})")
else:
    print("No student data entered")