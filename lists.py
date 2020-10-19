# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print (mylist)

mylist2 = [5, True, "apple"]
print(mylist2)

if "banana" in mylist:
        print("yes")
else:
        print("no")
mylist.append("lemon")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

