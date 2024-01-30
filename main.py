import matplotlib.pyplot as plt
import numpy as np

#medidas da biela e da manivela em centímetros
manivela = 16 
biela = 92

#cálculo dos angulos
teta = np.arange(0, 360, 10)
teta = np.radians(teta)
beta = np.arcsin((manivela*np.sin(teta))/biela)

#cálculo das coordenadas dos pontos A e B
xa = [None] * len(teta)
ya = [None] * len(teta)
xb = [None] * len(teta)
yb = [None] * len(teta)
for i in range(0, len(teta)):
    xa = manivela*np.cos(teta)
    ya = manivela*np.sin(teta)
    xb = (biela*np.cos(beta)) + xa
    yb[i] = 0

plt.ion()

for i in range(len(teta)):

    plt.scatter(xa[i], ya[i], marker = '.', color = 'b')
    plt.scatter(xb[i], yb[i], marker = '.', color = 'k')
    plt.grid(True)

    plt.pause(0.1)
    plt.cla()
    plt.clf()

plt.ioff()
