from datetime import dtetime
first=input()
second=input()
format="%H:%M"
time=datetime.strptime(first,format)-datetime.strptime(second,format)
print(time)
