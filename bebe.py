import os
import time
import string
import random

def display_timer(limit_sec: int):
    counter = 0
    try:
        while counter < limit_sec:
            os.system('clear')
            counter += 1
            print(counter)
            time.sleep(1)
    except KeyboardInterrupt:
        print('\ntimer STOPED!')

def main():
    for i in range(5):
        print('@@@@@')

    print('5x5')

def aq():
    print("I can guess the number you choose!(press any key to continue...)")
    dum = input() 
    guess = int(input("your guess:"))
    print('processing..')
    time.sleep(1)
    yesno = input(f'was it < {guess} > [Y/N]? ')
    if yesno.lower() == 'n':
        print('you son of a liar. I was correct!')
        return
    print('that\'s the power of this program')

def password_generator(pass_len):
    rand_pass = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(pass_len))
    print(rand_pass)
    return rand_pass

if __name__ == "__main__":
    choise = input("""
Choose function to run 
1: main, 
2: number guess, 
3: timer, 
4: random_passowrd_generator

enter the number:
    """)
    funcs = {
        '1': main,
        '2': aq,
        '3': display_timer,
        '4': password_generator
    }   
    choosed_func = funcs[choise]
    if choise == '3':
        limit = int(input("how long it should be (second): "))
        choosed_func(limit)
    elif choise == '4':
        pass_len = int(input("how long should the password be: "))
        choosed_func(pass_len)
    else:   
        choosed_func()
