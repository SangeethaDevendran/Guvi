check,run=map(int,input().split())
valid=list(map(int,input().split()))
sange=0
for p in range(run):
  sange=sange+valid[p]
print(sange)
