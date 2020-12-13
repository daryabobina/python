def revers(s):
    return s[::-1]

def IsPalindrom(k):
    Ks=str(k)
    if (Ks==revers(Ks)):
       return True 
    else:
        return False
Result=0
for i in range(0,3):
    k = int(input("Введите число K="))
    if IsPalindrom(k)==True:
       Result=Result+1
print("Количество палиндромов в наборе из 10 чисел=",Result)
