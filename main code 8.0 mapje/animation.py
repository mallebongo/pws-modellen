import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
import time

x = [0]
y = [0]


def animate(i):
    data_Planeten = pd.read_csv('data_Planeten.csv')
    columxaarde = data_Planeten["columxaarde"]
    columyaarde = data_Planeten["columyaarde"]
    columxmars = data_Planeten["columxmars"]
    columymars = data_Planeten["columymars"]
    satellieten_x = tuple(data_Planeten["x_satelliet_plot"])

    satellieten_y = tuple(data_Planeten["y_satelliet_plot"])
    print(np.shape(satellieten_y), np.shape(satellieten_x))
    print(satellieten_y)

    plt.cla()
    plt.plot(satellieten_x, satellieten_y, color='c', markersize=2)
    plt.plot(columxaarde, columyaarde, color='b', markersize=2.5)
    plt.plot(columxmars, columymars, color='r', markersize=2.5)
    plt.plot(0, 0, color='y', markersize=20)
    plt.axis([-500, 500, -500, 500])


ani = FuncAnimation(plt.gcf(),animate, interval=1000)

plt.show()

