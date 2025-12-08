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

def bouncing_ball():
    a,b,c,d,e,n='+- |*\n'
    w=d+c*18+d+n
    s=a+b*18+a+n
    x,y=0,0
    g,h=17,7
    j,k=1,1
    count_sec = 0
    while count_sec < 10:
        if 0>x or x>g:j*=-1;x+=j
        if 0>y or y>h:k*=-1;y+=k
        os.system('cls');print( s+w*y+d+c*x+e+c*(g-x)+d+n+w*(h-y)+s );x+=j;y+=k;time.sleep(0.1)
        count_sec += 0.1

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
