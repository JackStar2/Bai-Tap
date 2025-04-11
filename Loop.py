def printNumbers():
    for i in range(1, 11):
        print(i)

def calculateSum(n):
    if n == 1:
        return 1
    else:
        return n + calculateSum(n - 1)

def calculateOddEvenSum(n):
    if n == 1:
        return 1, 0
    else:
        odd_sum, even_sum = calculateOddEvenSum(n - 1)
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
        return odd_sum, even_sum

def checkHowManyVowel():
    vowels = "aeiouAEIOU"
    string = input("Enter a string: ")
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def countWords():
    string = input("Enter a string: ")
    words = string.split()
    return len(words)

def guessNumber():
    import random
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Guess the Number game!")
    print("Choose difficulty level:")
    print("1. Easy (10 times)")
    print("2. Medium (6 times)")
    print("3. Hard (3 times)")
    difficulty = int(input("Enter your choice (1-3): "))
    if difficulty == 1:
        attempts_allowed = 10
    elif difficulty == 2:
        attempts_allowed = 6
    elif difficulty == 3:
        attempts_allowed = 3
    else:
        print("Invalid choice! Defaulting to Easy level.")
        attempts_allowed = 10
    
    print(f"You have {attempts_allowed} attempts to guess the number.")

    for attempt in range(attempts_allowed):
        guess = int(input("Enter your guess (1-100): "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        elif attempt == attempts_allowed - 1:
            print("You have only one attempt left!")
        else:
            print("Congratulations! You've guessed the number!")
            break

    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    # print(printNumbers())
    # print(calculateSum(10))
    
    # odd_sum, even_sum = calculateOddEvenSum(10)
    # print(f"Odd sum: {odd_sum}, Even sum: {even_sum}")

    # print(f"Number of vowels: {checkHowManyVowel()}")
    # print(f"Number of words: {countWords()}")
    # guessNumber()
    pass



