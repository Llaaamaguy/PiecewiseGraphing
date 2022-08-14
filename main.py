import matplotlib.pyplot as plt
from Piecewise import Piecewise
from Function import Function
import numpy as np


def main():
    funcs = [
        Function("3x+8", "x <= -4"),
        Function("-1", "-4 < x <= 2"),
        Function("(x-2)^2-5", "x > 2")
    ]
    pwFunc = Piecewise(funcs)
    points = pwFunc.getGraphPoints((-10, 10))
    for k, v in points.items():
        x = [i[0] for i in v[1]]
        y = [j[1] for j in v[1]]
        plt.plot(x, y, label=v[0])
    plt.legend()
    plt.grid()
    plt.axhline(y=0, lw=1, color="k")
    plt.axvline(x=0, lw=1, color="k")
    plt.show()


if __name__ == "__main__":
    main()
