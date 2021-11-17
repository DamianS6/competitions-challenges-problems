# https://www.codingame.com/ide/puzzle/power-of-thor
# 10.11.2021 - solution ranked 3991/33214

l,m,t,u=map(int,input().split())
s=print
while 1:
 if(l<t)*(m>u):s("SW");u+=1
 elif l<t:s("W")
 elif m<u:s("N")
 elif m>u:s("S");u+=1
 else:s("E")