check=int(input())
valid=list(map(int,input().split()[:check]))
for p in range(check):
  print(valid[p],p)
