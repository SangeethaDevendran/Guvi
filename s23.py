source=int(input())
for p in range(2,source):
  if(source%p==0):
    print("no")
    break
else:
  print("yes")
