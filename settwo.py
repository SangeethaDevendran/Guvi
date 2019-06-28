check=int(input())
for i in range(2,check):
  if(check%i==0):
    print("no")
    break
else:
  print("yes")
