def main():
    for i in range(5):
        print('@@@@@')

    print('5x5')

def aq():
    import time
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
    aq()
   
