
def Power12345(a):
    b=a*a
    c=b*a
    d=c*a
    return(b,c,d)

for i in range(0,5):
    a = int(input("Введите число a="))
    b,c,d=Power12345(a)
    print("a^2=",b)
    print("a^3=",c)
    print("a^4=",d)
    
