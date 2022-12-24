class Student:
    def __init__(self, first_name) :
        self._first_name = first_name

    @property
    def get_name(self):
        return self._first_name

student = Student("Monica")

print(student._first_name)
print(student.get_name)


class Teacher:
    def __init__(self, name):
        self._name = name
    

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


t = Teacher("Akbari")
print(t.name)
