import math

def distance(point):
    x, y = point
    return math.sqrt(x**2 + y**2)

# Test
print(distance((3, 4)))  # devrait donner 5.0
