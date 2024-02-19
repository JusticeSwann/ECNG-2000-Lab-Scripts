import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def createDataFrame(path_to_data):
    df = pd.read_csv(path_to_data)
    return df



def generateScatterPlot(title, x ,y ,xAxisLabel, yAxisLabel,bestfit=False):
    plt.scatter(x, y)
    
    # Add gridlines
    plt.grid(True)
    
    if bestfit == True:
        # Calculate and plot best fit line
        coeffs = np.polyfit(x, y, 1)
        best_fit = np.poly1d(coeffs)
        plt.plot(x, best_fit(x), color='red')
    else:
        plt.plot(x, y)
    
    
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.title(title)
    plt.show()