# # Q-1) 

# C = 50 
# H = 30

# import math

# numbers = input("Provide D: ")
# numbers = numbers.split(',')

# result = []
# for D in numbers:
#     Q = round(math.sqrt(2 * C * int(D) / H))
#     result.append(Q)

# print(result)

# # Q-2) 

# class Shape(object):
#     def __init__(self):
#         pass

#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, l):
#         Shape.__init__(self)
#         self.length = l

#     def area(self):
#         return self.length*self.length

# Square_a= Square(3)
# print (Square_a.area())

# # Q-3) 

# def findNumbers(arr, n):
 
#     found = False
#     for i in range(0, n-2):
     
#         for j in range(i+1, n-1):
         
#             for k in range(j+1, n):
             
#                 if (arr[i] + arr[j] + arr[k] == 0):
#                     print(arr[i], arr[j], arr[k])
#                     found = True
     
#     if (found == False):
#         print(" not exist ")
 

# arr = [-25,-10,-7,-3,2,4,8,10]
# n = len(arr)
# findNumbers(arr, n)

# # Q-4) 

# class Time():

# 	def __init__(self, hours, mins):
# 		self.hours = hours
# 		self.mins = mins

# 	def addTime(t1, t2):
# 		t3 = Time(0,0)
# 		if t1.mins+t2.mins > 60:
# 			t3.hours = (t1.mins+t2.mins)/60
# 		t3.hours = t3.hours+t1.hours+t2.hours
# 		t3.mins = round((t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60))
# 		return t3

# 	def displayTime(self):
# 		print ("Time is",self.hours,"hours and",self.mins,"minutes.")

# 	def displayMinute(self):
# 		print((self.hours*60)+self.mins, "minutes")

# a = Time(2,50)
# b = Time(1,20)
# c = Time.addTime(a,b)
# c.displayTime()
# c.displayMinute()

# Q-5) 

class Person: 

  def __init__(self, initialAge): 
    if(initialAge < 0): 
      print("Age is not valid, setting age to 0.")
      self.age = 0 
    else: 
      self.age = initialAge
  
  def amIOld(self): 
    if(self.age < 13): 
      print("You are young.")
    elif(self.age >=13 and self.age < 18): 
      print("You are a teenager.")
    else: 
      print("You are old.")
  
  def yearPasses(self): 
    self.age += 1
  

t = int(input())

for i in range (0, t): 
  age = int(input())
  p = Person(age)
  p.amIOld()
  for j in range(0,3): 
    p.yearPasses()
  p.amIOld()
  print("")