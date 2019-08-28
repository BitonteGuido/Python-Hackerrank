a=int(input())
b=input()
c=int(input())
d=input()

x=set(map(int,b.split()))
y=set(map(int,d.split()))

print(len(x.intersection(y)))
