def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print("el inverso modular no existe")
    else:
        return x % m
a=int(input("ingresa un numero a: "))  
m=int(input("ingresa un numero m: "))  
print("el inverso multiplicativo es: ",modinv(a,m))