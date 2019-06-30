ch=input()
for i in range(o,len(ch)):
  if(ch[i].isalpha() and ch[i].isdigit()):
    print("Yes")
else:
  print("No")
