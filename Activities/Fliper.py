val1 = list(input(""))
del(val1[1])

if val1[0] == "1" and val1[1] == "1":
    print("A")

elif val1[0] == "1" and val1[1] == "0":
    print("B")

elif val1[0] == "0":
    print("C")