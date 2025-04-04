#41. Strip a set of characters from a string
def strip_characters(string, chars):
    return string.strip(chars)


string = "Hello, World!"
chars = "!"
modified_string = strip_characters(string, chars)
print(f"Modified string: {modified_string}")

#42. Count repeated characters in a string
def count_repeated_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return {char: count for char, count in char_count.items() if count > 1}
# Sample string
string = "thequickbrownfoxjumpsoverthelazydog"
repeated_chars = count_repeated_characters(string)
print(f"Repeated characters in '{string}': {repeated_chars}")

#43. Print the square and cube symbols in the area of a rectangle and the volume of a cylinder
def print_area_volume(area, volume):
    print(f"The area of the rectangle is {area:.2f}cm²")
    print(f"The volume of the cylinder is {volume:.3f}cm³")
   
area = 1256.66
volume = 1254.725
print_area_volume(area, volume)

#44. Print the index of a character in a string
def print_character_index(string):
    for index, char in enumerate(string):
        print(f"Current character '{char}' position at {index}")

string = "w3resource"
print_character_index(string)

#45. Check whether a string contains all letters of the alphabet
def contains_all_letters(string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(string.lower()))

string = "The quick brown fox jumps over the lazy dog"
contains_all = contains_all_letters(string)
print(f"Does '{string}' contain all letters of the alphabet? {contains_all}")

#46. Convert a given string into a list of words
def convert_string_to_list(string):
    return string.split()

string = "The quick brown fox jumps over the lazy dog."
word_list = convert_string_to_list(string)
print(f"List of words: {word_list}")

#47. Lowercase the first n characters in a string
def lowercase_first_n(string, n):
    return string[:n].lower() + string[n:]

string = "Hello, World!"
n = 5
modified_string = lowercase_first_n(string, n)
print(f"Modified string: {modified_string}")

#48. Swap commas and dots in a string
def swap_commas_dots(string):
    return string.replace(",", "temp").replace(".", ",").replace("temp", ".")

string = "32.054,23"
modified_string = swap_commas_dots(string)
print(f"Modified string: {modified_string}")

#49. Count and display vowels in text
def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = {vowel: string.count(vowel) for vowel in vowels}
    return {vowel: count for vowel, count in vowel_count.items() if count > 0}

string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"Vowel count in '{string}': {vowel_count}")

#50. Split a string on the last occurrence of the delimiter
def split_on_last_occurrence(string, delimiter):
    parts = string.rsplit(delimiter, 1)
    return parts if len(parts) > 1 else [string]
string = "Hello, World! Hello, Python!"
delimiter = "Hello"
modified_string = split_on_last_occurrence(string, delimiter)
print(f"Modified string: {modified_string}")
