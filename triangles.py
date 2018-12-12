import math
side_1 = int(input("put in one side of the triangle "))
side_2 = int(input("put in the second side of the triangle "))
hypotenuse_inter = side_1*side_1+side_2*side_2
hypotenuse = math.sqrt(hypotenuse_inter)
print(f"the hypotenuse of the triangle is {hypotenuse}")