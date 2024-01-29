x=input("enter the 1st value\n")
y=input("enter the 2nd value\n")
z=input("enter the command\n")

if z=="+":
    print(int(x)+int(y))

elif z=="-":
    print(int(x)-int(y))
  
elif z=="div":
    print(int(x)/int(y)) 

elif z=="mul":
    print(int(x)*int(y)) 

else:
    print("invalid command")