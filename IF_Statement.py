def checkAge():
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are not eligible to vote.")
    elif 18 <= age < 65:
        print("You are eligible to vote.")
    else:
        print("Invalid age.")

def checkEven():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

def checkDivisilbe7():
    number = int(input("Enter a number: "))
    if number % 7 == 0:
        print(f"{number} is divisible by 7.")
    else:
        print(f"{number} is not divisible by 7.")

def checkLastDigit():
    number = int(input("Enter a number: "))
    last_digit = number % 10
    if last_digit % 3 == 0:
        print(f"The last digit of {number} is divisible by 3.")
    else:
        print(f"The last digit of {number} is not divisible by 3.")

def guessNumber():
    import random
    number_to_guess = random.randint(1, 10)
    attempts = 0
    while True:
        guess = int(input("Guess the number (between 1 and 10): "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def printWeekday():
    day = int(input("Enter a number (1-7): "))
    if day == 2:
        print("Monday")
    elif day == 3:
        print("Tuesday")
    elif day == 4:
        print("Wednesday")
    elif day == 5:
        print("Thursday")
    elif day == 6:
        print("Friday")
    elif day == 7:
        print("Saturday")
    elif day == 1:
        print("Sunday")
    else:
        print("Invalid input. Please enter a number between 1 and 7.")