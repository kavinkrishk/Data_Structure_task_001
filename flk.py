

a = [1,12,1.3,"kavin",1+5j,1,1.3]
print(type(a))
print(a)
a[0]=10
print(a)

b = (1,12,1.3,"kavin",1+5j,1,1.3)
print(type(b))
print(b)

c = {1,12,1.3,"kavin",1+5j,1,12,1.3,15}
print(type(c))
print(c)

di = {"a":1,"b":2.5,"c":5+5j,"d":5,"a":"kavin"}
print(type(di))
print(di)

di["b"]="good"
print(di)
k = [1,2,3,4]
print(k)
k.pop()
print(k)
k.remove(3)
print(k)