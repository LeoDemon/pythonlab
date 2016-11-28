# DATA-STRUCT for list, tuple, dict, sequence, reference, string

def tt_list():
    shoppingList = ['apple', 'mango', 'carrot', 'banana', 'orange', 'peach']
    print 'I have ', len(shoppingList), ' items to purchase.'
    print 'The items are: '
    for item in shoppingList:
        print item

    print 'I also have to buy pitaya.'
    shoppingList.append('pitaya')
    print 'Now, my shopping list is: ', shoppingList

    shoppingList.sort()
    print 'After sort, my shopping list is: ', shoppingList

    print 'The first fruit I will buy is: ', shoppingList[0]
    del shoppingList[0]
    print 'I have bought the first fruit, now my shopping list is:', shoppingList

    shoppingList.append(12358)
    print 'Append digital, my shopping list is: ', shoppingList

def tt_tuple():
    zoo = ('wolf', 'elephant', 'penguin')
    print 'The old zoo has %d animals.' % len(zoo)
    new_zoo = ('monkey', 'dolphin', zoo)
    print 'The new zoo has ', len(new_zoo), ' animals.'
    print 'All animals in new zoo are:', new_zoo
    print 'Animals brought from old zoo are:', new_zoo[2]
    print 'The animal brought from old zoo is:', new_zoo[2][2]

def tt_dict():
    address = {'leo':'jwkljh@163.com', 'lijha':'lijha@si-tech.com.cn'}
    print "Leo's address is [%s]" % address['leo']
    address['sophie'] = 'sophie1.wang@lcfc.com'
    del address['leo']
    print 'There are %d contacts in the address.They are:' % len(address)
    for name, add in address.items():
        print '     (%s, %s)' % (name, add)
    if 'lijha' in address:
        print "lijha's address is [%s]" % address['lijha']

def tt_seq():
    shoppingList = ['apple', 'mango', 'carrot', 'banana', 'orange', 'peach']
    print 'shoppingList[0]=%s' % shoppingList[0]
    print 'shoppingList[1]=%s' % shoppingList[1]
    print 'shoppingList[2]=%s' % shoppingList[2]
    print 'shoppingList[3]=%s' % shoppingList[3]
    print 'shoppingList[-1]=%s' % shoppingList[-1]
    print 'shoppingList[-2]=%s' % shoppingList[-2]
    print 'shoppingList[-3]=%s' % shoppingList[-3]
    print 'shoppingList[1]~[3]=', shoppingList[1:3]
    print 'shoppingList[2]~end=', shoppingList[2:]
    print 'shoppingList[1]~[-1]=', shoppingList[1:-1]
    print 'shoppingList[all]=', shoppingList[:]

    name = 'Hello,Python!'
    print 'characters 1~3==', name[1:3]
    print 'characters 2~end==', name[2:]
    print 'characters 1~-1==', name[1:-1]
    print 'characters All==', name[:]

def tt_reference():
    shoppingList = ['apple', 'mango', 'carrot', 'banana', 'orange', 'peach']
    cpyList = shoppingList
    del cpyList[0]
    print 'shoppingList=', shoppingList
    print 'cpyList=', cpyList
    cpyList = shoppingList[:]
    del cpyList[0]
    print 'shoppingList=', shoppingList
    print 'cpyList=', cpyList

def tt_str():
    name='China,2016!'
    var1='Ch'
    var2='na'
    var3='2016'
    delimiter='~'
    if name.startswith(var1):
        print 'Yes, the string starts with "%s"' % var1
    else:
        print 'No, the string does not start with "%s"' % var1
    if var2 in name:
        print 'Yes, the string contains "%s"' % var2
    else:
        print 'No, the string does not contains "%s"' % var2
    if name.find(var3) != -1:
        print 'Yes, the string contains "%s"' % var3
    else:
        print 'No, the string does not contains "%s"' % var3
    myList = ['Brazil','Russia','India']
    print delimiter.join(myList)

if __name__ == '__main__':
    tt_str()
else:
    print 'being imported from another module...'
