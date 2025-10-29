#armstrong number

num=int(input("enter the number :"))
sum=0
temp=num
while temp>0:
   digit =temp%10
   sum+=digit**3
   temp=temp//10
if sum==num:
    print("armstrong number")
else:
    print("not an armstrong number")


#sum of digits

num=int(input("enter the number:"))
sum=0
temp=num
while temp>0:
    digits=temp%10
    sum+=digit
    temp=temp//10
print("sum of digits :",sum)


#perfect numbers

number=int(input("enter the number:"))
sum=0
for i in range(1,number):    
  if (number %i++0):
    sum=sum+i
if (sum==number):
    print("%d is the perfect number"%number)
else:
    print("%d is not the perfect number"%number)

# facters

x=int(input("enter the number:"))
y=[]
print("the facters of",x,"are")
for i in range (i,x):
    if x %1==0:
        y.append(i)
print(y)
print("number of the facters:",len(y))
n=int(input("enter n value:"))
if n>len(y):
  print("invalid")
else:
    print("first",n,"factors:")
    for k in range (0,n):
        print(y[k],end="")
