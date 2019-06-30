cho,cha=map(int,input().split())
sho,sha=cho,cha
while(cha):
  cho,cha=cha,cho%cha
sasu=(sho*sha)//cho
print(sasu)
