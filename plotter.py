
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

plt.plot(x_vals, y_vals)


def animate(i):
    data = pd.read_csv('pings.csv')
    x_vals = data['count']
    y_vals = data['pings']

    plt.cla()
    plt.plot(x_vals, y_vals, label="pings")
    plt.legend(loc="upper left")
    plt.tight_layout()

animate = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()



# y2 = data['total_2']