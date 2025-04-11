import math

def calculate_triangle_area():
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    area = 0.5 * base * height
    print("Area of the triangle:", area)

def calculate_triangle_perimeter():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    perimeter = a + b + c
    print("Perimeter of the triangle:", perimeter)

def calculate_rectangle_properties():
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print("Area of the rectangle:", area)
    print("Perimeter of the rectangle:", perimeter)

def calculate_circle_properties():
    radius = float(input("Enter radius of the circle: "))
    pi = 3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    print("Area of the circle:", area)
    print("Circumference of the circle:", circumference)

def analyze_line():
    slope = 2
    y_intercept = -2
    x_intercept = y_intercept / -slope
    print("Slope:", slope)
    print("x-intercept:", x_intercept)
    print("y-intercept:", y_intercept)

def slope_and_distance():
    x1, y1 = 2, 2
    x2, y2 = 6, 10
    slope = (y2 - y1) / (x2 - x1)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Slope between points:", slope)
    print("Euclidean distance between points:", distance)
    return slope

def compare_slopes():
    slope1 = 2
    slope2 = slope_and_distance()
    print("Slopes equal:", slope1 == slope2)

def find_y_zero():
    for x in range(-10, 11):
        y = x**2 + 6*x + 9
        print(f"When x = {x}, y = {y}")
        if y == 0:
            print(f"y is 0 when x = {x}")

def compare_word_lengths():
    len_python = len("python")
    len_dragon = len("dragon")
    print("Falsy comparison (lengths not equal):", len_python != len_dragon)

def check_substring_on():
    print("'on' in both 'python' and 'dragon':", 'on' in 'python' and 'on' in 'dragon')

def check_jargon():
    sentence = "I hope this course is not full of jargon."
    print("'jargon' in sentence:", 'jargon' in sentence)

def convert_length():
    length = len("python")
    float_val = float(length)
    str_val = str(float_val)
    print("Float:", float_val)
    print("String:", str_val)

def is_even():
    num = int(input("Enter a number to check if it's even: "))
    print("Is even:", num % 2 == 0)

def calculate_pay():
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate per hour: "))
    pay = hours * rate
    print("Total pay:", pay)

def seconds_lived():
    years = int(input("Enter number of years you expect to live: "))
    seconds = years * 365 * 24 * 60 * 60
    print("You can live about", seconds, "seconds")

if __name__ == "__main__":
    #calculate_triangle_area()
    #calculate_triangle_perimeter()
    #calculate_rectangle_properties()
    #calculate_circle_properties()
    #analyze_line()
    #compare_slopes()
    #find_y_zero()
    #compare_word_lengths()
    #check_substring_on()
    #check_jargon()
    #convert_length()
    #is_even()
    #calculate_pay()
    #seconds_lived()
    pass
