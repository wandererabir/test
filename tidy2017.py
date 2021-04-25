c=int(input())
for cc in range(c):
    n,b=input().split()
    a=list(map(int,input().split(' ')))
    a.sort()
    s=0
    count=0
    for i in range(len(a)):
        if s+a[i]>int(b):
            break
        s+=a[i]
        count+=1
        
    print("Case #{}: {}".format(cc+1,count))
        

  
    