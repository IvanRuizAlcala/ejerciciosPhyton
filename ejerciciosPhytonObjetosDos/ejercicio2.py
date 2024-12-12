class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sumar_vectores(self, otro_vector):
        nuevo_x = self.x + otro_vector.x
        nuevo_y = self.y + otro_vector.y
        return Vector(nuevo_x, nuevo_y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(2, 3)
vector2 = Vector(4, 5)
vector_suma = vector1.sumar_vectores(vector2)
print(vector_suma)  
