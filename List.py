'''
Tạo 1 danh sách (list) ngẫu nhiên N phần tử (N nhập từ bàn phím) có giá trị từ 1 đến N sau đó tạo 1 menu cho phép thực hiện các công việc sau:

In ra danh sách vừa tạo.
In đảo ngược danh sách.
Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất.
đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
In ra vị trí các phần tử là số nguyên tố.
tìm các số duy nhất (không trùng lặp) trong danh sách.
liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
In ra các đoạn con trong danh sách giảm liên tiếp.
'''

def create_random_list(n):
    import random
    return [random.randint(1, n) for _ in range(n)]

def print_list(lst):
    print("Danh sách:", lst)

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

def find_max(lst):
    max_value = max(lst)
    max_index = lst.index(max_value)
    return max_value, max_index

def count_occurrences(lst, x):
    count = lst.count(x)
    positions = [i for i, value in enumerate(lst) if value == x]
    return count, positions

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_positions(lst):
    return [i for i, value in enumerate(lst) if is_prime(value)]

def find_unique(lst):
    return list(set(lst))

def count_occurrences_all(lst):
    from collections import Counter
    return Counter(lst)

def find_decreasing_subsequences(lst):
    subsequences = []
    current_subsequence = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            current_subsequence.append(lst[i])
        else:
            if len(current_subsequence) > 1:
                subsequences.append(current_subsequence)
            current_subsequence = [lst[i]]

    if len(current_subsequence) > 1:
        subsequences.append(current_subsequence)

    return subsequences

def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = create_random_list(n)
    print_list(lst)

    while True:
        print("\nMenu:")
        print("1. In ra danh sách")
        print("2. In đảo ngược danh sách")
        print("3. Sắp xếp danh sách")
        print("4. Tìm phần tử lớn nhất và vị trí của nó")
        print("5. Đếm số lượng các phần tử bằng giá trị X và in ra vị trí xuất hiện")
        print("6. In ra vị trí các phần tử là số nguyên tố")
        print("7. Tìm các số duy nhất trong danh sách")
        print("8. Liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó")
        print("9. In ra các đoạn con trong danh sách giảm liên tiếp")
        print("0. Thoát")

        choice = int(input("Chọn một tùy chọn: "))

        if choice == 1:
            print_list(lst)
        elif choice == 2:
            reversed_lst = reverse_list(lst)
            print_list(reversed_lst)
        elif choice == 3:
            sorted_lst = sort_list(lst)
            print_list(sorted_lst)
        elif choice == 4:
            max_value, max_index = find_max(lst)
            print(f"Phần tử lớn nhất: {max_value}, Vị trí: {max_index}")
        elif choice == 5:
            x = int(input("Nhập giá trị X: "))
            count, positions = count_occurrences(lst, x)
            print(f"Số lượng phần tử bằng {x}: {count}, Vị trí: {positions}")
        elif choice == 6:
            prime_positions = find_prime_positions(lst)
            print(f"Các vị trí các phần tử là số nguyên tố: {prime_positions}")
        elif choice == 7:
            unique_values = find_unique(lst)
            print(f"Các số duy nhất trong danh sách: {unique_values}")
        elif choice == 8:
            occurrences = count_occurrences_all(lst)
            for value, count in occurrences.items():
                print(f"{value}: {count} lần xuất hiện")
        elif choice == 9:
            decreasing_subsequences = find_decreasing_subsequences(lst)
            for subsequence in decreasing_subsequences:
                print("Đoạn con giảm liên tiếp:", subsequence)  
        elif choice == 0:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()










