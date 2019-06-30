check=int(input())
valid=list(map(int,input().split()[:check]))
valid.sort()
que=(len(valid))/2
print(valid[que])
