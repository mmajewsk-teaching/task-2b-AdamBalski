import collections

# todo: 
# persistence (e.g. via json.dump())
# tui stretch goal

class Test:
    def __init__(self):
        pass
class Teacher:
    def __init__(self, name):
        self.name = name
class Course:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.tests = {}
class Student:
    def __init__(self, name):
        self.name = name
class Class:
    def __init__(self):
        self.students = {}
        self.courses = {}
class School:
    def __init__(self):
        self.classes = {}
        self.teachers = {}

class System:
    def __init__(self):
        self.schools = {}
    # writes
    def register_school(self, s_id, school):
        self.schools[s_id] = school
    def register_class(self, school_id, class_id, clazz):
        self.schools[school_id].classes[class_id] = clazz
    def register_student(self, school_id, class_id, student_id, student):
        self.schools[school_id].classes[class_id].students[student_id] = student
    def register_teacher(self, school_id, teacher_id, teacher):
        self.schools[school_id].teachers[teacher_id] = teacher
    def register_course(self, school_id, class_id, course_id, course):
        self.schools[school_id].classes[class_id].courses[course_id] = course
    def create_test(self, school_id, class_id, course_id, test_uid, test):
        self.schools[school_id].classes[class_id].courses[course_id].tests[test_uid] = test
    def mark_class_instance(self, course_id):
        pass
    def mark_positive_attendance(self, student_id, class_instance_id, course_id):
        pass

    # reads
    def get_gpa_across_classes(self, s_id):
        pass
    def get_in_class_gpa(self, clazz_id, school_id):
        pass
    def count_total_student_attendance(self, school_id, student_id):
        pass
if __name__ == "__main__":
    system = System()

    system.register_school(0, School())
    system.register_class(0, 0, Class())
    system.register_student(0, 0, 0, Student("John Doe"))
    system.register_teacher(0, 0, Teacher("Jane Doe"))
    system.register_course(0, 0, 0, Course(0, "Chemistry"))

