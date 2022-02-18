def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1
def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2
def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3
def is_triangle(sides):
    con1 = sides[0] + sides[1] > sides[2]
    con2 = sides[1] + sides[2] > sides[0]
    con3 = sides[0] + sides[2] > sides[1]
    return all(sides) and con1 and con2 and con3


'''
print("Input triangle sides: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
	print("Equilateral triangle")
elif a==b or b==c or c==a:
	print("isosceles triangle")
else:
	print("Scalene triangle")
'''    