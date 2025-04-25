from shape import Sphere, Cylinder, Cube
import random

shapes = []

for i in range(10):
    shape_type = random.choice(["Sphere", "Cylinder", "Cube"])

    if shape_type == "Sphere":
        radius = random.randint(1, 10)
        shape = Sphere(radius)
    
    elif shape_type == "Cylinder":
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        shape = Cylinder(radius, height)
    
    else:  # Cube
        side = random.randint(1, 10)
        shape = Cube(side)

    shapes.append(shape)

for j in shapes:
    print(f"Name of the shape: {j}")
    print(f"Surface area: {j.surface_area():.2f}")
    print(f"Volume: {j.volume():.2f}")
    print()
