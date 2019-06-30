source=int(input())
final=list(map(int,input().split()[:source]))
final.sort()
for i in final:
  print(i,end=" ")
