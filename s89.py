cha,che=map(int,input().split())
for i in range(0,(cha*che)+1):
  if(i**2==0):
    print("yes")
    break
else:
  print("no")
