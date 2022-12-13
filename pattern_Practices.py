row = 5

for i in range(0,row+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("@-------------------------------@")

# print Pattern reverse pramid

for i in range(row,0,-1):
    for j in range(0,i):
        print(i,end="")
    print()
for i in range(2,row+1):
    for j in range(0,i):
        print(i,end="")
    print()

print("@-------------------------------@")

rows = 5
ij = rows
for i in range(row,0,-1):
    for j in range(0,i):
        print(ij,end="")
    print()

print("@-------------------------------@")

def fib(mymax):
    a = 1
    b = 0
    while True:
        c = a+b
        if c<mymax:
            yield c
            a = b
            b = c
        else:
            break

gen = fib(10)
"""print(gen)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

st = "iam the very happiest person in the wolrd"

out = ""
for i in st:
    if i not in out:
        out = out + i
print(out)

outer = []
for i in st:
    if i not in outer:
        outer.append(i)
print(outer)
print(" ".join(outer))
