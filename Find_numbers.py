my_list = range(10,20)
my_set = {5,10,25,46,50}
my_tuble = (7,5,3,9,8,63,54)

list = 15
set = 50
tuple = 54

if list in my_list:
    print(list,"is present")
else:
    print(list,"is not present")
if set in my_set:
    print(set,"is present")
else:
    print(set,"not present")
if tuple not in my_tuble:
    print(tuple,"is not present")
else:
    print(tuple,"is present")
