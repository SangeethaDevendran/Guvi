cho,cha=map(int,input().split())
p=1
waht=0
while(p<=cho and p<=cha):
  if(cho%p==0 and cha%p==0):
    waht=p
  p+=1
print(waht)
