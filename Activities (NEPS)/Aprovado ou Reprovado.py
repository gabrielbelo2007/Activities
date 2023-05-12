notas = input()
nota1 = ''
var = True

while var:
    for v in notas:
        if v.isdigit() or v == '.':
            nota1 += v
        else:
            var = False
            break

nota2 = ''.join(x for x in notas if x not in nota1)

if nota2 == ' ':
    nota2 += notas[0]
    nota2 += notas[1]

media = (float(nota1) + float(nota2)) / 2

if media >= 7:
    print('Aprovado')

elif media >= 4:
    print('Recuperacao')

else:
    print('Reprovado')