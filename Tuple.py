# Tuple
# 1. Create a tuple of numbers and print one item.
numbers = (1, 2, 3, 4, 5)
print("First item in the tuple:", numbers[0])

# 2. Unpack a tuple into several variables.
a, b, c = numbers
print("Unpacked values:", a, b, c)

# 3. Add an item to a tuple.
new_numbers = numbers + (6,)
print("Tuple after adding an item:", new_numbers)

# 4. Find the index of an item in a tuple.
item_index = numbers.index(3)
print("Index of item 3 in the tuple:", item_index)

# 5. Find the repeated items of a tuple.
repeated_items = [item for item in set(numbers) if numbers.count(item) > 1]
print("Repeated items in the tuple:", repeated_items)