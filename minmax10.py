N = int(input("Введите количество чисел N="))
ResMin=0
ResMax=0
MinimumN=-1
MaximumN=-1

for i in range(1,N+1):
    a = int(input("Введите число n"+str(i)+"="))
    if i==1:
        ResMin=i
        MinimumN=a
        ResMax=i
        MaximumN=a
    else:    
        if MinimumN>a :
            ResMin=i
            MinimumN=a
        if MaximumN<a :
            ResMax=i
            MaximumN=a
            
Result=min(ResMin,ResMax)

print("Первый экстремальный элемент =",Result)
print("Минимум =",MinimumN)
print("Максимум =",MaximumN)
print("Минимальный номер =",ResMin)
print("Максимальный номер =",ResMax)
