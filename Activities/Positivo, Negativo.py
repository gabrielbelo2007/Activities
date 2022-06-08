N = input()

if N.isdigit() and int(N) >= 1:
    print("positivo")
elif int(N) == 0:
    print("nulo")
else:
    print("negativo")