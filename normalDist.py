# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt


def normalDist():
    mu = 0
    variance = 16
    variance_y = 64 * 2
    sigma = np.sqrt(variance)
    sigma_y =np.sqrt(variance_y)
    s = np.random.normal(mu, sigma, 1000)
    s_y = np.random.normal(mu, sigma_y, 50)

    count, bins, ignored = plt.hist(s,100, density=True)
    count_y, bins_y, ignored_y = plt.hist(s_y,100, density=True)
    plt.close()
    plt.plot(bins,1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r',label='Z')
    plt.plot(bins_y,1/(sigma_y * np.sqrt(2 * np.pi)) *
             np.exp( - (bins_y - mu)**2 / (2 * sigma_y**2) ),
             linewidth=2, color='b',label='Y')
    plt.legend()

    plt.show()
    print("asasd")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    normalDist()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
