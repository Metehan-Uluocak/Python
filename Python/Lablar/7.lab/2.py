class Fraction():
    
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom        
        self.wholePart = self.num // self.denom
    
    def __gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify(self, top, bottom):
        if top < 0:
            top = top * -1
        ebob = self.__gcd(top, bottom)
        top2 = top // ebob
        bottom2 = bottom // ebob
        return Fraction(-1 * top2, bottom2) if top < 0 else Fraction(top2, bottom2)

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return self.simplify(top, bottom)
    
    def __sub__(self, other):
        top = self.num * other.denom - self.denom * other.num
        bottom = self.denom * other.denom
        return self.simplify(top, bottom)

    def __mul__(self, other):
        top = self.num * other.num
        bottom = self.denom * other.denom
        return self.simplify(top, bottom)
    
    def __truediv__(self, other):
        temp = other.num
        other.num = other.denom
        other.denom = temp
        top = self.num * other.num
        bottom = self.denom * other.denom
        return self.simplify(top, bottom)

    def __str__(self):
        if self.num > 0:
            if (self.num / self.denom) % 1 == 0:
                return str(self.wholePart)
            elif self.num / self.denom > 0:
                self.num = self.num % self.denom
                return f"{self.wholePart}+{self.num}/{self.denom}"
                
            return f"{self.wholePart}+{self.num}/{self.denom}" 
        else:
            self.num = self.num * -1
            if (self.num / self.denom) % 1 == 0:
                return str(self.wholePart)
            elif self.num / self.denom > 0:
                self.num = self.num % self.denom
                return f"{self.wholePart + 1}-{self.num}/{self.denom}"
                
            return f"{self.wholePart + 1}-{self.num}/{self.denom}" 


numerator = int(input("İlk kesirin sayısını girin: "))
denominator = int(input("İlk kesirin paydasını girin: "))
rational1 = Fraction(numerator, denominator)


numerator = int(input("İkinci kesirin sayısını girin: "))
denominator = int(input("İkinci kesirin paydasını girin: "))
rational2 = Fraction(numerator, denominator)


print(f"Toplama: {rational1 + rational2}")
print(f"Çıkarma: {rational1 - rational2}")
print(f"Çarpma: {rational1 * rational2}")
print(f"Bölme: {rational1 / rational2}")
