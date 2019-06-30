ch=input()
fi=0
for i in range(len(ch)):
  if(ch[i].isdigit() or ch[i].isalpha() or ch[i]==(" ")):
    continue
  else:
    fi+=1
print(fi)
  
