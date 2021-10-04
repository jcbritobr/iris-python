# load modules
# %%
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import pandas as pd

# Load dataset
# %%
iris_df = pd.read_csv("Iris.csv")
iris_df.head()

# Load datasets by species
# %%
virginica_df = iris_df[iris_df['Species'] == 'Iris-virginica']
setosa_df = iris_df[iris_df['Species'] == 'Iris-setosa']
versicolor_df = iris_df[iris_df['Species'] == 'Iris-versicolor']

# Plot functions
# %%

def generate_scatter(x_field: str, y_field: str, xlabel: str, ylabel: str, dataset: pd.DataFrame):
    fig = plt.figure()
    ax = sn.scatterplot(x=x_field, y=y_field,
                        data=dataset, hue="Species")
    ax.set(xlabel=xlabel, ylabel=ylabel)


def generate_histograms(title: str, dataset: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(16, 8))
    fig.suptitle(title, fontsize=22)

    sp_width_h = sn.histplot(ax=axes[0, 0], data=dataset, x="SepalWidthCm")
    sp_width_h.set(xlabel="Sepal Width (cm)", ylabel="Frequency")

    splenght_h = sn.histplot(ax=axes[0, 1], data=dataset, x='SepalLengthCm')
    splenght_h.set(xlabel="Sepal Length (cm)", ylabel="")

    pl_width_h = sn.histplot(ax=axes[1, 0], data=dataset, x="PetalWidthCm")
    pl_width_h.set(xlabel="Petal Width (cm)", ylabel="Frequency")

    ptlenght_h = sn.histplot(ax=axes[1, 1], data=dataset, x='PetalLengthCm')
    ptlenght_h.set(xlabel="Petal Length (cm)", ylabel="")

# Plot data
# %%

generate_scatter("PetalWidthCm", "PetalLengthCm", "Petal Width (cm)", "Petal Length (cm)", iris_df)
generate_scatter("SepalWidthCm", "SepalLengthCm", "Sepal Width (cm)", "Sepal Length (cm)", iris_df)
generate_histograms("Setosa Histograms", setosa_df)
generate_histograms("Virginica Histograms", virginica_df)
generate_histograms("Versicolor Histograms", versicolor_df)
