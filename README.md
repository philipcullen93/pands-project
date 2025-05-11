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

### Task 2: Histograms of Variables
This task uses the program to create 4 histograms showing the frequency of variables, it then creates 4 more histograms showing the breakdown of the variables between iris species.

The program also creates a folder called "Histograms", if one doesn't already exist, and populates it with the Histograms produced by the script.

Below is how the script works for one of the Histograms (Fig 2.1. Sepal Length (cm) vs Frequency). For the other the code remains realtively the same.

Histogram Fig 2.1. Sepal Length vs Frequency
1. Create the "Histograms" folder.
- os.makedirs("Histograms", exist_ok=True)
  - Creates a folder named Histograms if it doesn't already exist.
  - If one exists the script will not create a second.

2. Plot the Histogram
- plt.hist(sepal_l, bins = 20, color = "blue", edgecolor = "black")
  - Plots the histogram for the variable sepal_l (Sepal Length).
  - bins = 20: Divides the data into 20 even spaces
  - color="blue": Sets the bar color. Without this, the colour defaults to blue.
    - More important for the other histograms, that other colours are selected as to help differentiate between them.
  - edgecolor="black": Outlines each bar to make them visually distinct, and easier to read data.
 
  3. Add Axis Labels and Title
- plt.xlabel("Sepal Length (cm)")
- plt.ylabel("Frequency")
- plt.title("Fig 2.1. Histogram of Sepal Length vs Frquency (cm)")
  - Adds an x-axis label, y-axis label, and title to the histogram.

4. Save the Histogram
- plt.savefig("Histograms/Fig 2.1. Histogram of Sepal Length vs Frquency (cm).png", dpi=300)
  - Saves the resulting histogram in the Histograms folder as a .png file.
  - dpi = 300 ensures the output is in a high resolution.
 
5. Display the Histogram
- plt.show()
  - Displays the histogram
  - This will display the histogram in the Python environment.
  - However, if this line of code is left out the histogram will still save to the Histogram folder.
 
For the second set of histograms where it displays the breakdown of variables between the different species the code changes slightly.

1. Plotting the Histogram for Species Variable Breakdown
- plt.hist(setosa_sepal_l, bins=20, alpha = 0.5, label="Setosa", color="blue", edgecolor='black')
- plt.hist(versicolor_sepal_l, bins=20, alpha = 0.5, label="Versicolor", color="green", edgecolor='black')
- plt.hist(virginica_sepal_l, bins=20, alpha = 0.5, label="Virginica", color="red", edgecolor='black')
  - bins=20: Divides the data into 20 intervals (bars).
  - alpha=0.5: Makes the bars 50% transparent, this is important as it make overlapping areas are visible.
  - label="Setosa": Adds a legend entry for this dataset. The same is done for Veriscolor and Virginica.
  - color="blue": Fills the bars with blue. For Veriscolor blue is changed to "green", and for Virginica blue is changed to "red".
  - edgecolor='black': Outlines each bar in black.
 
### Additional Analysis: Heatmap
This script creates a heatmap using the correlation matrix between the values.

It provides a visual showing the relationship between the variables, and thus can provide useful insights.

- df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
  - Converts the Iris dataset into a Pandas DataFrame and assigns names to the columns
  - iris.data is the variable values
  - iris.feature_names provides names for the columns (e.g., "sepal length (cm)").
- corr = df_iris.corr()
  - Computes the correlation matrix
  - Correlation values range from 1 to -1
    - 1 means perfect positive correlation between variables.
    - 0 means no correlation between variables.
    - -1 means perfect negative correlation between variables.
- plt.figure()
- plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
  - plt.figure() starts a new figure.
  - plt.imshow() displays the corr matrix as an image, where colors represent values.
  - cmap='coolwarm': Provides a color scale from blue (low correlation) to red (high).
  - interpolation='nearest': This ensures that each cell is a solid block of color.
- plt.colorbar()
  - Adds a color scale legend to the side of the heatmap to show what the colors represent (e.g., red = 1.0, blue = -1.0).

## Discussion

## References
