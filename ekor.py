
from matplotlib import pyplot as plt




def plot_my_graph(x,val):
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    plt.xlim(0.00, -val)
    plt.ylim(0.00, val)
    plt.grid(True)
    plt.plot(x,marker="o", markersize=20, markeredgecolor="red", markerfacecolor="red")
    plt.show()


