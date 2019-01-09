s=int(input("Enter upper limit: "))
for a in range(2,s+1):
    m=0
    for s in range(2,a//2+1):
        if(a%s==0):
          m=m+1
    if(m<=0):
        print(a)
