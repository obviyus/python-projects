from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

    return m, b

def squared_error (ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error (ys_orig, ys_line)
    squared_error_y_mean = squared_error (ys_orig, y_mean_line)








r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs,ys)

plt.plot(xs, regression_line)
plt.show()
