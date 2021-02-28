# Q-1) 

try:  
  print("a/b")
except SyntaxError:
  print("Please check the Syntax" ) 

#Q-2) 

import sys

with open(sys.argv, 'r') as my_file:
    print(my_file.read())

#Q-3) 

length = None

while length is None: 
 
  try: 
    length = input("Please enter the digits")
  except: 
    print("Please enter the numbers") 

if len(length) != 4: 
  print("The length is short/long!!! Please provide only four digits")
else: 
  print("You are good. ")

#Q-4) 

count=0

while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Jayraj1122' and username=='Jayraj':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1

# Q-6) 

f = open("doc.txt", "r")

content = f.read()
print(content)

f.close()






