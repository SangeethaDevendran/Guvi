cho=input()
cha=[]
for i in cho:
  if i.isnumeric():
    cha.append(i)
print("".join(cha))
