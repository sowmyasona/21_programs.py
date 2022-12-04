# id=int(input("your Id:"))
# name=input("Enter your Name:")
# salary=float(input("Enter your Salary:"))
# print("Your id is: {} , Name is: {} , Salary is: {}".format(id,name,salary))
# print(f"Your id is: {id} , Name is: {name} and Salary is: {salary}")

# a,b,c=[float(x) for x in input("Enter 3 Numbers:").split(',')]
# sum=a+b+c
# avg=sum/3
# print("The Sum is %.2f\nAverage is %.2f" %(sum,avg))

# r=float(input("Enter the Radius:"))
# PI=22/7
# Area=PI*r**2
# print("The Area of the Circle is %.2f" %Area)

# import math
# r=float(input("Enter the Radius:"))
# Area=math.pi*r**2
# print("The Area of the Circle is:%.2f" %Area)
# import math
# print(math.pi)

# c=(input("Enter a char:"))
# """we can perform it in 2 ways"""
# print("The Entered Character is: "+c[-1])
# print("The Entered Character is:",c[+1])

# s1,s2=input('Enter two Strings:').split(",")
# print(s1+s2)
# print(s1,s2,sep="&")

# n=float(input("Enter Any Number:"))
# print("Cube of the Number is:",n**3)

# import math
# a=float(input("Enter any Number: "))
# print(math.pow(a,3))

# v=int(input("Enter the ending value: "))
# for i in range(1,v+1):
#     print(i**3)

# sor=[]
# n=int(input("How many strings?"))
# for i in range(n):
#     s=input("Enter String:")
#     sor.append(s)
# sor.sort(reverse=True)
# print(sor)
# print(sor[::-1])
# print(*sor)
# for i in sor:
#     print(i)

# k=eval(input("Enter numbers:"))
# print(k,type(k))
# print(("Num=%f"%k))

# n=int(input("Enter a Number:"))
# if n%2==0:
#     print(f"{n} is Even Number")
# else:
#     print(f"{n} is Odd Number")

# n=int(input("Enter any Positive Number:"))
# if(n==0): print("The user entered {} Number".format(n))
# elif(n%2==0): print("The Number {} is Even Number".format(n))
# else: print("The number {} is Odd Number".format(n))

# n=int(input("Enter any number: "))
# for j in range(1,n+1):
#     print(j)

# a=1
# while(a<=10):
#     print(a)
#     a=a+1 

# m,n=[int(i) for i in input("Enter Start Value, Stop Value: ").split()]
# x=m
# if x%2!=0: x=m+1
# while(x<=n):
#     print(x)
#     x+=22

# m=int(input())
# n=int(input())
# for i in range(m,n,2):
#     print(i)

# for i in range(100,111):
#     print(i)

# a=range(100,111)
# for y in a:
#     print(y)

# m=int(input("Enter the value of m:"))
# n=int(input("Enter the value of n:"))
# while(m>=n):
#     print(m)
#     m-=1

# for i in range(100,111,2):
#     print(i)

# name="python"
# for n in name:
#     print(n)

# name="python"
# for n in name[ : : 2 ]:
#     print(n)

# m1=[5,10,15,20,25,30,35,67,65]
# c=0
# for i in m1:
#     c+=1
# print('No. of Elements present inside the lists is =',c)
# print(len(m1))

# import math
# a=[7,8,6]
# print(a[0]+a[1]+a[2])
# print('The Sum of all the lists is',math.fsum(m1))
# print('The Sum of all the lists is',math.fsum(a))
# print('The Sum of all the lists is',math.fsum(m1+a))
# print(sum(m1))
# print(sum(a))
# print(sum(m1+a))

# import math
# a,b,c,d=[float(x) for x in input().split()]
# y=a,b,c,d
# print(sum(y))
# print(int(math.fsum(y))) 
# print(math.fsum(y)) 
