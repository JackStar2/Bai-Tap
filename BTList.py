def sumAll(list): 
    total = 0
    for i in list:
        total += i 
    return total 

def mulAll(list):
    total = 1
    for i in list:
        total *= i
    return total

def largestNum(list):
    max = 0
    for i in list:
        if i > max:
            max = i 
    return max

def smallestNum(list):
    min = list[0]

    for i in list:
        if i < min:
            min = i
    return min

def count_strings_with_same_ends(string_list):
    count = 0
    for string in string_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

def remove_duplicates(input_list):
    return list(set(input_list))

def is_list_empty(input_list):
    return len(input_list) == 0

def clone_list(input_list):
    return input_list.copy()

def words_longer_than_n(words_list, n):
    return [word for word in words_list if len(word) > n]

def have_common_member(list1, list2):
    return any(item in list1 for item in list2)

def remove_elements(input_list, indices_to_remove):
    return [item for index, item in enumerate(input_list) if index not in indices_to_remove]

def generate_3d_array(dimensions):
    return [[[ '*' for _ in range(dimensions[2])] for _ in range(dimensions[1])] for _ in range(dimensions[0])]

def remove_even_numbers(input_list):
    return [num for num in input_list if num % 2 != 0]

def shuffle_list(input_list):
    import random
    random.shuffle(input_list)
    return input_list

def generate_square_numbers(start, end):
    return [i**2 for i in range(1, int(end**0.5) + 1) if i**2 >= start and i**2 <= end]

def are_all_prime(numbers_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return all(is_prime(num) for num in numbers_list)

def generate_permutations(input_list):
    from itertools import permutations
    return list(permutations(input_list))

def calculate_difference(list1, list2):
    return list(set(list1) - set(list2))

def access_index(input_list, index):
    return input_list[index] if 0 <= index < len(input_list) else None

def list_to_string(input_list):
    return ''.join(input_list)

def find_index(input_list, item):
    try:
        return input_list.index(item)
    except ValueError:
        return -1
    
def flatten_list(input_list):
    return [item for sublist in input_list for item in sublist]

def append_list_to_second_list(list1, list2):
    list2.extend(list1)
    return list2

def select_random_item(input_list):
    import random
    return random.choice(input_list)

def are_lists_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    return any(list1 == list2[i:] + list2[:i] for i in range(len(list2)))

def find_second_smallest(input_list):
    unique_list = list(set(input_list))
    unique_list.sort()
    return unique_list[1] if len(unique_list) > 1 else None

def find_second_largest(input_list):
    unique_list = list(set(input_list))
    unique_list.sort(reverse=True)
    return unique_list[1] if len(unique_list) > 1 else None

def get_unique_values(input_list):
    return list(set(input_list))

def get_frequency(input_list):
    from collections import Counter
    return dict(Counter(input_list))

if __name__ == '__main__':
    n = int(input("Number of elements: "))
    num_list = []
    import random

    for i in range(random.randint(1,n)):
        num_list.append(random.randint(1,n))
   
    # print(num_list)
    # print(sumAll(num_list))
    # print(mulAll(num_list))
    # print(largestNum(num_list))
    # print(smallestNum(num_list))    
    # print(count_strings_with_same_ends(["abc", "xyz", "aba", "1221"]))
    # print(sort_by_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
    # print(remove_duplicates([1, 2, 3, 3, 3, 4, 5]))
    # print(is_list_empty([]))
    # print(clone_list([1, 2, 3, 4, 5]))
    # print(words_longer_than_n(["hello", "world", "python", "is", "awesome"], 3))
    # print(have_common_member([1, 2, 3], [3, 4, 5]))
    # print(remove_elements([1, 2, 3, 4, 5], [0, 2]))
    # print(generate_3d_array((2, 3, 4)))
    # print(remove_even_numbers([1, 2, 3, 4, 5, 6]))
    # print(shuffle_list([1, 2, 3, 4, 5]))
    # print(generate_square_numbers(10, 100))
    # print(are_all_prime([2, 3, 5, 7]))
    # print(generate_permutations([1, 2, 3]))
    # print(calculate_difference([1, 2, 3], [2, 3, 4]))
    # print(access_index([1, 2, 3, 4, 5], 2))
    # print(list_to_string(['H', 'e', 'l', 'l', 'o']))
    # print(find_index([1, 2, 3, 4, 5], 3))
    # print(flatten_list([[1, 2], [3, 4], [5]]))    
    # print(append_list_to_second_list([1, 2, 3], [4, 5]))
    # print(select_random_item([1, 2, 3, 4, 5]))
    # print(are_lists_circularly_identical([1, 2, 3], [3, 1, 2]))
    # print(find_second_smallest([1, 2, 3, 4, 5]))





