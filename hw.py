from matplotlib import pyplot as plt
import random
from scipy.integrate import solve_ivp
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

X0 = random.random() * (0.1 + 0.1) - 0.1
Y0 = random.random() * (0.1 + 0.1) - 0.1
Z0 = random.random() * (0.1 + 0.1) - 0.1

def f1(x,y,a,b):
    g = 1.0 - a*x**2.0 + y
    h = b*x
    return g, h

def f2(x,y,z, M1, B, M2):
    g = y
    h = z
    j = M1 + B*x + M2*y - z**2.0
    return g, h, j

def task1(x0, y0):
    x, y = f1(x0, y0, 2, 2)
    listX = [x]
    listY = [y]
    plt.scatter(listX, listY)
    plt.show()

def task2(x0, y0):
    finalTrajectories = []
    params = [(0.9, -0.3), (1.27, 0.03), (1.42, 0.26)]
    for a,b in params:
        x = x0
        y = y0
        trajectoryX = []
        trajectoryY = []
        for i in range(1000):
            trajectoryX.append(x)
            trajectoryY.append(y)
            x, y = f1(x, y ,a, b)
        finalTrajectories.append((trajectoryX,trajectoryY));
    return finalTrajectories

def task3(x0,y0):
    finalTr = task2(x0,y0)
    fig, ax = plt.subplots(3, 1, figsize = (8,8))
    for i in range(len(finalTr)):
        trajectoryX, trajectoryY = finalTr[i]

        ax[i].scatter(trajectoryX, trajectoryY, s=1)
        ax[i].set_xlabel("X")
        ax[i].set_ylabel("Y")

    plt.show()

def task4(x0, y0, z0):
    B = 0.7
    finalTrajectories = []
    params = [(0.06, 0.06), (-0.5, 0.03), (-0.28, 0.23)]
    for a, b in params:
        x = x0
        y = y0
        z = z0
        trajectoryX = []
        trajectoryY = []
        trajectoryZ = []
        for i in range(1000):
            trajectoryX.append(x)
            trajectoryY.append(y)
            trajectoryZ.append(z)
            x, y, z = f2(x, y, z, b, 0.7, a)
        finalTrajectories.append((trajectoryX, trajectoryY, trajectoryZ));

    fig = plt.figure(figsize=(8, 8))
    for i in range(len(finalTrajectories)):
        trajectoryX, trajectoryY, trajectoryZ = finalTrajectories[i]
        ax = fig.add_subplot(3, 1, i + 1, projection='3d')
        ax.scatter(trajectoryX, trajectoryY, trajectoryZ, s=1)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

    plt.show()


def task5():
    def logistic_map(r, x):

        return r * x * (1 - x)


    r_values = np.linspace(2.4, 4.0, 1000)
    iterations = 10000
    last = 1000

    x_values = np.zeros((len(r_values), last))

    for i, r in enumerate(r_values):
        x = 0.01
        for _ in range(iterations):
            x = logistic_map(r, x)
            if _ >= iterations - last:
                x_values[i, _ - (iterations - last)] = x

    plt.figure(figsize=(12, 8))
    plt.title("Бифуркационное дерево для логистического отображения")
    plt.xlabel("r")
    plt.ylabel("x")


    for i in range(len(r_values)):
        plt.scatter(np.full(last, r_values[i]), x_values[i], s=0.1, color='black')

    plt.xlim(2.4, 4.0)
    plt.ylim(-0.1, 1.1)
    plt.grid()
    plt.show()

task1(X0, Y0)
print(task2(X0, Y0))
task3(X0, Y0)
task4(X0,Y0,Z0)
task5()