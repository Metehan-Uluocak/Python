class Circle():
    pi = 3.14

    def __init__(self, apsis, ordinate):
        self.x = apsis
        self.y = ordinate
        self.radius = self.calculate_radius()
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    def calculate_radius(self):
        return abs(self.x * self.y)

    def get_area(self):
        return round(self.pi * self.radius ** 2)

    def get_perimeter(self):
        return round(2 * self.pi * self.radius)

    def position(self, other):
        x_diff = (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        distance = (x_diff + y_diff) ** 0.5

        if abs(self.radius - other.radius) < distance < (self.radius + other.radius):
            return "Bu çemberler kesisiyor."
        elif distance == (self.radius + other.radius) or distance == abs(self.radius - other.radius):
            return "Bu çemberler teğet."
        else:
            return "Bu çemberler kesilmiyor."

    def __str__(self):
        return f"Circle = M({self.x},{self.y})\nRadius = {self.radius}\nArea = {self.area}\nPerimeter = {self.perimeter}"


apsis = int(input("1. çemberin apsisini girin: "))
ordinate = int(input("1. çemberin ordinatını girin: "))
circle1 = Circle(apsis, ordinate)

apsis = int(input("2. çemberin apsisini girin: "))
ordinate = int(input("2. çemberin ordinatını girin: "))
circle2 = Circle(apsis, ordinate)


print(circle1.position(circle2))
print(circle1)
print(circle2)
