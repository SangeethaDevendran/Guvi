check=int(input())
valid=list(map(int,input().split()[:check]))
valid.sort()
que=(len(valid)-1)/2
print(valid(que))
