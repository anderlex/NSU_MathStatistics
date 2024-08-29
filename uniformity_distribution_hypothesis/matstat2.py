from math import *
from scipy.stats import norm, nct, chi2, f
import matplotlib.pyplot as plt
import numpy as np

eps = 0.05
x = np.loadtxt("vyborka_3.txt", delimiter=' ', dtype=float)
x = np.sort(x)

x_ = np.average(x) #Выборочное среднее
n = x.size

#Кол-во интервалов для Хи-квадрат
K = 5

#Квантиль Колмoгорова уровня 1 - eps = 0.95 (eps = 0.05)
q_k = 1.36 

F_emp = np.where(x <= x)[0]/n

D_k = sqrt(n)*max(abs(F_emp - x))

print("d =",round(D_k,4))
print("q =",round(q_k,4))

print("Kritery Kolmogorova:")
if D_k < q_k: print("Ravnomernaya")
else: print("Ne ravnomernaya")

#Квантиль Хи-квадрат уровня 1 - eps = 0.95
ch = chi2(df = K - 1)
q_ch = ch.ppf(1 - eps) 

p = [0.2,0.2,0.2,0.2,0.2]

nu = [0,0,0,0,0]

for i in range(K):
	for xi in x:
		if 0.2*i <= xi and xi <= 0.2*i + 0.2:
			nu[i] += 1

Xi2 = 0
for j in range(K):
	Xi2 += (nu[j] - n*p[j])**2/(n*p[j])

D_ch = Xi2

print("d =",round(D_ch,4))
print("q =",round(q_ch,4))

print("Kritery X2:")
if D_ch < q_ch: print("Ravnomernaya")
else: print("Ne ravnomernaya")

plt.figure(figsize=(9,6))
plt.plot(x,x, label="distribution")

plt.hlines(F_emp[0], x[0], x[0], label="empiric", color='black')
for j in range(n-1): 
	plt.hlines(F_emp[j+1], x[j], x[j+1], color='black')

plt.legend(title='Functions:')
plt.grid()
plt.show()
