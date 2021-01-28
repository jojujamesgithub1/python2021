#print  even  and odd no from upper nd low limits
low=int(input("enter no low limit"))
up=int(input("enter no limit"))
for i in range(low,up):
    if(i%2==0):
        print("the even numbers are",i)
    else:
        print("the odd numbers are:",i)