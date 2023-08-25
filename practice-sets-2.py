import math
def heron_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area
compute_a = float(input("Enter the length of side a: "))
compute_b = float(input("Enter the length of side b: "))
compute_c = float(input("Enter the length of side c: "))

triangle = heron_area(compute_a, compute_b, compute_c)
print(f"The area of the triangle is: {triangle}")

