cha=int(input())
if(cha>1):
  for i in range(2,cha):
    if(cha%i==0):
      print("yes")
      break
  else:
  print("no")
