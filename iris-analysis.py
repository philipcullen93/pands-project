# This program is designed to analyse the Iris dataset
# There are three main tasks associated with this program
# 1. Output a summary of each variable into a single text file
# 2. Save a histogram of each variable into .png files
# 3. Output a scatter plot of each pair of variables
# Each task will be highlighted with their own section but will all be run in the same program

# Setup
# In this section, all packages and modules required for analysis

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

# To check if the data has been successfully imported and loaded, I print the data.
print(iris)


