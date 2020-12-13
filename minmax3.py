N = int(input("Введите количество прямоугольников N="))

Result=0

for i in range(1,N+1):
    print("Введите данные прямоугольника n"+str(i)+":")
    a = int(input("Введите сторону a"+str(i)+"="))
    b = int(input("Введите сторону b"+str(i)+"="))
    Perimetr=(a+b)*2
    
    if Perimetr>Result :
        Result=Perimetr
        

print("максимальный периметр прямоугольника =",Result)

