class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        return 'Sum of complex number: ' + str(self.real) + ' + ' + str(self.imaginary) + 'i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
n = int(input("Enter the number of complex numbers to be added: "))
c3 = Complex()
for i in range(n):
    print(f"Enter Complex number {i+1}:")
    r = float(input("Enter real: "))
    i = float(input("Enter imaginary: "))
    c2 = Complex(r, i)
    c3 = c3 + c2

print(c3)