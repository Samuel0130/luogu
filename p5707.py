m,n =map(int,input().split())
minute =8*60-10+24*60
if m%n ==0:
    time = m//n
else:
    time = m//n+1
minute = minute-time
H = minute//60
M = minute%60
if H>=24:
    H-=24
# if H<10 and M<10:
#     print('0{}:0{}'.format(H,M))
# elif H<10 and M>10:
#     print('0{}:{}'.format(H,M))
# elif H>10 and M<10:
#     print('{}:0{}'.format(H,M))
# else:
#     print('{}:{}'.format(H,M))
print('{}:{}'.format('%.2d'%H,'%.2d'%M))