ch=int(input())
fab,fabo=0,1
print(fabo,end=" ")
for i in range(1,ch):
  faboo=fab+fabo
  print(faboo,end=" ")
  fab,fabo=fabo,faboo
