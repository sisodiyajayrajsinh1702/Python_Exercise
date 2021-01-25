# 1.) Write a program in Python to perform the following operation:

# If a number is divisible by 3 it should print “Consultadd” as a string
a = 15

if(a % 5 == 0):
    print('Consultadd')

# If a number is divisible by 5 it should print “Python Training” as a string
b = 15
if(b % 5 == 0):
    print('Python Training')

# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.
c = 45

if(c % 5 == 0) and (c % 3 ==0):
    print('Consultadd - Python Training')

# 2.) Write a program in Python to perform the following operator based task:

# Take input from the user
choice = input("Enter choice(1/2/3/4/5): ")

# Check if choice is one of 5 options
if choice in('1', '2', '3', '4', '5'):
    num1 = float(input("Enter first num: "))
    num2 = float(input("Enter second num: "))

    result = 0
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 / num2
    elif choice == '4':
        result = num1 * num2
    elif choice == '5':
        result = (num1 + num2) / 2

     print(result)

3.) Write a program in Python to implement a flowchart.

a = 10
b = 20
c = 30

avg = (a+b+c)/3
print("avg = ", avg)

if (avg > a) and (avg > b) and (avg > c):
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif (avg > a) and (avg > b):
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif (avg > a) and (avg > c):
    print("%d is higher than %d, %d" %(avg, a, c))
elif (avg > b) and (avg > c):
    print("%d is higher than %d, %d" %(avg, b, c))
elif (avg > a):
    print("%d is just higher than %d" %(avg, a))
elif (avg > b):
    print("%d is just higher than %d" %(avg, b))
elif (avg > c):
    print ("%d is just higher than %d" %(avg, c))

#4.) Write a program in Python to break and continue if the following cases occurs:

while True:
    number = float(input('Enter the number : '))
    if number < 0:
        print("It's Over")
        break
    print("Good Going")

# 5.) Write a progam that will find all the numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200.

nl = []
for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print(','.join(nl))


#6.) What is the output of following code

# x = 123
#     for i in x:
#         print(i)

# Ans - It will provide an error because we should use while loop instead of for loop.
#
# i = 0
#     while i<5:
#         print(i)
#         i += 1
#         if i == 3:
#             break
#         else
#             print("error")
#
# Ans - It will provide an error because we should use For loop instead of while loop.

# count = 0
#
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break
#
# Ans - It will throw an error as 'break' should be used instead of 'Break'

#7.) Print al numbers from 0 to 6 except 3 and 6.

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")

#8.) Accept all string as an input from the user and calculate number of digits and and letters.

Input = input("Enter the string")

d=l=0

for c in Input:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass
print("Letters", l)
print("Digits", d)

#9.)
# Guess the lucky number

number = input("Guess the lucky number ")
while number != 5:
   print ("That is not the lucky number")
   number = input("Guess the lucky number ")

# Guess again each time

number = -1
again = "yes"
while number != 5 and again != "no":
    number = input("Guess the lucky number: ")
    if number != 5:
        print ("That is not the lucky number")
        again = input("Would you like to guess again? ")

#10.) Ask 5 times to guess lucky numbers

counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 5:
       print ("Try again.")
   else:
       print ("Good guess!")
   counter = counter +1
else:
   print ("Game over")














