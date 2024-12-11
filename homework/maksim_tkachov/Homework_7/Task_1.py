import random

random_value = random.randint(0, 9)

while True:
    user_input = input('Please enter a number (0-9): ')

    if user_input.isdigit() and 0 <= int(user_input) <= 9:
        user_input = int(user_input)

        if random_value == user_input:
            print('Congratulations! You guessed it!')
            break
        else:
            print('Try again')
    else:
        print('Invalid input. Please enter a number between 0 and 9.')
