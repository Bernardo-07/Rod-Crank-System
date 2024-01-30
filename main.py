import matplotlib.pyplot as plt
import numpy as np

#medidas da biela e da manivela em centímetros
manivela = 41
biela = 92

#cálculo dos angulos
teta = np.arange(0, 361, 10)
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

for i in range(0, len(teta)):

    plt.scatter(xa[i], ya[i], marker = '.', color = 'b')
    plt.scatter(xb[i], yb[i], marker = '.', color = 'k')

    plt.plot([0, xa[i]], [0, ya[i]], color='b') 
    plt.plot([xa[i], xb[i]], [ya[i], yb[i]], color='k') 

    plt.xlabel('X Axis (cm)')
    plt.ylabel('Y Axis (cm)')
    plt.title('Rod-Crank System')
    plt.grid(True)

    #calculo dos limites da escala de x e y
    a = -manivela - biela - 5
    b = manivela + biela + 5
    c = -manivela - biela - 5
    d = manivela + biela + 5
    plt.xlim(a, b)
    plt.ylim(c, d)

    plt.pause(0.1)
    plt.cla()
    plt.clf()

plt.ioff()
