# filename: inherit.py
# learning python class inherited property


class SchoolMember:
    '''Represents any school member'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        '''tell my details'''
        # add a comma at last for avoiding automatic newline added by Python
        print 'details: name==%s, age==%s,'%(self.name, self.age),


class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        print 'I am a teacher...'
        SchoolMember.tell(self)
        print 'salary==%d' % self.salary

class Student(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        print 'I am a student...'
        SchoolMember.tell(self)
        print 'marks==%d' % self.marks


t = Teacher('Liu Chang', 33, 5000)
s = Student('LeoDemon', 28, 86)

members = [t, s]
for member in members:
    member.tell()
    print  # prints a blank line

