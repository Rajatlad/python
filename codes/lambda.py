x= lambda a:a+5
print(x(4))

#multiple argumnets
x=lambda a,b,c: a+b+c
print(x(1,2,3))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))