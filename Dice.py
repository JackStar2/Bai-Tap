"""
Viết 1 game Tài xỉu dưa trên nguyên tắc gieo 2 con xúc sắc ngẫu nhiên.
Nếu tổng giá trị của 2 con xúc sắc > 5, gọi là "Tài"
Còn không, gọi là "Xỉu"

Cho người dùng chọn 1 trong 2 trạng thái Tài hoặc Xỉu.
So sánh kết quả.
Hỏi người chơi có tiếp tục không? Nếu có thì chơi tiếp cho dến khi người dùng chọn không.

Mở rộng:
    1. Bắt đầu chơi, cho người dùng 1 số tiền là 100,000. Số tiền cược của mỗi lần chơi
        là 10,000. Sau khi người dùng chọn không chơi tiếp hoặc hết tiền thì ngưng. Sau đó thống kê
        tiền của người chơi, số ván thắng. (có thể cho người dùng chọn số tiền đặt cược)
    2. Cho phép người dùng cược vào số 5 (3 trạng thái thay vì 2 (Tài/Xỉu). Nếu người dùng cược đúng
        thì thắng được 3 lần số tiền cược.
"""
import random


def roll_dice():
    """Gieo 2 con xúc sắc ngẫu nhiên và trả về tổng giá trị của 2 con xúc sắc"""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


def main():
    """Chương trình chính"""
    print("Chào mừng bạn đến với game Tài Xỉu!")
    balance = 100000  # Số tiền bắt đầu
    bet_amount = 10000  # Số tiền cược mỗi lần chơi

    while True:
        print(f"Số dư hiện tại của bạn: {balance} VND")
        if balance < bet_amount:
            print("Bạn không đủ tiền để chơi tiếp.")
            break

        # Người dùng chọn trạng thái cược
        user_choice = input("Bạn muốn cược Tài, Xỉu hay 5? (T/X/5): ").strip().upper()
        if user_choice not in ['T', 'X', '5']:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue

        # Gieo xúc sắc
        total = roll_dice()
        print(f"Tổng giá trị của 2 con xúc sắc là: {total}")

        # Kiểm tra kết quả
        if total > 5:
            result = 'T'
        elif total < 5:
            result = 'X'
        else:
            result = '5'

        # So sánh kết quả và cập nhật số dư
        if user_choice == result:
            balance += bet_amount
            print("Chúc mừng bạn đã thắng!")
        else:
            balance -= bet_amount
            print("Rất tiếc, bạn đã thua.")

        # Hỏi người dùng có muốn chơi tiếp không
        play_again = input("Bạn có muốn chơi tiếp không? (C/K): ").strip().upper()
        if play_again != 'C':
            break

    print(f"Cảm ơn bạn đã chơi! Số dư cuối cùng của bạn là: {balance} VND")

if __name__ == "__main__":
    main()
