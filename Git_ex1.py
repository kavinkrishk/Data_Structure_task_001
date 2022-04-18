a = 5000
print(a,"Available balance")
b =(input("Enter Amount"))

if a>=int(b):
    c = ((int(a))-(int(b)))
    d = a-(int(b))

    if d==0:
        print("Zero Balance")
        print("Please maintain Minimum Balance")
    elif d<=3000:
        print(d,"Your Current Balance")
        print("Please maintain Minimum Balance")
    else:
        print(d,"Your Current Balance")

else:
    print("Please Enter Numbers Only")



