alfa = {"a": 1, "b": 2, "c": 3, "d": 4,  "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
        "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "x": 23, "z": 24}

alfa_num = dict((valor, chave) for chave, valor in alfa.items())

P = input()


def vogal(*args):
    P_n = ""
    for v in P:
        if v in "aeiou":
            P_n += v
        elif v in alfa:
            P_n += v
            num_cons = alfa.get(v)
            x = alfa_num[num_cons]
            num_cons1 = num_cons
            num_cons2 = num_cons
            while x not in "aeiou" and num_cons1 < 24:
                num_cons1 += 1
                x = alfa_num[num_cons1]
            else:
                y = alfa[x]
                x = alfa_num[num_cons]
                while x not in "aeiou":
                    num_cons2 -= 1
                    x = alfa_num[num_cons2]
                else:
                    z = alfa[x]
                    if num_cons - y > z - num_cons and y < 24:
                        P_n += alfa_num[y]
                    else:
                        P_n += alfa_num[z]
            if num_cons < 24:
                num_cons += 1
                x = alfa_num[num_cons]
            if x not in "aeiou" and num_cons < 25:
                P_n += alfa_num[num_cons]
            elif num_cons == 24:
                P_n += alfa_num[num_cons]
            else:
                num_cons += 1
                P_n += alfa_num[num_cons]

    print(P_n)
vogal(P)

