# pands-project

# Project Title: Investigation of Iris Dataset

## Contents
This repository contains:
- python file iris-analysis.py
- README.md
- Histograms Folder
- Scatter Plot Folder
- Additional Analysis Folder
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
- Discussion
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
The data for this project original comes from "The Use of Multiple Measuremanets in Taxonomic Problems" by R. A. Fisher. The paper written in 1936, serves as a foundation for multivariate statisitcs. In the paper, Fisher took measurements of three different varients of the Iris flower. The Iris flowers used in the study were  *Iris setosa*, *Iris versicolor*, and *Iris virginica*. For each flower he measured the petal length (cm), petal width (cm), sepal length (cm), and the sepal width (cm). from this Fisher developed a statiscal method, linear discriminant. This method is used to identify a clear combination of features for two or more objects while being able to discriminate between them [1].

### Why is this important in data analytics
Fisher's linear discrimiant statistical model served as the foundation for Linear Disciminant Analysis (LDA), also known as normal discriminant analysis (NDA) or discriminant function analysis (DFA). This model is used in machine learning, bioinformatics, and pattern recognicition. This allows analysts to take large complex datasets and simplify them while still preserving each classes unique information. By doing this it allows for better visualisation and interpretation of highly complex datsets [2].

## Required Modules
- sklearn
- NumPy
- Matplotlib.pyplot
- OS
- Pandas

## How to Run the Program
To run the program:

1. Download or clone the pands-project.git repository from https://github.com/philipcullen93/pands-project.git

2. In VSCode run the program python.iris-analysis.py

## How the Program Works
Below offers a more indepth look at what each task does.

### Setup
In the beginning of the code there is an initial setup step. The code provided in this section is used to import the data and any required modules. Furthermore, it isolates several features of the dataset, using variable names. Variable Naming allows the data to be more easily manipulated dueing tasks. There is additional code sections that are not required for the program to run successfully but that can be implemented to check to ensure the data being imported is correct and has been successfully imported [3] [4] [5] [6].

### Task 1: Variable Summary
This task uses the program to calculate key statistics of the variables — Mean, Minimum, Maximum, Standard Deviation, and Median — and save the results in a .txt file called "variable_summary".

In order to do this effectively, the code needs to run through 4 important steps:
1. Looping Through Each Column [8]
- for i in range(data.shape[1]):
  - Loops through each column in the NumPy data.
  - data.shape[1] returns the total number of columns.

2. Extracting the Data in Each Column Using NumPy Slicing
- column = data[:, i]
  - Uses NumPy slicing to extract column i from data.
  - : means "all rows", so data[:, i] means "column i of all rows"

3. Writing the Results into the .txt file. [7]
- print(f"{column_names[i]}:", file=f)
  - Writes the name of the current column to the file.
  - file=f makes sure the output from the script is written into the .txt file and not the VSCode terminal.

4. Calculating the Statisitcs [9] [10] [11] [12] [13]
- print("Mean:", float(np.mean(column)), file=f)
  - Uses the NumPy mean function to calculate the mean of each column
  - Adds the result to the variable_summary.txt file
  - This is repeated using the minimum, maximum, standard deviation, and median Numpy functions.

### Task 2: Histograms of Variables
This task uses the program to create 4 histograms showing the frequency of variables, it then creates 4 more histograms showing the breakdown of the variables between iris species.

The program also creates a folder called "Histograms", if one doesn't already exist, and populates it with the Histograms produced by the script.

Below is how the script works for one of the Histograms (Fig 2.1. Sepal Length (cm) vs Frequency). For the other the code remains realtively the same.

Histogram Fig 2.1. Sepal Length vs Frequency [14]
1. Create the "Histograms" folder.
- os.makedirs("Histograms", exist_ok=True)
  - Creates a folder named Histograms if it doesn't already exist.
  - If one exists the script will not create a second.

2. Plot the Histogram [15]
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

4. Save the Histogram [16] [17]
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

### Task 3: Scatter Plots

As with Task 2: Histograms, provided below is the script for generating one of the Scatter Plots, performing the R^2 calculation and adding the Linear Regression Line, in this case Fig 3.1. Iris Dataset - Sepal Length vs. Sepal Width. 

The other scatter plots and calculations aare done in the same manner, just changing the variables.

- slope, intercept = np.polyfit(sepal_l, sepal_w, 1) [19] [20]
  - Performs a 1st-degree polynomial fit to sepal_l (x-values) and sepal_w (y-values).
      - 1st-degree polynomial is a function in the form: y = mx + b (line equation)
  - Returns the slope and intercept of the best-fit line.
- y_pred = slope * sepal_l + intercept
  - Calculates predicted y-values (Sepal Width) using the line equation.
- r2 = 1 - np.sum((sepal_w - y_pred) ** 2) / np.sum((sepal_w - np.mean(sepal_w)) ** 2) [22]
  - Calculates R^2 (coefficient of determination) 
- colors = ['blue', 'green', 'red']
- for i in range(3):
- plt.scatter(sepal_l[target == i], sepal_w[target == i], color=colors[i], label=target_names[i]) [18]
  - Loops through the 3 species and plots each group using a different color (blue, green, red) stated above.
  - target == i filters the data to only that species.
  - label=target_names[i] sets the names in the legend.
- x_vals = np.linspace(min(sepal_l), max(sepal_l), 100)
  - Creates a smooth line using 100 x-values. Ensures even spacing.
  - Plots the regression line in black with a label for the legend.
- plt.plot(x_vals, slope * x_vals + intercept, color='black', label='Linear Fit') [21]
  - Plots the regression line in black and provides the label used in the legend.
- plt.text(min(sepal_l) + 0.5, max(sepal_w) - 0.2, f'$R^2 = {r2:.2f}$', fontsize=12, bbox=dict(facecolor='white'))
  - Displays the R^2 value on the scatter plot.

### Additional Analysis: Heatmap
This script creates a heatmap using the correlation matrix between the values.

It provides a visual showing the relationship between the variables, and thus can provide useful insights.

- df_iris = pd.DataFrame(iris.data, columns=iris.feature_names) [23]
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
- plt.imshow(corr, cmap='coolwarm', interpolation='nearest') [24] [25]
  - plt.figure() starts a new figure.
  - plt.imshow() displays the corr matrix as an image, where colors represent values.
  - cmap='coolwarm': Provides a color scale from blue (low correlation) to red (high).
  - interpolation='nearest': This ensures that each cell is a solid block of color.
- plt.colorbar()
  - Adds a color scale legend to the side of the heatmap to show what the colors represent (e.g., red = 1.0, blue = -1.0).

## Discussion

### Task 1: Variable Summary
From the variable summary there is some information we can learn about the Iris Dataset.

- Petal features (length and width) vary more across the dataset than sepal features, this makes them more useful for distinguishing between the three species of Iris.
  - This is due to them having high variability and broad range.
  - Petal length in particular has widest range and highest variability, this suggests it could be a strong candidate for separating species, particularly Setosa vs. Virginica Iris species.
- Sepal Width on the otherhand has the lowest standard deviation. This makes it a very consistent variable and thus may be a poor candidate for identifying individual Iris species.

### Task 2: Histograms
The Histograms can help support the observations seen when looking at the variable summary.

Below are the observation made by looking at the histograms plotting each variable against the frequency.

All histograms with their associate data and Figure number (Fig X.X.) can be found in the Histograms folder.

- Fig 2.1. Sepal length varies in frequency over the range. This indicates a good variability between species.
- Fig 2.2. Sepal Width is more clustered. Since it is more clustered, there is less variation, further supporting the idea that it may not be ideal when trying to effectively classify species.
- Fig 2.3. When looking at the Histogram for Petal Length, there is a sharp peak around 1.5 cm, this suggests that it may belong to a single species, while the other range (4 cm - 6 cm) represent the other two species. This provides more insight as to the idea that petal length may be a good variable to differeniate species from one another.
- Fig 2.4. As with Petal Length, Petal Width also has a sharp peak (approx 0.25 cm - 0.75 cm , likely belonging to a single Iris species. This suggests it may also be useful when trying to distinguish between species.

From the first 4 Histogras displaying each variable against frequency. We have more evidence backing up the information provided in Task 1: Variable Summary. At this point Petal Length and Petal Width are strong candidates to identify the Iris Species. 

By breaking it down further and plotting each variable on the histograms by species, we can find more evidence to backup our earlier observations.

- Fig 2.5. There is a lot of overlap on this histogram between the various species. While we can see high peaks for Setosa (blue) and Virginica (red), the high degree of overlap suggests that Sepal Length remains a poor candidate for distinguishing between species.
- Fig 2.6. Similarly to Fig 2.5., the high degree of overlap shows that Sepal Width remains a poor candidate for separating out species.
- Fig 2.7. Petal Length shows a lot less overlap between species, particularly for Setosa where it has no overlap with other species. Furthermore, the is significantly less overlap between Veriscolor (green) and Virginica. This reinforces the idea that Petal Length is the best candidate for distinguishing between Iris species.
- Fig 2.8. As with Fig 2.7., we can clearly see there is significantly less overlap. The three species bers are clearly represented and separated. Thus, Petal Width is a good candidate for separating the Iris species.

The above observations suggest that using the Petal Length and Petal Width we can easily classify the Iris species. 

While Sepal Length and Sepal Width remain poor candidates, it is possible that graphing them against Petal Length and Petal Width could make them more useful for classification.

# Task 3: Scatter Plots
Combining scatter plots with R^2 values and linear regression lines helps us observe the relationships between the different species variables. It also proves insight into the physical differences between the species.

R^2 values cover a range from 0 to 1. The closer a value is to 1 the more strongly related the variables are.

All scatter splots with their associate data and Figure number (Fig X.X.) can be found in the Scatter Plots folder.

- Fig 3.1. Sepal length vs Sepal Width: The first scatter plot showing Sepal Length vs. Sepal Width provides an R^2 value of 0.01. This indicates that there is a very poor relationship between Sepal Length and Sepal Width. There is no clear trend, as the data points are widely scatter. This supports the idea that neither Sepal Length and Sepal Width are useful for separating the Iris species. Additionally, it shows that using Sepal Length would not be good for predicting sepal width, and vice versa.
- Fig 3.2. Sepal Length vs Petal Length: This scatter plots points are more clustered with an R^2 value of 0.76. There is a clearer trend in the data with more points falling closer to the linear regression line. This suggests that we could use Sepal length to predict Petal Length in Iris species. We can also see that there is a clearer separation between the species, we see that setosa tends to have short sepals and petals, while virginica has the large sepals and petals. This highlights the physical difference between the Iris species which could aid in classification.
- Fig 3.3. Sepal Length vs Petal Width: The data points in this scatter plot are less tightly clustered, particularly for the Verisicolor and Viginica species, making the trend harder to observe. The R^2 value of 0.67 suggests that there is a moderate relationship between these two variables. However, the correlation is not strong enough to reliably use Sepal Length to predict Petal Width. This is especially evident in the Virginica species, which shows considerable variation in its data points.
- Fig 3.4. Sepal Width vs Petal Length: There is significant scattering of data points across all Iris species. This is evident by the R² value of 0.18, indicating a very weak relationship between Sepal Width and Petal Length. As a result, Sepal Width cannot be utilised as a predictor of Petal Length. This further suggests that the physical differences between species are not strongly displayed through the relationship between these two features. Sepal Width does not vary consistently with Petal Length across the species, this makes it less useful for distinguishing or classifying them
- Fig 3.5. Sepal Width vs Petal Width: Similarly to Fig 3.4. there is an extreme amount of scattering of the data points. It has a lower R^2 value of 0.13, this shows an even weaker relationship between the two variables. Therefore, Sepal Width is not a good indicator of Petal Length. Additionally, due to the large degree of scattering, the physical differences of the flowers are not expressed through the relationship of these values. 
- Fig 3.6. Petal Length vs Petal Width: This plot displays a high degree of clustering of the data points. Each set of data points is grouped tightly together with a small degree of overlap. The R^2 value of 0.93, suggests a storng linear relationship between these two variables. Thus, we can see that Petal Length is a good predictor of Petal Width. From a pysical classification standpoint, it shows that Setosa has small short petals, Verisicolor has moderately sized petals, and Virginica has wide long petals. This provides evidence that Petal Length and Width can be used to classify the individual Iris species. It further supports the data seen in Task 1: Variable Summary and Task 2: Histograms.

### Additional Analysis: Heatmap

The heatmap can be found in the Additional Analysis folder.

The heatmap allows us to make several obervations:
- There is a strong positive correlation between petal length and petal width, seen previoisly in other tasks.
- There is a strong positive correlation between sepal length and both petal length, and petal width.
- A negative correlation between sepal width and the other features of the dataset.
- Interestingly, sepal length has a positive correlation with petal length and width.

From these observations we can make several conclusions:
- Petal length and width are highly informative and strongly related to each other.
- Sepal length correlates with both petal length and width, suggesting sepal length can be used to help distinguish the species when observed with petal length and width.
- Sepal width behaves differently from the other features and therefore is less useful for distinguishing between iris species on its own.
- It further provides support for the observation that petal length and petal width may be used as the primary features for classification of species.
- 
## References
1. Source of the Paper "The Use of Multiple Measuremanets in Taxonomic Problems" by R. A. Fisher: https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x

2. Linear Discrimination Analysis: https://www.ibm.com/think/topics/linear-discriminant-analysis#:~:text=Linear%20discriminant%20analysis%20(LDA)%20is,helps%20optimize%20machine%20learning%20models.

3. Loading the Iris Dataset: https://scikit-learn.org/stable/datasets/toy_dataset.html

4. Importing Packages and Modules: https://docs.python.org/3/tutorial/modules.html

5. Creating Python Variables: https://www.w3schools.com/python/python_variables.asp

6. Numpy Array Creation: https://numpy.org/doc/stable/user/basics.creation.html

7. Reading and Writing Files in Python: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
  
8. Python for Loops: https://www.w3schools.com/python/python_for_loops.asp

9. Numpy Mean: https://docs.vultr.com/python/third-party/numpy/mean

10. Numpy Minimum: https://docs.vultr.com/python/third-party/numpy/minimum

11. Numpy Maximum: https://docs.vultr.com/python/third-party/numpy/maximum

12. Numpy Standard Deviation: https://docs.vultr.com/python/third-party/numpy/std

13. Numpy Median: https://docs.vultr.com/python/third-party/numpy/median

14. Making a Directory/Folder in Python: https://docs.python.org/3/library/os.html#os.makedirs

15. Plotting Histograms using Matplotlib.pyplot: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/

16. Saving an Image as a .png file: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

17. Saving a file in a Folder in Python: https://stackoverflow.com/questions/55400992/create-a-folder-in-the-directory-and-save-files-in-the-new-folder

18. Using Matplotlib.pyplot to Create Scatter Plots: https://www.w3schools.com/python/matplotlib_scatter.asp

19. Using NumPy.polyfit: https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html

20. Adding a Linear Regression Line using numpy.polyfit: https://data36.com/linear-regression-in-python-numpy-polyfit/

21. Adding a Linear Regression Line to a Scatter plot: https://www.statology.org/scatterplot-with-regression-line-python/

22. Calculating R^2 using NumPy and Python: https://stackoverflow.com/questions/893657/how-do-i-calculate-r-squared-using-python-and-numpy
  
23. Corelations in Panda: https://www.w3schools.com/python/pandas/pandas_correlations.asp#:~:text=Finding%20Relationships,column%20in%20your%20data%20set.

24. Creating a Heatmap using Matplotlib: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html

25. Analysing Heatmaps: https://medium.com/@kulkarni.madhwaraj/heatmap-analysis-using-python-seaborn-and-matplotlib-f6f5d7da2f64
