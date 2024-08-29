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
#Параметры нормального распределения и эпсилон
alpha = -1
sigma2 = 0.5
eps = 0.05
#Несмещенная выборочная дисперсия для первых 20
n = len(x)
x_ = np.average(x)
print(round(x_,4))
s_x_0 = x - x_*np.ones(n)
s_x_0 = sum(s_x_0*s_x_0)/(n-1)
print(round(s_x_0,4))
#Несмещенная выборочная дисперсия для последних 30
m = len(y)
y_ = np.average(y)
print(round(y_,4))
s_y_0 = y - y_*np.ones(m)
s_y_0 = sum(s_y_0*s_y_0)/(m-1)
print(round(s_y_0,4))

#Критерий Фишера

d_F = s_x_0/s_y_0

fis = f(dfn = n - 1, dfd = m - 1)
t_1 = fis.ppf(eps/2)
t_2 = fis.ppf(1 - eps/2)

if t_1 <= d_F and d_F <= t_2:
	print("Dispersii sovpadauyt")
else: print("Dispersii ne sovpadauyt")
print("f_eps/2 =",round(t_1,4))
print("f_(1-eps/2) =",round(t_2,4))
print("d_F =",round(d_F,4))

#Критерий Стьюдента

st = nct(df = m+n-2, nc = 0)

q_s = st.ppf(1-eps/2)

numer = sqrt(n*m/(n+m))*(x_ - y_)
denum = sqrt(((n-1)*s_x_0 + (m-1)*s_y_0)/(n+m-2))

d_S = numer/denum

if abs(d_S) <= q_s:
	print("Srednie sovpadauyt pri uslovii 4to sovpadauyt Dispersii")
else: print("Srednie ne sovpadauyt pri uslovii 4to sovpadauyt Dispersii")
print("q_s =", round(q_s,4))
print("|d_S| =", round(abs(d_S),4))