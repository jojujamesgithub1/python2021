upper=int(input("enter the upper limit"))
lower=int(input("enter the lower limit"))
sum=0
for i in range(lower,upper+1):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if (flag==0):
        sum-sum+i
print("sum of prime numbers:",sum)
