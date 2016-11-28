# filename: Persion.py
# learning python class

class Person:
    '''Represents a person'''
    population = 0
    
    def __init__(self, name):
        '''Initializes the person's data'''
        self.name = name
        print 'Initializing %s...' % self.name
        
        # When this person is created, he/she adds to the population
        Person.population += 1
    
    def __delete__(self):
        '''Erase this person'''
        print '%s says bye-bye...' % self.name

        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one...'
        else:
            print 'There are still %d people left...' % Person.population
            
    def sayHi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print 'Hi, my name is %s...' % self.name
        
    def howMany(self):
        '''Prints the current population'''
        if Person.population == 1:
            print 'I am the only person here...'
        else:
            print 'We have %d persons here...' % Person.population

if __name__ == '__main__':
    Leo = Person('LeoDemon')
    Leo.sayHi()
    Leo.howMany()
    print 'Leo\'s information:(%s,%s)...' % (Leo.name, Leo.population)
    print '-----------------separation line--------------------'
    Kinly = Person('Kinly')
    Kinly.sayHi()
    Kinly.howMany()
    print 'Kinly\'s information:(%s,%s)...' % (Kinly.name, Kinly.population)
    print '-----------------separation line--------------------'
    Jack = Person('Jack')
    Jack.sayHi()
    Jack.howMany()
    print 'Jack\'s information:(%s,%s)...' % (Jack.name, Jack.population)
    print '-----------------separation line--------------------'
    Kinly.__delete__()
    Kinly.howMany()
else:
    print 'being imported by another module...'

