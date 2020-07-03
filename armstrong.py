n=int(input("enter a number"))
sum=0
t=n
c=0
while(t>0):
    c=c+1
    t=t//10
t=n

while(t>0):
    d=t%10        
    sum=sum+d**c  
    t=t//10       
print(sum)

if(n==sum):
    print(n,"its a armstrong number")
else:
    print(n,"Its not armstrong number")
