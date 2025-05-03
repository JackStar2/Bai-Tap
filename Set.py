# Set
# 1. Write a Python program to find the maximum and minimum values in a set.
numbers_set = {1, 2, 3, 4, 5}
max_value = max(numbers_set)
min_value = min(numbers_set)
print("Maximum value in the set:", max_value)
print("Minimum value in the set:", min_value)

# 2. Write a Python program to check if a given value is present in a set or not.
value_to_check = 3
is_present = value_to_check in numbers_set
print(f"Is {value_to_check} present in the set? {is_present}")

# 3. Write a Python program to check if two given sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
no_common_elements = set1.isdisjoint(set2)
print(f"Do set1 and set2 have no elements in common? {no_common_elements}")

# 4. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
words_list = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
unique_words = set(words_list)
word_count = {word: words_list.count(word) for word in unique_words}
print("Unique words and their frequency:", word_count)

# 5. Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
missing_in_b = set_a - set_b
missing_in_a = set_b - set_a
print("Missing in set_b compared to set_a:", missing_in_b)
print("Missing in set_a compared to set_b:", missing_in_a)