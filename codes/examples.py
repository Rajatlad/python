# #1)Python program to interchange first and last elements in a list

# # list1=[1,2,3,4]
# # print(list1)
# # #list2=[]
# # #list2[1]=list1[0]
# # list1[0]=list1[3]
# # list1[3]=list1[0]

# # print(list1)


# #2)Python program to swap two elements in a list

# list1=[2,3]
# x=list1[0]
# list1[0]=list1[1]
# list1[1]=x
# print(list1)




# #3)Maximum of two numbers in Python


# a=5
# b=55
# if a>b:
#     print("a is greater ")
# else:
#     print("b is greater")    


# #4)Minimum of two numbers in Python
    
# a=10
# b=5
# if a<b:
#     print("a is smaller")
# else:
#     print("b is smaller")    




# #5)Python program to check whether number is even or odd
    
# a=int(input("enter the number"))

# if (a)%2==0:
#         print("the number is even")
# else:
#         print("the number is odd")    



# #6)Python program to find the area of a triangle whose sides are given
        
# hieght=input("enter the hieght of the traingle")
# base=input("enter the base of the triangle")
# area=1/2*int(hieght)*int(base)
# print(area)




# #7)Python program to find out the average of a set of integers

# a=1
# b=3
# c=5
# average=a+b+c/3
# print(average)


# 8)Python program to check whether the given integer is a multiple of 5 and 7
        
# a=int(input("enter the number"))
# if a%5==0:
#     print("the number is multiple of 5")
# elif a%7==0:
#     print("it is multiple of 7")
# else:
#     print("it is not multiple of 5 and 7")



# 9)Python program to display the given integer in a reverse manner
    
# a=int(input("enter the number"))
# sum=0
# while a>0:
    
#     rem=a%10
#     a=a//10
#     sum=sum*10+rem
# print(sum)

#Python program to display all the multiples of 3 within the range 10 to 50

# for a in range(10,50):
#     if a%3==0:
#         print(a)
4
4

#swaping without 3rd var
# a=5
# b=10
# a,b=b,a
# print(a,b)

#2nd min
# list=[]4
# n=int(input("enter the number"))
# for i in range(0,n):
#     ele=int(input())
#     list.append(ele)
# #print(list)

# list.sort()
# #print(list)

# print(list[-2])


#sum of sum array

# list=[]
# sum=0
# n=int(input("enter the number"))
# for i in range(0,n):
#     ele=int(input())
#     list.append(ele)
# print(list)
# for x in list:
#     sum=sum+x
# print(sum) 



#largest element in an array

# list=[]
# n=int(input("enter the number"))
# for i in range(0,n):
#     ele=int(input())
#     list.append(ele)
# print(list)    
# list.sort()
# print(list)
# print("the max elemnet is",list[-1])


#reverse element in array
# list=[]
# n=int(input("enter the number"))
# for i in range(0,n):
#     ele=int(input())
#     list.append(ele)
# print(list)  
# list.reverse()
# print(list)


#palindrome  

# str=input("enter the string:")
# print(str)
# str1=str[::-1]
# if str1==str:
#     print("is palindrome")
# else:
#     print("is not a palindrome")


#palindrome using function
# def is_palindrome(str):
 
    
#     str1=str[::-1]
#     if str1==str:
#         print(str1)
#         print("palindrome")
#         return 1
#     else:
#         print("not a palindrome")    
#         return 0

# is_palindrome(input("enter the string ")) 






#reverse elements in list

# list=[1,2,3,4]
# print(list)
# list1=list[::-1]
# print(list1)


#factorial
# n=int(input("enter the value"))
# fact=1
# while n>0:
#  fact=fact*(n)
#  n-=1
# print("the factorial of number is :",fact)



#armstrong number

# n=int(input("enter the number"))
# new=n
# sum=0
# while new >0:
#  rem=new%10
#  sum=sum+(rem*rem*rem)
#  new=new//10
# if sum==n:
#     print("it is an armstrong no")
# else:
#     print("it is not an armstrong no")



# prime number
# n=int(input("enter the number"))
# for i in range(2,int(n**0.5)+1):
#      if n%i==0:
#         print("not a prime ")
#         break
# else:
#   print("it is a prime")


 #Write a Python program to find the common elements between two lists.

# list=[3,2,6,4]
# list1=[1,2,5,6]
# list2=[]
# for i in list:
#     if i in list1:
#         list2.append(i)
#         print(list2)

#Write a Python program to count the frequency of each element in a list.

# list=[1,2,3,4,1,2,4,5]
# count={}
# for i in list:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)


#Write a Python program to remove duplicates from a list.

# a=[1,2,3,2,4,5,2,4,7]
# result=[]
# for i in a:
#     if i not in result:
#         result.append(i)
# print(result)        


#check if two strings are anagram

# def anagram(s1,s2):
#     s1=sorted(s1)
#     s2=sorted(s2)
#     if s1==s2:
#         print("the two strings are anagram")
#     else:
#         print("not anagram")
# s1=input("enter the string1")
# s2=input("enter the string2")
# anagram(s1,s2)

#fibonacii series

# def fib(n):
#     a=0
#     b=1
    
#     if n==1:
#         print(a)

#     elif n<0:
#        print("invalid input")
       
#     else:    
#       print(a)
#       print(b)
#       for i in range(2,n):
#         sum=a+b
#         a=b
#         b=sum
#         print(sum)
# print("enter the no:")        
# fib(int(input()))


#star printing

# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print(i*'*')
#     i=i+1


# i=int(input("enter the number"))

# while i>0:
#     print(i*'*')
#     i=i-1
    
#using for loops

# def myfunc(n):
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print("* ",end=" ")
#         print("\r")

# n = 5
# myfunc(n)

# def myfunc(n):
#     num=1
#     for i in range(0, n):
#         #num=1
#         for j in range(0, i+1):
#             print(num,end=" ")
#             num=num+1
#         print("\r")

# n = 5
# myfunc(n)


a=int(input("enter the side"))
b=int(input("enter the side"))
print(a>=b)
