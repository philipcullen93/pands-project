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

# matplotlib.pyplot is required to create the histograms and scatter plots
import matplotlib.pyplot as plt

# From sklearn I sppecifically need the datasets module
from sklearn import datasets

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

# plot feature: Sepal Length (cm)
plt.hist(sepal_l, bins = 20, color = "blue", edgecolor = 'black')
# edgecolor = black, helps outline each bar on the histogram
# bins = 20, put the data into 20 evenly spaced bars. A bins value that is too high or too low can make the data harder to interpret.
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
# plt.xlabel and plt.ylabel add labels to the x and y axes
plt.title("Fig 2.1. Histogram of Sepal Length vs Frquency (cm)")
# plt.tile adds a title to the histogram.
plt.show()
# plt.show() is required to display the histogram, without this the code will still run but won't display the resulting histogram.

# The prpcess is repeated for the ret of the variables
# plot feature: Sepal Width (cm)
plt.hist(sepal_w, bins = 20, color = "green", edgecolor = 'black')
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.2. Histogram of Sepal Width Vs Frequency (cm)")
plt.show()

# plot feature: Petal Length (cm)
plt.hist(petal_l, bins = 20, color = "red", edgecolor = 'black')
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.3. Histogram of Petal Length vs Frequency (cm)")
plt.show()

# plot feature: Petal Width (cm)
plt.hist(petal_w, bins = 20, color = "yellow", edgecolor = 'black')
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.title("Fig 2.4. Histogram of Petal Width vs Frequency (cm)")
plt.show()

# The histograms above display the frequency of the variables, hoever we can gleam more information if we look at the breakdown of the variables between each species.

# Task 3: Scatter Plots
# In order to have scatter plots comparing each pair of variables I will require 6 plots
# The plots are as follows:
# 1. Sepal length vs Sepal width
# 2. Sepal length vs Petal length
# 3. Sepal length vs Petal width
# 4. Sepal width vs Petal length
# 5. Sepal width vs Petal width
# 6.Petal length vs Petal width

# 1. Sepal Length vs Sepal width
# Creates a scatter plot using the variables provided
plt.scatter(sepal_l[target==0], sepal_w[target==0], color = 'red', label = target_names[0], alpha = 1)
plt.scatter(sepal_l[target==1], sepal_w[target==1], color = 'blue', label = target_names[1], alpha = 1)
plt.scatter(sepal_l[target==2], sepal_w[target==2], color = 'green', label = target_names[2], alpha = 1)

# Add labels and title to the scatter plot
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Fig 3.1. Iris Dataset: Sepal Length vs. Sepal Width')
# Adds a grid for easier comparison 
plt.grid(True)
# shows the legend using the labels provided
plt.legend()
# Renders and displays the plot
plt.show()