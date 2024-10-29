#ARC3EXAM3

#student class to create each variable
class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Score: {self.score}"

#function to add students
def add_student(student_list, student):
    student_list.append(student)

#function to search students
def search_student(student_list, student_id):
    for student in student_list:
        if student.student_id == student_id:
            return str(student)
    return "Student could not be found"

#function to get the score
def get_score(student):
    return student.score

#function to sort the student list
def sort_students(student_list):
    return sorted(student_list, key=get_score, reverse=True)

#list of students
students = [
    Student(1, "Alejandro", 99),
    Student(2, "Jose", 96),
    Student(3, "Amadeo", 89)
]

# while loop to manage everything you can do like adding, searching, sorting or exiting.
while True:
    print("\nStudent Management Menu:")
    print("1. Add a student")
    print("2. Search for a student")
    print("3. Sort students")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        #adding a student
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        score = int(input("Enter student score: "))

        new_student = Student(student_id, name, score)
        add_student(students, new_student)
        print("Student added successfully!")

    elif choice == "2":
        #searching for a student
        search_id = int(input("Enter student ID to search: "))
        result = search_student(students, search_id)
        if result:
            print("Student found:", result)
        else:
            print("Student could not be found.")

    elif choice == 3:
        #sorting
        student_id = int(input("Enter the student ID to search for: "))
        result = search_student(students, student_id)  
        if result:
            print("Student found:")
            print(result)
        else:
            print("Student could not be found.")

    elif choice == "4":
        #exiting the program
        print("Exiting the program")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
