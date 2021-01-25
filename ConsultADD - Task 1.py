# 1.) Create 3 Variables in a single line.
a, b, c = 1, 2.01, 'string'
print(a, b, c)

# 2.) Create a variable of type complex and swap it with another variable of type integer.
d = 1 + 2j
d = 5
print(d)

# 3.) Swap two numbers using a third variable and do the same task without using any third variable.

# Using 3rd variable

e = 15
f = 10

temp = e
e = f
f = temp

print("Swapping both the numbers using 3rd variables:")
print("Value of e: ", e)
print("Value of f: ", f)

# Without using 3rd variable

g = 45
h = 35

g = g + h
h = g - h
g = g - h

print("Swapping both the numbers without using 3rd variables:")
print("Value of g: ", g)
print("Value of h: ", h)

# 4.) Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.
# Ans: Skipped the question because the default version of PyCharm IDE is 3.9

# 5.) Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

i = int(input("Enter any number between 1 - 10 "))
j = int(input("Enter any number between 1 - 10 "))

z = i + j
z = z + 30

print("Final Output: ", z)

# 6.) Write a program to check the data type of the entered values.

k = 'Jayraj' # Assign any type of input value to variable "a" and code will execute the output.
print("The data type of the input value is : ", type(k))

# 7.) Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE

Value = 25 #Upper CamelCase
value = 35 #Lower CamelCase
value_01 = 45 #SnakeCase
VALUE = 55 #UPPERCASE

# 8.) If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?

l = 25
l = 'Jay'

print(l)

# Ans: Yes, variables in Python can be reassigned to a new value that is a different data type from its current value.
# In fact, variables can be reassigned to any valid value in Python, regardless of its current value.
# Variables are essentially like an empty box, that can contain something like a string, number, or other value.
# When you assign it a value, the box will contain that value, and when you reassign it, it will empty out the old value, and the new value will be placed inside of it.

