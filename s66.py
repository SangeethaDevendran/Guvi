ch=input()
for i in range(0,len(ch)):
  if(ch[i].isalpha() and ch[i].isdigit()):
    print("No")
else:
  print("Yes")
