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

#remove item 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(y)

#add item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)


#unpacking a tuple
fruits=("apple","cherry","mango")
(green,red,yellow)=fruits
print(green)
print(red)
print(yellow)