from math import *
from scipy.stats import norm, nct, chi2, f
import matplotlib.pyplot as plt
import numpy as np

#Первая выборка из 20 элементов
x = np.loadtxt("vyborka_1.txt", delimiter=' ', dtype=float)
#Последняя выборка из 30 элементов
y = np.loadtxt("vyborka_2.txt", delimiter=' ', dtype=float)
#Общая выборка из 50 элементов
Xn = np.concatenate([x,y])
print(Xn)
#Параметры нормального распределения и эпсилон
alpha = -1
sigma2 = 0.5
eps = 0.05

n = len(Xn)
#Выборочное среднее
X_ = round(np.average(Xn),4)
print("X^_ =", X_)
#Выборочная дисперсия
S = round(np.average(Xn*Xn) - X_**2,4)
print("S =", S)
#Несмещенная выборочная дисперсия
S_0 = round(n/(n-1)*S,4)
print("S0 =", S_0)
#Несмещенная выборочная дисперсия при известном среднем
S_1 = round(np.average((Xn - alpha*np.ones(n))*(Xn - alpha*np.ones(n))),4)
print("S1 =", S_1)

#Значение а при известном сигма
tau_a = norm.ppf(1 - eps/2)
print("\nN(0,1):", round(tau_a,4))

offset = tau_a*sqrt(sigma2)/sqrt(n)
L = round(X_ - offset,4)
R = round(X_ + offset,4)
print("P(",L,"<", alpha ,"<", R,") =", 1 - eps)

#Значение а при неизвестном сигма
st = nct(n - 1, 0)
tau_b = st.ppf(1 - eps/2)
print("\nT(49):", round(tau_b,4))

offset = tau_b*S_0/sqrt(n)
L = round(X_ - offset,4)
R = round(X_ + offset,4)
print("P(",L,"<", alpha ,"<", R,") =", 1 - eps)

#Значение сигма при известном а
ch = chi2(n)
print("\nXu^2(50):")
tau_c_1 = ch.ppf(eps/2)
print("eps/2:",round(tau_c_1,4))
tau_c_2 = ch.ppf(1 - eps/2)
print("1 - eps/2:",round(tau_c_2,4),"\n")

L = round(n*S_1/tau_c_2,4)
R = round(n*S_1/tau_c_1,4)
print("P(",L,"<", sigma2 ,"<", R,") =", 1 - eps)

#Значение сигма при неизвестном а
ch = chi2(n - 1)
print("\nXu^2(49):")
tau_c_1 = ch.ppf(eps/2)
print("eps/2:",round(tau_c_1,4))
tau_c_2 = ch.ppf(1 - eps/2)
print("1 - eps/2:",round(tau_c_2,4),"\n")

L = round(n*S/tau_c_2,4)
R = round(n*S/tau_c_1,4)
print("P(",L,"<", sigma2 ,"<", R,") =", 1 - eps)


