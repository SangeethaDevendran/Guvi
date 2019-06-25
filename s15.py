LAR1=int(input())
LAR2=int(input())
LAR3=int(input())
if(LAR1 > LAR2 and LAR1 > LAR3):
  Largest=LAR1
if(LAR2 > LAR1 and LAR2 > LAR3):
  Largest=LAR2
else:
  Largest=LAR3
print(Largest)
