# filename: stack_queue.py
# learning stack & queue

val_list = []
opt_chr = 'uovq'

def push_val():
    input_val = input('Enter a new string: ').strip()
    if(input_val == ''):
        print ('Warning: you input a null string, please try again!')
    else:
        val_list.append(input_val)

def pop_val():
    if 0 == len(val_list):
        print ("Cann't pop from an empty list!")
    else:
        print ('Erase the item [%s]!' % val_list.pop())

def view_val():
    if 0 == len(val_list):
        print ('Empty list, no item!')
    else:
        for k, v in enumerate(val_list):
            print (k, v)

cmd_opt = {'u':push_val, 'o':pop_val, 'v':view_val}

def show_menu():
    pr = '''options:
    u-->push
    o-->pop
    v-->view
    q-->quit

    Enter choice:'''

    while True:
        while True:
            try:
                chce = input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError) as ex:
                print("Excepiton:", ex)
                chce = 'q'
            
            print ('You picked: [%s]' % chce)
            if chce not in opt_chr:
                print ('Invalid option, please try again!')
            else:
                break
            
        if chce == 'q':
            print ('process exit normally!')
            break
            
        cmd_opt[chce]()

if __name__ == '__main__':
    show_menu()
else:
     print ('being imported by another module...')


