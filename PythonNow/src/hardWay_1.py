#!/usr/bin/env python

# filename: hardWay_1.py
# description: learning python for <<Learn Python the hard way>>
# author: Demon.Lee
# date: 2016.10.23

#list
def testEx38():
    ten_things = "Apples Oranges Crows Telephone Light Sugar"
    print("Wait there's not 10 things in that list, let's fix that.")
    stuff = ten_things.split(' ')
    print("before deal, stuff==%s"%stuff)

    more_stuff = ["Day","Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
    while len(stuff) != 10:
        next_one = more_stuff.pop()
        stuff.append(next_one)
        print("Adding [%s], there's %d items now."%(next_one,len(stuff)))

    print("after deal, stuff==%s"%stuff)
    print("Let's do some things with stuff.")
    print("stuff[1]==%s"%stuff[1])
    print("stuff[-1]==%s"%stuff[-1])
    print("stuff.pop==%s"%stuff.pop())
    print("''.join(stuff)==%s"%' '.join(stuff))
    print("'#'.join(stuff)==%s"%'#'.join(stuff[2:5]))

#dict
def testEx39():
    #create a mapping of state to abbreviation
    states={
        'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New York':'NY',
        'Michigan':'MI'
    }
    #create a basic set of states and some cities in them
    cities={
        'CA':'San Francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
    }
    #add some more cities
    cities['NY']='New York'
    cities['OR']='Portland'
    #print out some cities
    print('---'*10)
    print('NY state has:%s'%cities['NY'])
    print('OR state has:%s'%cities['OR'])
    print('---'*10)
    print('Michigan has:%s'%cities[states['Michigan']])
    print('Florida has:%s'%cities[states['Florida']])
    print('---'*10)
    for state, abbrev in states.items():
        print('[%s] is abbreviated [%s]'%(state, abbrev))
    print('---'*10)
    stateTx = states.get('Texas', None)
    if not stateTx:
        print('Sorry, no [Texas] state!')
    print('---'*10)
    #print(states['xxx'])  #Keyerror
    cityTx = cities.get('TX', 'Does not Exist!')
    print('The city for the state [TX] is: %s'%cityTx)

if '__main__' == __name__:
    #testEx38()
    testEx39()
else:
    print('being imported by another module!')

