# Program 1: Print a specific formatted string using \n
print("Twinkle, twinkle, little star,\n"
      "How I wonder what you are! \n"
      "Up above the world so high,\n"
      "Like a diamond in the sky.\n"
      "Twinkle, twinkle, little star,\n"
      "How I wonder what you are")



# Program 2: Accept first and last name and print in reverse order
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Your name in reverse order is:", last_name, first_name)



# Program 3: Calculate the area of a circle
import math as m
radius = float(input("Enter the radius of the circle: "))
area = m.pi * radius ** 2
print("The area of the circle is:", area)



# Program 4: Display first and last colors from a list
color_list = ["Red", "Green", "White", "Black"]
print("First color:", color_list[0])
print("Last color:", color_list[-1])



# Program 5: Compute n + nn + nnn
n = int(input("Enter a number: "))
n1 = int(str(n))
n2 = int(str(n) * 2)
n3 = int(str(n) * 3)
result = n1 + n2 + n3
print("Result of n + nn + nnn is:", result)



# Program 6: Generate list and tuple from comma-separated input
input_str = input("Enter comma-separated numbers: ")
number_list = input_str.split(',')
number_tuple = tuple(number_list)
print("List:", number_list)
print("Tuple:", number_tuple)



# Program 7: Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)



# Program 8: Swap two numbers entered by the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Before swapping: num1 =", num1, ", num2 =", num2)
temp = num1
num1 = num2
num2 = temp
print("After swapping: num1 =", num1, ", num2 =", num2)



# Program 9: Check if a number is odd or even
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



# Program 10: Check if a year is leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")




# Program 11:to find the euclidean distance between two points
p1 = input("Enter coordinates of point 1 (x1,y1): ")
p2 = input("Enter coordinates of point 2 (x2,y2): ")
p1 = p1.split(',')
p2 = p2.split(',')
distance = m.sqrt((float(p2[0]) - float(p1[0])) ** 2 + (float(p2[1]) - float(p1[1])) ** 2)
print("The Euclidean distance between the points is:", distance)



#Program 12: To check if 3 angles can form a triangle
angle1 = float(input("Enter first angle: "))    
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))
if angle1 + angle2 + angle3 == 180:
    print("The angles can form a triangle.")
else:
    print("The angles cannot form a triangle.")



#Program 13: To find the compound interest
principal = float(input("Enter the principal amount: "))    
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
compound_interest = principal * ((1 + rate / 100) ** time - 1)
print("The compound interest is:", compound_interest)   



#Program 14: To check if a number is prime
num = int(input("Enter a number to check if it is prime: "))
is_prime = True
for i in range(2, int(m.sqrt(num)) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1:
    print(num, "is a prime number.")    
else:
    print(num, "is not a prime number.")    



# Program 15: To find 1^2 + 2^2 + ... + n^2
n = int(input("Enter the number N:"))
for i in range (1,n+1):
    sum_of_squares = i**2
    sum_of_squares += sum_of_squares
print("The sum of squares from 1 to", n, "is:", sum_of_squares)