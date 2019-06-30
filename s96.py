cho=list(input())
cha=[]
for i in cho:
  if(i not in cha):
    cha.append(i)
if(cho==cha):
  print("Yes")
else:
  print("No")
