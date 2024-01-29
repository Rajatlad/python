fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#loop through string 

animal="lion"
for x in animal:
  print(x)

#break statement

fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i)
  if i=="apple":
    break
  
#continue

fruitsruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#nested loop
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
