import math

def square(side):
    area = side * side
    return math.ceil(area) if not isinstance(side, int) else area
num_side = int(input("Введите число: "))
print(f"Площадь квадрата: {square(num_side)}")