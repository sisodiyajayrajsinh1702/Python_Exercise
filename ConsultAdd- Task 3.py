# Q-1) 

my_list = [1, 2, 3, 4, 5.5, 6.5, "Hello", "Jayraj", 2+3j, 4+ 5j]
print(my_list)


# Q-2) 

list_2 = [1, 2, 3, 4, 5]
print(list_2[2:4])

# Q-3) 

def multiply_list(list): 
  result = 1
  for i in list: 
    result = result * i 
  return result


def sum_list(list): 
  result = 1
  for i in list: 
    result = result + i 
  return result

list1= [1,2,3]
print("The multiplication of the list is: ", multiply_list(list1))
print("The sum of the list is: ", sum_list(list1))

# Q-4) 

list_2 = [10,20,30,40,50]

print("Largest element is: ", max(list_2))
print("Smallest element is: ", min(list_2))

#Q-5) 

list_3 = [11,22,33,44,55,66]

for i in list_3:
  if(i % 2 == 0): 
    list_3.remove(i)

print("list after removing Even numbers")
print(list_3)

# Q-6)

def square(): 
  l = list()
  for i in range(1,31): 
    l.append(i**2)
  print(l[:5])
  print(l[-5:])

square()

#Q-7) 

list_4 = [1,3,5,7,9,10]
list_5 = [2,4,6,8]

list_4[-1:] = list_5
print(list_4)

# Q-8)  

def merge(a, b): 
  return(a.update(b))

a = {1:10, 2:20}
b = {3:30, 4:40}

print(merge(b,a))
print(b)

# Q-9)

n=5
d = dict()

for x in range(1, n+1): 
  d[x] = x*x

print(d)

# Q-10)

values = input("Enter comma seprated numbers: ")

list_5 = values.split(",")
tuple = tuple(list_5)
print(list_5, tuple)
