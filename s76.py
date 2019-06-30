cha=int(input())
if(cha>1):
  for p in range(2,cha/2):
    if(cha%p==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
