f = open("myfile.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("...and another one!")

f = open("myfile.txt","r")
print(f.readable())
f = open("new.txt","r")
print(f.readable())
