# Dict
# 1. Convert two lists into a dictionary
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
dict_from_lists = dict(zip(list1, list2))
print("Dictionary from two lists:", dict_from_lists)

# 2. Merge two Python dictionaries into one
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

# 3. Print the value of key ‘history’ from the below dict
dict_example = {'math': 90, 'science': 85, 'history': 88}
history_value = dict_example.get('history', 'Key not found')
print("Value of key 'history':", history_value)

# 4. Initialize dictionary with default values
default_dict = dict.fromkeys(['a', 'b', 'c'], 0)
print("Dictionary with default values:", default_dict)

# 5. Create a dictionary by extracting the keys from a given dictionary
dict_to_extract = {'a': 1, 'b': 2, 'c': 3}
keys_extracted = dict.fromkeys(dict_to_extract.keys(), 0)
print("Dictionary with extracted keys:", keys_extracted)

# 6. Delete a list of keys from a dictionary
keys_to_delete = ['a', 'b']
dict_to_modify = {'a': 1, 'b': 2, 'c': 3}
for key in keys_to_delete:
    dict_to_modify.pop(key, None)
print("Dictionary after deleting keys:", dict_to_modify)

# 7. Check if a value exists in a dictionary
value_to_check = 2
dict_to_check = {'a': 1, 'b': 2, 'c': 3}
is_value_present = value_to_check in dict_to_check.values()
print(f"Is value {value_to_check} present in the dictionary? {is_value_present}")

# 8. Rename key of a dictionary
dict_to_rename = {'a': 1, 'b': 2}
old_key = 'a'
new_key = 'x'
if old_key in dict_to_rename:
    dict_to_rename[new_key] = dict_to_rename.pop(old_key)
print("Dictionary after renaming key:", dict_to_rename)

# 9. Get the key of a minimum value from the following dictionary
dict_min_value = {'a': 3, 'b': 1, 'c': 2}
min_key = min(dict_min_value, key=dict_min_value.get)
print("Key of minimum value:", min_key)

# 10. Change value of a key in a nested dictionary
nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3}}
nested_dict['a']['b'] = 10
print("Nested dictionary after changing value:", nested_dict)

# 11. Counts the number of times characters appear in a text paragraph.
text = "Hello World! Hello Python!"
char_count = {}
for char in text:
    if char.isalnum():  # Count only alphanumeric characters
        char_count[char] = char_count.get(char, 0) + 1

print("Character count:", char_count)

# 12. Using a dictionary containing keys starting from 1 and values ​​containing prime numbers less than a value N.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True 

num = 20
prime_dict = {i: i for i in range(1, num + 1) if is_prime(i)}
print("Dictionary of prime numbers:", prime_dict)

# 13. Restructuring the company data
# Sample employee data
employees = {
    101: {'name': 'Alice', 'department': 'HR', 'salary': 50000},
    102: {'name': 'Bob', 'department': 'IT', 'salary': 60000},
    103: {'name': 'Charlie', 'department': 'HR', 'salary': 55000},
    104: {'name': 'David', 'department': 'Finance', 'salary': 70000}
}

dept_employees = {}
for emp_id, emp_info in employees.items():
    dept = emp_info['department']
    if dept not in dept_employees:
        dept_employees[dept] = []
    dept_employees[dept].append({'name': emp_info['name'], 'salary': emp_info['salary']})

print("Nested dictionary of employees by department:", dept_employees)