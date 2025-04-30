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
