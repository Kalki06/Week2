students = [
    {"id": 1, "name": "A", "marks": 90},
    {"id": 2, "name": "B", "marks": 75}
]

def add_student(students):
    new_id = int(input("Enter student ID : "))
    new_name = input("Enter student name : ")
    new_mark = int(input("Enter marks : "))

    if(new_mark < 0 or new_mark > 100):
        return "invalid marks"
    
    new_student = {
        "id" : new_id,
        "name" : new_name,
        "marks" : new_mark
    }

    students.append(new_student)
    return "Student added successfully"

def search_student(students, student_id):
    for student in students:
        if(student["id"] == student_id):
            return student
    return None

def delete_student(students, student_id):
    for i in range(len(students)):
        if(students[i]["id"] == student_id):
            students.pop(i)
            return True
    return False

def user_input():
    print(" Enter 1 for Add\n Enter 2 for Delete\n Enter 3 for Search\n Enter 4 for Show All\n Enter 5 for Exit \n")
    user_choice = int(input("Enter your choice here : "))
    return user_choice

def main():
    
    while True:
        choice = user_input()

        if(choice == 1):
            result = add_student(students)
            print(result+"\n")

        elif(choice == 2):
            input_id = int(input("Enter student id to delete : "))
            result = delete_student(students, input_id)
            print(result+"\n")

        elif(choice == 3):
            input_id = int(input("Enter student id to search : "))
            result = search_student(students, input_id)
            if(result == None):
                print("Student not found\n")
            else:
                print("student details properly formatted\n")

        elif(choice == 4):
            for student in students:
                print(student)
                print("\n")
        
        elif(choice == 5):
            print("Exiting.....\n")
            break

        else:
            print("\n")
            print("Please enter valid input \n")

if __name__ == "__main__":
    main()
