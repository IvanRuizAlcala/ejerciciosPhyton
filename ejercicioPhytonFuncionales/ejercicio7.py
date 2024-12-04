def asignaturas_y_calificaciones(notas_dict):
    def calificacion(nota):
        if nota >= 90:
            return "SOBRESALIENTE"
        elif nota >= 70:
            return "NOTABLE"
        elif nota >= 50:
            return "APROBADO"
        else:
            return "SUSPENSO"

    return {asignatura.upper(): calificacion(nota) for asignatura, nota in notas_dict.items()}

notas = {"Matemáticas": 95, "Historia": 82, "Ciencias": 67, "Arte": 45}
resultado = asignaturas_y_calificaciones(notas)
print(resultado)
