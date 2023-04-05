class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id + ": " + self.name

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def readConf(self, file):
        try:
            print(f"Reading Input File from {file}")
            with open(file, 'r') as f:
                data_read = [[data.strip() for data in line.split(",") ] for line in f]
                f.close()
                return data_read
        except Exception as error:
            print("error on parsing file")
            raise error

    def createStudent(self, conf):
        for student_conf in conf:
            self.students.append(Student(student_conf[0], student_conf[1]))
    
    def getStudents(self):
        return self.students