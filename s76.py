cha=int(input())
if(cha>1):
  for p in range(2,cha):
    if(cha%p==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
