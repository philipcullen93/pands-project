# pands-project

# Project Title: Investigation of Iris Dataset

## Contents
This repository contains:
- python file iris-analysis.py
- README.md
- Histograms Folder
- Scatter Plot Folder
- column_statistics.txt
- .gitignore

## Table of Contents:
This README.md contains:
- Project Title
- Project Overview
- Summary of the Research Paper
- The Modules Required for the Program
- Information on How to Run the Program
- Information on How the Program Works
- A Discussion
- References

## Project Overview
This project intends to investigate the Iris Dataset using several different analytical techniques and code. 

In order to do this, a program will be created that breaks down and outlines several features of the dataset.

The program title is analysis.py and should do the following:
- Output a summary of each variable into a single text file.
- Save a histogram of each variable to .png files.
- Output a scatter plot of each pair of variables.

Additonally, other analysis techniques may be used to further analyse the data.

## Summary of Paper
The data for this project original comes from "The Use of Multiple Measuremanets in Taxonomic Problems" by R. A. Fisher. The paper written in 1936, serves as a foundation for multivariate statisitcs. In the paper, Fisher took measurements of three different varients of the Iris flower. The Iris flowers used in the study were  *Iris setosa*, *Iris versicolor*, and *Iris virginica*. For each flower he measured the petal length (cm), petal width (cm), sepal length (cm), and the sepal width (cm). from this Fisher developed a statiscal method, linear discriminant. This method is used to identify a clear combination of features for two or more objects while being able to discriminate between them.

### Why is this important in data analytics
Fisher's linear discrimiant statistical model served as the foundation for Linear Disciminant Analysis (LDA), also known as normal discriminant analysis (NDA) or discriminant function analysis (DFA). This model is used in machine learning, bioinformatics, and pattern recognicition. This allows analysts to take large complex datasets and simplify them while still preserving each classes unique information. By doing this it allows for better visualisation and interpretation of highly complex datsets.

## Required Modules
- sklearn
- NumPy
- Matplotlib.pyplot

## How to Run the Program
To run the program:

1. Download or clone the pands-project.git repository from https://github.com/philipcullen93/pands-project.git

2. In VSCode run the program python.iris-analysis.py

## How the Program Works
Below offers a more indepth look at what each task does.

### Setup
In the beginning of the code there is an initial setup step. The code provided in this section is used to import the data and any required modules. Furthermore, it isolates several features of the dataset, using variable names. Variable Naming allows the data to be more easily manipulated dueing tasks. There is additional code sections that are not required for the program to run successfully but that can be implemented to check to ensure the data being imported is correct and has been successfully imported.

### Task 1: Variable Summary
This task uses the program to calculate key statistics of the variables — Mean, Minimum, Maximum, Standard Deviation, and Median — and save the results in a .txt file called "column_ststistics".

In order to do this effectively, the code needs to run through 4 important steps:
1. Looping Through Each Column
- for i in range(data.shape[1]):
  - Loops through each column in the NumPy data.
  - data.shape[1] returns the total number of columns.

2. Extracting the Data in Each Column Using NumPy Slicing
- column = data[:, i]
  - Uses NumPy slicing to extract column i from data.
  - : means "all rows", so data[:, i] means "column i of all rows"

3. Writing the Results into the .txt file.
- print(f"{column_names[i]}:", file=f)
  - Writes the name of the current column to the file.
  - file=f makes sure the output from the script is written into the .txt file and not the VSCode terminal.

4. Calculating the Statisitcs
- print("Mean:", float(np.mean(column)), file=f)
  - Uses the NumPy mean function to calculate the mean of each column
  - Adds the result to the column_statistics.txt file
  - This is repeated using the minimum, maximum, standard deviation, and median Numpy functions.

## Discussion

## References
