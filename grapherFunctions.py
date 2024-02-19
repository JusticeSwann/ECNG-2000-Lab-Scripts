import pandas as pd
import matplotlib.pyplot as plt


def createDataFrame(path_to_data):
    df = pd.read_csv(path_to_data)
    return df


def generateScatterPlot(title, x ,y ,xAxisLabel, yAxisLabel):
    plt.plot(x, y)
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.title(title)
    plt.show()
