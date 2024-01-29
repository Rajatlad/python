"""
first=input("enter the number:")
second=input("enter the number:")
sum=int(first)+int(second)
print(sum)
"""

a="me"
A="raw"
print(a)
print(A)

x,y,z="kle","me","food"
print(x,y,z)
print(y)
print(z)

x=y=z="fruits"
print(x,y,z)


fruits=["apple\n","banana","papaya"]
x,y,z=fruits
print( x,y,z)
x=5
y="me"
print(x,y)

#global variable declaration
x="awesome"
def myfun():
    print("python is " + x)
myfun()


x = "awesome"
def myfunc():
  #local variable
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#------------------------------------------------------------------------------

#global keyword
def myfunc():
  #local variable
 global x
 x = "fantastic"
myfunc()

print("Python is " + x)

#to identify type of data use type()
x=1j
print(type(x))

x=tuple(("bat","rat","ball"))
print(type(x))
    



x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#random number
import random
print(random.randrange(1,10))


#strings
a="rajat"
print(a[2]) #accesing character from string 

#looping in strings
for x in "rajat":
   print(x)

#string length"
   a="rajat"
   print(len(a))

#in keyword
a="python is good"
print("is" in a)

a="today is a long day"
if 'long' in a:
 print("yes,long is present")
else:
  print("no,it is not present")

#upper case
a="rajat"
print(a.upper())

#lower case
a="RAJAT"
print(a.lower())

#replace string

a="rajat"
print(a.replace("j","p"))

#split string
a="rajat, lad,hubli"
print(a.split(","))

#if-else statements
"""
age=input("enter your age\n")

if int(age)>=18:
  print("u are an adult")
  print("u can vote")

elif int(age)<18 and int(age)>5:
  print("u are in school")

else:
  print("u are a child")
"""
#-------------------------------------------------------------"

#loops
  #while loop

i=1
while i<=5:
  print(i)
  i=i+1

i=5
while i>0:
  print(i)
  i=i-1

#star printing 
  #low to high
i=1
while i<=5:
  print(i*"*")
  i=i+1

 #high to low
i=5
while i>0:
  print(i*"*")
  i=i-1

#for loop

for i in range(5):
    print(i)


#---------------------------------------------
    #list in python

marks=[98,91,96]
marks[1]=90 #insert ele in list at pos 1
print(marks)
print(len(marks))
print(marks[0:2])
print(marks[:2])
print(marks[1])
print(marks[-1])

#loops in list

marks=[20,30,40]
marks.append(50)
marks.insert(0,10)
print(marks)
#for loop
for scores in marks:
  print(scores)


  #while loop
marks=[20,30,40]
i=0
while i<len(marks):
  print(marks[i])
  i=i+1
  
marks.clear()
print(marks)


#extend list

animal=["lion","tiger","deer"]
print(animal)
birds=["peacock","eagle"]
print(birds)
animal.extend(birds)
print(animal)

#remove from list
animal.remove("tiger")
print(animal)

#remove from specified index
fruits=["banana","apple","watermelon"]
fruits.pop(1)
print(fruits)

#comprehension list

list=["pen","ball","bat"]
newlist=[x for x in list if 'a' in x]
print(newlist)
newlist=[x.upper() for x in list]
print(newlist)

#sorting of list

#ascending
item=["rajat","lad","python",'1']
num=[30,20,66,25]
item.sort()
num.sort()
print(num)
print(item)

#decending order
num=[30,20,66,25]
num.sort(reverse=True)
print(num)

#reverse the order of the list
num=[30,20,66,25]
num.reverse()
print(num)

#copy list
num=[30,20,66,25]
new=num.copy()
print(new)

#join in list

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#using extend function 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


# tuple is python

animal=("rat","bat","cat")
print(animal)
#can have duplicate ele
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#convert tuple into list
x=('a','b','c','d')
print(x)
y=list(x)
print(y)
y[1]='e'
x=tuple(y)
print(x)