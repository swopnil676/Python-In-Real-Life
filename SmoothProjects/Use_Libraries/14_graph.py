import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

def plot_data(n=50):
    data = np.random.randn(n)
    sns.histplot(data, kde=True)
    plt.show()

widgets.interact(plot_data, n=(10, 200, 10))