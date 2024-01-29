#calling a function 

# def my_function():
#     print("hello world")

# my_function()


#with arguments

# def name(fname):
#     print(fname +" world")

# name("mine")
# name("beautiful")

#arbitatry arguments

# def name(*kids):
#     print("heyy "+kids[2])

# name("bro","boii","brother")

# #keyword arguments
# def child(child3,child2,child1):
#     print("the youngest child is "+child2)

# child(child1="rajat",child2="megha",child3="adi")


#default parameters

# def sum(a,b=4):
#     print(a+b)

# sum(1)


#passing lists as arguments
# def my_function(food):
#     for x in food:
#      print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

#return statement
# def mul(x):
#     return 3*x
# print(mul(3))



# def add(a,b):
#     c = a+b

#     return c


# c= add(5,8)

# def sub(c,d):
#      e = c - d
#      print(e)
#      return e


# sub(c,5)


def abc(a):
     if a > 5:
          return 1
     else:
          return 0
     
     

rajath = abc(4)

print(rajath)