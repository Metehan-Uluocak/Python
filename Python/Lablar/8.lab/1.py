class Person:
    def __init__(self, first_name, last_name, age, department=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}"

class Instructor(Person):
    def __init__(self, first_name, last_name, age, main_branch, department=""):
        super().__init__(first_name, last_name, age, department)
        self.main_branch = main_branch

    def get_main_branch(self):
        return self.main_branch

    def __str__(self):
        return f"Instructor: {super().__str__()}, Main Branch: {self.get_main_branch()}"

class Graduate(Person):
    def __init__(self, first_name, last_name, age, graduation_year, graduation_gpa, department=""):
        super().__init__(first_name, last_name, age, department)
        self.graduation_year = graduation_year
        self.graduation_gpa = graduation_gpa

    def get_graduation_year(self):
        return self.graduation_year

    def get_graduation_gpa(self):
        return self.graduation_gpa

    def __str__(self):
        return f"Graduate: {super().__str__()}, Graduation Year: {self.get_graduation_year()}, Graduation GPA: {self.get_graduation_gpa()}"

class Student(Person):
    predefined_courses = {"Com101", "Com201", "Com301"}
    def __init__(self, first_name, last_name, age, student_id, department=""):
        super().__init__(first_name, last_name, age, department)
        self.student_id = student_id
        self.courses = set()

    def get_student_id(self):
        return self.student_id

    def control_and_add_course(self, course):
        if course not in Student.predefined_courses:
            self.courses.add(course)
            print(f"{course} added to the courses.")
        elif course in Student.predefined_courses:
            print(f"{course} already in the predefined_courses")
        elif course in self.courses:
            self.courses.add(course)
            print(f"{course} added to the courses.")
        else:
            print(f"{course} is already in the courses.")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{course} removed from the courses.")
        else:
            print(f"{course} is not in the courses.")

    def get_courses(self):
        return self.courses
    
    def __str__(self):
        courses_str = ', '.join(self.get_courses()) if self.get_courses() else "No courses"
        return f"Student: {super().__str__()}, Student ID: {self.get_student_id()}, Courses: {courses_str}"


instructor1 = Instructor("Ayse", "Demir", 35, "Computer Science", "Computer Engineering")
graduate1 = Graduate("Cem", "Kara", 25, 2020, 3.5, "Computer Engineering")
student1 = Student("Ahmet", "Yilmaz", 20, "12345", "Computer Engineering")
student1.control_and_add_course("Math101")
student1.control_and_add_course("Physics101")
student1.control_and_add_course("Com101")
student1.remove_course("Physics101")
student1.control_and_add_course("Com102")


print(student1)
print(instructor1)
print(graduate1)
