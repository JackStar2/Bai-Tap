"""
Viết 1 game chgo phép người dùng đoán số từ 1 đến 100.
Game có 3 cấp độ chơi:
    - dễ - đoán tối đa 9 lần
    - vừa - đoán tối đa 6 lần
    - khó - đoán tối đa 4 lần
Sau khi người dùng hoàn tất 1 lần chơi,
    chương trình sẽ hỏi người dùng có chơi nữa không.
    - Nếu người chơi đồng ý thì tiếp tục 1 lần chơi mới.
    - Nếu không thì kết thúc trò chơi, thống kê số lần chơi thắng/thua
"""
import random

def play_game(level):
    if level == 'easy':
        max_attempts = 9
    elif level == 'medium':
        max_attempts = 6
    else:  # hard
        max_attempts = 4

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        guess = int(input(f"Guess the number (1-100), attempt {attempts + 1}/{max_attempts}: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            return True

    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
    return False

if __name__ == "__main__":
    play_again = True
    wins = 0
    losses = 0

    while play_again:
        level = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if level not in ['easy', 'medium', 'hard']:
            print("Invalid level. Please choose again.")
            continue

        if play_game(level):
            wins += 1
        else:
            losses += 1

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

    print(f"Game over! Wins: {wins}, Losses: {losses}")