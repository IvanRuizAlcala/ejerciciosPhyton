def calcular_calificaciones(notas):
    def calificacion(nota):
        if nota >= 90:
            return "Sobresaliente"
        elif nota >= 70:
            return "Notable"
        elif nota >= 50:
            return "Aprobado"
        else:
            return "Suspenso"

    return [calificacion(nota) for nota in notas]

notas = [95, 82, 67, 45, 73, 88]
resultado = calcular_calificaciones(notas)
print(resultado)
