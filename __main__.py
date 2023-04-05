from src.py_testing import School


def main():
    file = "src/conf/school1.txt"
    s1 = School("school1")
    conf = s1.readConf(file)
    s1.createStudent(conf)
    students = s1.getStudents()
    for student in students:
        print(student)


if __name__ == '__main__':
    main()
