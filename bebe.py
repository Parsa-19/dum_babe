import os
import time

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

if __name__ == "__main__":
    # main()
    # aq()
    display_timer(int(input("how long it should be (second): ")))
   
