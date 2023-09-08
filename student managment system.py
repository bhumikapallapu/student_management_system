
class Student:
    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no
        self.name = name
        self.age = age

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, age):
        student = Student(roll_no, name, age)
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No student records found.")
        else:
            print("Student Records:")
            for student in self.students:
                print(f"Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student found - Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}")
                return
        print(f"Student with Roll No {roll_no} not found.")

    def main():
        student_manager = StudentManager()

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            student_manager.add_student(roll_no, name, age)
            print("Student added successfully!")

        elif choice == "2":
            student_manager.display_students()

        elif choice == "3":
            roll_no = input("Enter Roll No to search: ")
            student_manager.search_student(roll_no)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
    if __name__ == "__main__":
          main()





