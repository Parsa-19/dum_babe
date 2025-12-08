import os
import time
import string
import random
import json

with open('os.config.json', 'r') as f:  
    clear_command = json.load(f)['clear_command']

def display_timer():
    limit_sec = int(input("how long it should be (second): "))
    global clear_command
    counter = 0
    try:
        while counter < limit_sec:
            os.system(clear_command)
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

def password_generator():
    pass_len = int(input("how long should the password be: "))
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
    global clear_command
    count_sec = 0
    print('Bouncing Ball! for 10 seconds')
    time.sleep(1.5)
    try:
        while count_sec < 10:
            if 0>x or x>g:j*=-1;x+=j
            if 0>y or y>h:k*=-1;y+=k
            os.system(clear_command);print( s+w*y+d+c*x+e+c*(g-x)+d+n+w*(h-y)+s );x+=j;y+=k;time.sleep(0.1)
            count_sec += 0.1
    except KeyboardInterrupt:
        print('\nbouncing ball STOPED!')
        
def calculator():
    print('\n( Welcome To Calculator )')
    print('you can continue with these prompts as long as you type \"finish\" to get out.')
    print()

    num_pair = []
    num_pair.append(int(input("enter the number? ")))

    while True:
        operator = input("enter the operator [+, -, *, /]? ")
        if operator.lower() == 'finish':
            break
        if operator not in ['+', '-', '*', '/', 'finish']:
            print(f"invalid operator {operator} try again!")
            continue
        
        sec_num = input("enter the number? ")
        if sec_num.lower() == 'finish':
            break

        num_pair.append(int(sec_num))
        current_result = 0
        match operator:
            case '+':
                current_result = num_pair[0] + num_pair[1]
            case '-':
                current_result = num_pair[0] - num_pair[1]
            case '*':
                current_result = num_pair[0] * num_pair[1]
            case '/':
                current_result = num_pair[0] / num_pair[1]
        
        num_pair = [current_result]
        print(f"current result = {current_result}")
    
    print("\nprogram stoped!")


if __name__ == "__main__":
    choise = input("""
Choose function to run 
1: main, 
2: number guess, 
3: timer, 
4: random_passowrd_generator
5: calculator
6: bouncing_ball

enter the number: """)
    funcs = {
        '1': main,
        '2': aq,
        '3': display_timer,
        '4': password_generator,
        '5': calculator,
        '6': bouncing_ball
    }   
    funcs[choise]()
