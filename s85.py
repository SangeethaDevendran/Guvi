cha=list(input())
if((len(cha))%2==0):
  cha[int(len(cha)/2)]="*"
  cha[int(len(cha)/2)-1]="*"
else:
  cha[int(len(cha)/2)]="*"
for p in range(0,len(cha)):
  print(cha,end=" ")
