# Author: Philip Cullen

# This program is designed to analyse the Iris dataset
# There are three main tasks associated with this program
# 1. Output a summary of each variable into a single text file
# 2. Save a histogram of each variable into .png files
# 3. Output a scatter plot of each pair of variables
# Each task will be highlighted with their own section but will all be run in the same program

# Setup
# In this section, all packages and modules required for analysis
# Additionally, any code required to provide variables to the data will be done here
# Variables should allow for easier manipulation of the data for the required tasks

# sklearn is required to import the iris dataset
import sklearn as skl

# numpy is required to analyse the dataset
import numpy as np

# imports the OS (Operating System) module, this allows python to interact with the operating system
import os

# matplotlib.pyplot is required to create the histograms and scatter plots
import matplotlib.pyplot as plt

# From sklearn I sppecifically need the datasets module
from sklearn import datasets

import pandas as pd

# Importing the Iris datset
iris = datasets.load_iris()

'''
# To check if the data has been successfully imported and loaded, I print the data.
print(iris)

# provides the target names in the dataset
iris.target_names
print(iris.target_names)
'''

# provides variable names for each target allowing for more efficient coding and manipulation
target = iris.target
target_names = iris.target_names
data = iris.data

# The code below separates out the different variables of each species. 
# This will make it easier when creating the histograms for each variable.
# gives only the seapl length for each species
setosa_sepal_l = data[target == 0, 0]
versicolor_sepal_l = data[target == 1, 0]
virginica_sepal_l = data[target == 2, 0]

# gives only the sepal width for each species
setosa_sepal_w = data[target == 0, 1]
versicolor_sepal_w = data[target == 1, 1]
virginica_sepal_w = data[target == 2, 1]

# gives only the petal length for each species
setosa_petal_l = data[target == 0, 2]
versicolor_petal_l = data[target == 1, 2]
virginica_petal_l = data[target == 2, 2]

# gives only the petal width for each species
setosa_petal_w = data[target == 0, 3]
versicolor_petal_w = data[target == 1, 3]
virginica_petal_w = data[target == 2, 3]

# give aliases to feature names to allow for easier manipulation later, basically separates out each column from the dataset.
# The columns in the dataset are the sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm)
sepal_l = data[:,0]
sepal_w = data[:,1]
petal_l = data[:,2]
petal_w = data[:,3]

#Task 1: Variable Summary
np_data = np.array(data)
column_names = iris.feature_names

# this code creates a loop that loops through each column in the dataset
# it calculates the statistical data for each column
# the statisitical data calculated is: mean, minimum, maximum, standard deviation, and median

# Loops through each column in the dataset, i = each column in the dataset

# opens/creates a file called column_statistics
# this is because of the "w"
# if the file does exist, it won't create a new file but will overwrite the existing file.
with open("column_statistics.txt", "w") as f:
    for i in range(data.shape[1]):
        # extracts column i
        column = data[:, i]
        # prints the name of each column
        print(f"{column_names[i]}:", file=f)
        # calculates and prints each of the statistical data
        # file=f is used to make sure the results are printed in a .txt file and not the vscode terminal
        print("Mean:", float(np.mean(column)), file=f)
        print("Minimum:", float(np.min(column)), file=f)
        print("Maximum:", float(np.max(column)), file=f)
        print("Standard Deviation:", float(np.std(column)), file=f)
        print("Median:", float(np.median(column)), file=f)
        print("", file=f)

# Task 2: Histograms

# creates the folder "Histograms" if it doesn't exist already
os.makedirs("Histograms", exist_ok = True)

# plot feature: Sepal Length (cm)
plt.hist(sepal_l, bins = 20, color = "blue", edgecolor = 'black')
# edgecolor = black, helps outline each bar on the histogram
# bins = 20, put the data into 20 evenly spaced bars. A bins value that is too high or too low can make the data harder to interpret.
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
# plt.xlabel and plt.ylabel add labels to the x and y axes
plt.title("Fig 2.1. Histogram of Sepal Length vs Frquency (cm)")
# plt.tile adds a title to the histogram.
# Save the histogram into the "Histograms" Folder
plt.savefig("Histograms/Fig 2.1. Histogram of Sepal Length vs Frquency (cm).png", dpi=300)
plt.show()
# plt.show() is required to display the histogram, without this the code will still run but won't display the resulting histogram.

# The prpcess is repeated for the ret of the variables
# plot feature: Sepal Width (cm)
plt.hist(sepal_w, bins = 20, color = "green", edgecolor = 'black')
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.2. Histogram of Sepal Width Vs Frequency (cm)")
plt.savefig("Histograms/Fig 2.2. Histogram of Sepal Width Vs Frequency (cm).png", dpi=300)
plt.show()

# plot feature: Petal Length (cm)
plt.hist(petal_l, bins = 20, color = "red", edgecolor = 'black')
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.3. Histogram of Petal Length vs Frequency (cm)")
plt.savefig("Histograms/Fig 2.3. Histogram of Petal Length vs Frequency (cm).png", dpi=300)
plt.show()

# plot feature: Petal Width (cm)
plt.hist(petal_w, bins = 20, color = "yellow", edgecolor = 'black')
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.4. Histogram of Petal Width vs Frequency (cm)")
plt.savefig("Histograms/Fig 2.4. Histogram of Petal Width vs Frequency (cm).png", dpi=300)
plt.show()

# The histograms above display the frequency of the variables, hoever we can gleam more information if we look at the breakdown of the variables between each species.

# plot variable: Sepal Length (cm) for each species
plt.hist(setosa_sepal_l, bins=20, alpha = 0.5, label="Setosa", color="blue", edgecolor='black')
plt.hist(versicolor_sepal_l, bins=20, alpha = 0.5, label="Versicolor", color="green", edgecolor='black')
plt.hist(virginica_sepal_l, bins=20, alpha = 0.5, label="Virginica", color="red", edgecolor='black')
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.5. Histogram of Sepal Length (cm) by Species")
plt.savefig("Histograms/Fig 2.5. Histogram of Sepal Length (cm) by Species.png", dpi=300)
plt.legend()
plt.show()

# plot variable: Sepal Width (cm) for each species
plt.hist(setosa_sepal_w, bins=20, alpha = 0.5, label="Setosa", color="blue", edgecolor='black')
plt.hist(versicolor_sepal_w, bins=20, alpha = 0.5, label="Versicolor", color="green", edgecolor='black')
plt.hist(virginica_sepal_w, bins=20, alpha = 0.5, label="Virginica", color="red", edgecolor='black')
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.6. Histogram of Sepal Width (cm) by Species")
plt.savefig("Histograms/Fig 2.6. Histogram of Sepal Width (cm) by Species.png", dpi=300)
plt.legend()
plt.show()

# plot feature: Petal Length (cm) for each species
plt.hist(setosa_petal_l, bins=20, alpha = 0.5, label="Setosa", color="blue", edgecolor='black')
plt.hist(versicolor_petal_l, bins=20, alpha = 0.5, label="Versicolor", color="green", edgecolor='black')
plt.hist(virginica_petal_l, bins=20, alpha = 0.5, label="Virginica", color="red", edgecolor='black')
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.7. Histogram of Petal Length (cm) by Species")
plt.savefig("Histograms/Fig 2.7. Histogram of Petal Length (cm) by Species.png", dpi=300)
plt.legend()
plt.show()

# plot feature: Petal Width (cm) for each species
plt.hist(setosa_petal_w, bins=20, alpha = 0.5, label="Setosa", color="blue", edgecolor='black')
plt.hist(versicolor_petal_w, bins=20, alpha = 0.5, label="Versicolor", color="green", edgecolor='black')
plt.hist(virginica_petal_w, bins=20, alpha = 0.5, label="Virginica", color="red", edgecolor='black')
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.8. Histogram of Petal Width (cm) by Species")
plt.savefig("Histograms/Fig 2.8. Histogram of Petal Width (cm) by Species.png", dpi=300)
plt.legend()
plt.show()

# The reason for saving the Histograms is that it allows easier access when trying to compare them as I don't have to run the code again or manually save them.

# Task 3: Scatter Plots
# In order to have scatter plots comparing each pair of variables I will require 6 plots
# The plots are as follows:
# 1. Sepal length vs Sepal width
# 2. Sepal length vs Petal length
# 3. Sepal length vs Petal width
# 4. Sepal width vs Petal length
# 5. Sepal width vs Petal width
# 6. Petal length vs Petal width

# Additionally, I have decided to add Linear Regression Lines to the scatter plots.
# This combined with R^2 calculations should provide some insight into the corelation between the variables.

# creates the folder "Scatter Plots" if it doesn't exist already
os.makedirs("Scatter Plots", exist_ok = True)

# 1. Sepal Length vs Sepal width
# Linear regression using numpy
slope, intercept = np.polyfit(sepal_l, sepal_w, 1)
y_pred = slope * sepal_l + intercept
r2 = 1 - np.sum((sepal_w - y_pred) ** 2) / np.sum((sepal_w - np.mean(sepal_w)) ** 2)
# Creating the Scatter Plot
colors = ['blue', 'green', 'red']
for i in range(3):
    plt.scatter(sepal_l[target == i], sepal_w[target == i], color=colors[i], label=target_names[i])
# Create an array of evenly spaced values between the minimum and maximum values of sepal_l
x_vals = np.linspace(min(sepal_l), max(sepal_l), 100)
plt.plot(x_vals, slope * x_vals + intercept, color='black', label='Linear Fit')
# Adding axes labels and scatter plot title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Fig 3.1 Iris Dataset - Sepal Length vs. Sepal Width')
# Displays the R^2 value on the scatter plot with a white background box
plt.text(min(sepal_l) + 0.5, max(sepal_w) - 0.2, f'$R^2 = {r2:.2f}$', fontsize=12, bbox=dict(facecolor='white'))
# Displays a grid on the scatter plot
plt.grid(True)
# Displays a legend showing the what species the colours refer to, the R^2 value, and the Linear Regression Line
plt.legend()
plt.savefig("Scatter Plots/Fig 3.1. Iris Dataset - Sepal Length vs. Sepal Width.png", dpi=300)
plt.show()

# Steps are repeated for the next 5 scatter plots, linear rgeression lines and R^2 calculations, with the required variables for each plot.

# 2. Sepal Length vs Petal Length
slope, intercept = np.polyfit(sepal_l, petal_l, 1)
y_pred = slope * sepal_l + intercept
r2 = 1 - np.sum((petal_l - y_pred) ** 2) / np.sum((petal_l - np.mean(petal_l)) ** 2)
colors = ['blue', 'green', 'red']
for i in range(3):
    plt.scatter(sepal_l[target == i], petal_l[target == i], color=colors[i], label=target_names[i])
x_vals = np.linspace(min(sepal_l), max(sepal_l), 100)
plt.plot(x_vals, slope * x_vals + intercept, color='black', label='Linear Fit')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Fig 3.2 Iris Dataset - Sepal Length vs. Petal Length')
plt.text(min(sepal_l) + 0.5, max(petal_l) - 0.2, f'$R^2 = {r2:.2f}$', fontsize=12, bbox=dict(facecolor='white'))
plt.grid(True)
plt.legend()
plt.savefig("Scatter Plots/Fig 3.2. Iris Dataset - Sepal Length vs. Petal Length.png", dpi=300)
plt.show()

# 3. Sepal length vs Petal Width
slope, intercept = np.polyfit(sepal_l, petal_w, 1)
y_pred = slope * sepal_l + intercept
r2 = 1 - np.sum((petal_w - y_pred) ** 2) / np.sum((petal_w - np.mean(petal_w)) ** 2)
colors = ['blue', 'green', 'red']
for i in range(3):
    plt.scatter(sepal_l[target == i], petal_w[target == i], color=colors[i], label=target_names[i])
x_vals = np.linspace(min(sepal_l), max(sepal_l), 100)
plt.plot(x_vals, slope * x_vals + intercept, color='black', label='Linear Fit')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Fig 3.3 Iris Dataset - Sepal Length vs. Petal Width')
plt.text(min(sepal_l) + 0.5, max(petal_w) - 0.2, f'$R^2 = {r2:.2f}$', fontsize=12, bbox=dict(facecolor='white'))
plt.grid(True)
plt.legend()
plt.savefig("Scatter Plots/Fig 3.3. Iris Dataset - Sepal Length vs. Petal Width.png", dpi=300)
plt.show()

# 4. Sepal Width vs Petal Length
slope, intercept = np.polyfit(sepal_w, petal_l, 1)
y_pred = slope * sepal_w + intercept
r2 = 1 - np.sum((petal_l - y_pred) ** 2) / np.sum((petal_l - np.mean(petal_l)) ** 2)
colors = ['blue', 'green', 'red']
for i in range(3):
    plt.scatter(sepal_w[target == i], petal_l[target == i], color=colors[i], label=target_names[i])
x_vals = np.linspace(min(sepal_w), max(sepal_w), 100)
plt.plot(x_vals, slope * x_vals + intercept, color='black', label='Linear Fit')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Fig 3.4 Iris Dataset - Sepal Width vs. Petal Length')
plt.text(min(sepal_w) + 0.5, max(petal_l) - 0.2, f'$R^2 = {r2:.2f}$', fontsize=12, bbox=dict(facecolor='white'))
plt.grid(True)
plt.legend()
plt.savefig("Scatter Plots/Fig 3.4. Iris Dataset - Sepal Width vs. Petal Length.png", dpi=300)
plt.show()

# 5. Sepal Width vs Petal Width
slope, intercept = np.polyfit(sepal_w, petal_w, 1)
y_pred = slope * sepal_w + intercept
r2 = 1 - np.sum((petal_w - y_pred) ** 2) / np.sum((petal_w - np.mean(petal_w)) ** 2)
colors = ['blue', 'green', 'red']
for i in range(3):
    plt.scatter(sepal_w[target == i], petal_w[target == i], color=colors[i], label=target_names[i])
x_vals = np.linspace(min(sepal_w), max(sepal_w), 100)
plt.plot(x_vals, slope * x_vals + intercept, color='black', label='Linear Fit')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Fig 3.5 Iris Dataset - Sepal Width vs. Petal Width')
plt.text(min(sepal_w) + 0.5, max(petal_w) - 0.2, f'$R^2 = {r2:.2f}$', fontsize=12, bbox=dict(facecolor='white'))
plt.grid(True)
plt.legend()
plt.savefig("Scatter Plots/Fig 3.5. Iris Dataset - Sepal Width vs. Petal Width.png", dpi=300)
plt.show()

# 6. Petal Length vs Petal Width
slope, intercept = np.polyfit(petal_l, petal_w, 1)
y_pred = slope * petal_l + intercept
r2 = 1 - np.sum((petal_w - y_pred) ** 2) / np.sum((petal_w - np.mean(petal_w)) ** 2)
colors = ['blue', 'green', 'red']
for i in range(3):
    plt.scatter(petal_l[target == i], petal_w[target == i], color=colors[i], label=target_names[i])
x_vals = np.linspace(min(petal_l), max(petal_l), 100)
plt.plot(x_vals, slope * x_vals + intercept, color='black', label='Linear Fit')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Fig 3.6 Iris Dataset - Petal Length vs. Petal Width')
plt.text(min(petal_l) + 0.5, max(petal_w) - 0.2, f'$R^2 = {r2:.2f}$', fontsize=12, bbox=dict(facecolor='white'))
plt.grid(True)
plt.legend()
plt.savefig("Scatter Plots/Fig 3.6. Iris Dataset - Petal Length vs. Petal Width.png", dpi=300)
plt.show()

# The reason for saving the scatter plots is that it allows easier access when trying to compare them.

# Additional Analysis: Heatmap
# Create a DataFrame of the Iris Dataset using Pandas.
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
# Computes the corealation between the variables and displays the result
corr = df_iris.corr()
# Create the heatmap
plt.figure()
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
# Set tick marks and labels
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
# Add information to the heatmap
plt.title('Fig 4.1 Variable Correlation Heatmap - Iris Dataset')
plt.savefig("Fig 4.1 Variable Correlation Heatmap - Iris Dataset.png", dpi = 300)
plt.tight_layout()
plt.show()