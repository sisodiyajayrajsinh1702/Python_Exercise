# Q-1) 

string = " My Name Is Jayrajsinh Sisodiya"
print("The original string is: " + str(string))

result = [i for i in string if i.isupper()]
print("The upper case characters in string are : " + str(result))

# Q-2) 

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

D = { k:v for (k,v) in zip(students, subjects)}
print(D)

# Q-4)

def reverse_string(my_str): 
  my_str = "".join(reversed(my_str))
  return my_str

Input = ("Consultadd Training")

print("The original string is: ", Input)
print("The reversed string is: ", reverse_string(Input))

# Q-5) 

def add(x, y):
  return x + y

def inc(func, x, y): 
  result = func(x, y)
  return result

print(inc(add, 3, 4)) 



