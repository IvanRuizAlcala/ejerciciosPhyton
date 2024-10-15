#1
asignaturas=list(['Matematicas','Fisica','Quimica','Historia','Lengua'])
print ("Las asignaturas son: ")
for asignaturas in asignaturas:
    print(asignaturas)

#2
asignaturas=list(['Matematicas','Fisica','Quimica','Historia','Lengua'])
for asignaturas in asignaturas:
    print("Yo estudio: " + asignaturas)

#3
asignaturas=list(['Matematicas','Fisica','Quimica','Historia','Lengua'])
notas=[]

for i in asignaturas:
    nota = int(input("Dime que nota has sacado en "+str(i)+": "))
    notas.append(nota)

for i in range(0,len(asignaturas)):
    print("La asignatura " , asignaturas[i] , " has sacado un: " + str(notas[i]))

#4
loteria = int(input('Dime cuantos numeros ganados de la loteria han salido: '))
premiados=[]
for i in range(0,loteria):
    premio = int(input('Dime el numero : '))
    premiados.append(premio)

premiados.sort()
print("Lista ordenada de menor a mayor: ",premiados)

#5
print('Numeros del 1-10 mostrados en orden inverso')
numerosLista = []
for i in range(1,11):
    numerosLista.append(i)

numerosLista.reverse()
print(numerosLista)

#6
print('Asiganturas aprobadas y suspensas')
asignaturas=list(['Matematicas','Fisica','Quimica','Historia','Lengua'])
repetir=[]

for asignaturas in asignaturas:
   nota = float(input(f"Que nota has sacado en {asignaturas}?: "))

if nota < 5:
    repetir.append(asignaturas)

    
if repetir:
    print('Asignaturas a repetir: ',repetir)
else:
     print('Enhorabuena, todas aprobadas')

#7
print('Mostrar el abecedario modificado')
abecedario = list('abcdefghijklmnopqrstuvwxyz')
resultado = []
for i in range(len(abecedario)):
   
    if (i + 1) % 3 != 0: 
        resultado.append(abecedario[i])

print("Lista resultante después de eliminar los múltiplos de 3:")
print(resultado)

#8
palabra = input("Introduce una palabra: ")
palabra = palabra.lower().replace(" ", "")

if palabra == palabra[::-1]:
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')

#9
palabra = input("Introduce una palabra: ").lower() 

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for letra in palabra:
    if letra == 'a':
        a_count += 1
    elif letra == 'e':
        e_count += 1
    elif letra == 'i':
        i_count += 1
    elif letra == 'o':
        o_count += 1
    elif letra == 'u':
        u_count += 1

# Mostrar el resultado
print("Número de veces que contiene cada vocal:")
print(f"a: {a_count}")
print(f"e: {e_count}")
print(f"i: {i_count}")
print(f"o: {o_count}")
print(f"u: {u_count}")

#10
print('Ordenar de menor a mayor')
num2 = [50,75,46,22,80,65,8]

num2.sort()
print(num2)


#11
vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

producto_escalar = 0

for i in range(len(vector1)):
    producto_escalar += vector1[i] * vector2[i]

print("El producto escalar de los vectores es:", producto_escalar)









