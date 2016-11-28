# filename: pickle.py
# using pickle lib

import cPickle as cp

shopping_list_file='../file/shop.txt'
shopping_list = ['apple', 'mango', 'carrot']

f=file(shopping_list_file, 'w')
cp.dump(shopping_list, f)
f.close()

f=file(shopping_list_file)
storedlist=cp.load(f)
print 'loading content==%s' % storedlist
