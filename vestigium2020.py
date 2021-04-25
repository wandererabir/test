n=int(input())
for k in range(1,n+1):
 mat=[]
 c=0
 r=0
 su=0
 n1=int(input())
 for i in range(n1):
     a=list(map(int, input().split()))    
     mat.append(a)
 
 for i in range(n1):
     lstr=[]
     lstc=[]
     for j in range(n1):
         lstr.append(mat[i][j])
         lstc.append(mat[j][i])
         if (i == j): 
            su+= int(mat[i][j])
     sr=set(lstr)
     if len(sr)!=n1:
         r=r+1
     sc=set(lstc)
     if len(sc)!=n1:
         c=c+1
        
 print("Case #{}: {} {} {}".format(k,su,r,c))