import math

# 35
V = int(input("Введите скорость лодки в стоячей воде"))
U = int(input("Введите скорость течения реки"))
T1 = int(input("Введите время движения лодки по озеру"))
T2 = int(input("Введите время движения лодки по реке(против течения)"))
S = V*T1+(V-U)*T2
print(S)
