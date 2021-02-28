# Q-1) 

txt = "1234abcd"
txt = "1234abcd" [::-1]
print(txt)

#Q-2) 

def string_check(txt): 
  a = {"Upper_Case": 0, "Lower_Case":0}
  for i in txt: 
    if i.isupper(): 
      a["Upper_Case"]+=1
    elif i.islower(): 
      a["Lower_Case"]+=1
    else: 
      pass
  
  print("Input : ", txt)
  print("No. of Upper case characters : ", a["Upper_Case"], "No. of Lower case characters : ", a["Lower_Case"])

string_check("abcSdefPghijQkl")

# Q-3)

def unique(l):
  x = []
  for a in l: 
    if a not in x: 
      x.append(a)
  return x 

print(unique([1,2,2,3,3,4,4,5,5]))

# Q-4)

colors='red-orange-yellow-green-blue'
 
items=[n for n in colors.split('-')]
items.sort()
print('-'.join(items))

# Q-5) 

string = 'Hello world Practice makes man perfect'
new_string = string.upper()
print(new_string)

# Q-6) 

def sum(a,b): 
  s = int(a) + int(b)
  return s

num1 = "20"
num2 = "30"

final_sum = sum(num1, num2)

print(final_sum)

# Q-7) 

def length_of_string(str1, str2):
	if (len(str1) == len(str2)):
		print(str1)
		print(str2)

	elif (len(str1) < len(str2)):
		print(str2)
	
	else:
		print(str1)

stri1 = input(str("enter First String: "))
stri2 = input(str("enter Second String: "))

length_of_string(stri1, stri2)

#Q-8) 

def square(): 
  l = list()
  for i in range (1,21): 
    l.append (i**2)
  print(l)

square_list = tuple(square())
print(square_list)

# Q-9) 

def shownumber(limit):

  for i in range(0, limit):
    if i==0:
    print(i,end=" ")
    print("EVEN")

    elif i%2==0:
    print(i,end=" ")
    print("EVEN")

    else:
    print(i,end=" ")

    print("ODD")

print(shownumber(4))

# Q-10) 

# my_list = list(range(1,21))

# new_list = list(filter(lambda x: (x % 2 == 0), my_list))

# print(new_list)

# Q-11) 

# my_list = list(range(1,11))

# new_list = list(filter(lambda x: ( x % 2 == 0), my_list))
# new_list2 = list(map(lambda x : x**2, new_list)) 

# print(new_list2)

# Q-12) 

# try: 
#   numerator = int(input("Enter numerator: "))
#   denominator = int(input('Enter denominator: '))

#   result = numerator / denominator
#   print(result)

# except: 
#   print("Denominator cannot be 0. Please try again")

# print("Program Ends.")

#Q-13) 

# import operator
# from functools import reduce

# list = [1,2,3,4,5,6,7,8]

# joinedlist = reduce(lambda a,d: 10*a+d, list)
# print(joinedlist)

# Q-14) 

n = 1000
l = list(range(1,n))
list = []

for x in l: 
  if (x%3 == 0) and (x%7 ==0): 
    list.append(str(x))
print(",".join(list))


#Q-15)

# my_list = [1,2,3,4,5]

# final_list = list(map(lambda x: x*x, my_list))
# print(final_list)

# Q-16) 

# def foo(): 
#   try: 
#     return 1
#   finally: 
#     return 2
#   k = foo()
#   print(k)

# def a():
#   try: 
#     f(x,4)
#   finally: 
#     print('after f')
#     print('after f?')
#   a() 




