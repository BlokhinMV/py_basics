class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return f'{self.real} + {self.img}j'

    def __add__(self, other):
        summ_c = Complex(self.real + other.real, self.img + other.img)
        return summ_c

    def __mul__(self, other):
        mul_c = Complex(self.real * other.real - self.img * other.img, self.real * other.img + self.img * other.real)
        return mul_c

c1 = Complex(3, 2)
c2 = Complex(5, 1)
print(c1 + c2)
print(c1 * c2)
