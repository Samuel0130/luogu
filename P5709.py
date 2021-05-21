m,t,s = map(int,input().split())

if t==0:
    print(0)
if t!=0 and s%t !=0 :
    print(max(0,int(m-s//t-1)))
if t!=0 and s%t ==0:
    print(max(int(m-s//t),0))
