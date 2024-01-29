set={"rajat","lad","me"}
print(len(set))
for x in set:
    print(x)
print("rajat" in set)

#add items in set

set1={"bat","cat","dog"}
print(set1)
set1.add("ball")
print(set1)

#add 2 sets
one={"lion","tiger","deer"}
two={"eagle","owl","peacock"}
two.update(one)
print(two)


#remove item from set
one={"lion","tiger","deer"}
one.remove("lion")
print(one)


#clear set
one={"lion","tiger","deer"}
one.clear()
print(one)


#delete set
one={"lion","tiger","deer"}
print(one)
del one

#join to set union
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#intersection
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3,'a'}
set3 = set1.intersection(set2)
print(set3)


#Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)