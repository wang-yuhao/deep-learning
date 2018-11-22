
# coding: utf-8

# # Deep Learning and AI - WiSe 18/19
# 
# * Lecturer: Prof. Dr. Matthias Schubert
# * Assistants: Sebastian Schmoll, Sabrina Friedl
# 

# # 1st Tutorial - 10/22/18
# 
# In this tutorial, we want to give you a short introduction in Python and some insights in the basic usage of some common libraries in the scope of Data Science.

# <strong>Installing Python</strong>
# 
# * Anaconda distribution (recommended)
# 
# Visit the website https://www.continuum.io/downloads and download the Anaconda distribution for the Python 3.6 version. Make yourself familiar with the jupyter Python notebook which is included in the anaconda installation. If preferred, install also an IDE/editor of your choice, e.g. PyCharm.
# The Anaconda distribution comes along with a lot of libraries (numpy, scipy, pandas, ...) which otherwise have to be installed individually. IF you need an additional library which is not initially included in Anaconda, you can install the lib via "conda install PACKAGENAME". (Further information can be looked up in the documentation: https://conda.io/docs/index.html)
# 
# * W/o distribution
# 
# Visit https://www.python.org/downloads/ and download your preferred python version. Next, go to https://pip.pypa.io/en/stable/installing/ and install $pip$. With $pip$ being installed one can install each package individually. For Example, to install the packages $numpy, scipy, matplotlib, ipythong, jupyter, pandas$, execute the following command:<br/>
# pip install --user numpy scipy matplotlib ipython jupyter pandas
# If you need an additional package during the course, don't forget to install the libraries which might be handy. 

# <strong>First steps</strong>

# <b>Assigning Values to Variables.</b> Create variables and assign numbers, strings, floating values to them. 

# <b>Variable types</b>
# Python has five standard data types −
# <ul>
# <li>Numbers</li>
# <li>String</li>
# <li>List</li>
# <li>Tuple</li>
# <li>Dictionary</li>
# </ul>
# 
# <b>Lists.</b> Create a list which contains all numbers from 0 to 10

# <b>Loops and conditionals.</b> Using the created list, print each element of the created list if its is an odd number, by using a loop and conditionals. Try using different type of loops.

# <b>List Comprehensions.</b> Now, generate a list which contains all numbers from 0 to $n$ which have been squared using list comprehensions.

# <b>Functions. </b> Write a function which takes an integer $n$. The function first creates a list of numbers from $0$ to $n$. Then, squares each number of the list. Further each of the squared numbers is tested if it is odd. All odd numbers are then appended to a new list. The function returns the list of odd (squared) numbers.

# <b>Assignments. </b> Given a list $a=['I','like','cookies']$ and another list $b=a$. Replace in the list $b$ the word $'cookies'$ with $'apples'$. Finally, print both lists ($a$ and $b$). What do you observe? What leads to the observed behavior?

# <b>Shallow Copy I.</b> Given a list $a=['I','like','cookies']$ and another list which takes a shallow copy of $a$, $b=a[:]$. Like in the previous assignment, replace in the list $b$ the word $'cookies'$ with $'apples'$. Finally, print both lists ($a$ and $b$). What do you observe now?

# <b>Shallow Copy II.</b> Now, we are given a list $a = ['I', 'like', ['chocolate', 'cookies']]$. Another list $b = deepcopy(a)$ takes this time a deep copy from $a$. Change now the work $'cookies'$ with $'apples'$ in $b$. Print both lists ($a$ and $b$). What do you observe now?<br/>
# <i>Hint: For deep copy. first type: from copy import deepcopy</i>

# <b>Dictionaries I.</b> Create a dictionary with $n$ entries, where the  keys are enumerated from $0$ to $n-1$ and the values are their corresponding keys squared. Use list comprehensions. <br/>
# Example for expected result: $n = 7; \{0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36\}$

# <b>Dictionaries II.</b> Use the dictionary from the previous assignment. Write a list comprehension to get a list of all the  keys of the  dictionary. 

# <b>Lambda functions.</b> Write a list comprehension which takes a number $n$ and returns a list with even numbers, using a lambda function.

# <b>map. </b> First, write a function which takes a length in $inch$ and returns a length in $cm$. Given a list $l$ with lengths in $inches$: $l=[4,4.5,5,5.5,6,7]$. Write a list comprehension which takes $l$ and returns a list with all values converted to $cm$ using $map()$.

# <b>filter. </b> Write a list comprehension which filters the list $l$ from the assignment above by returning only sizes between $4$ and $6$ $inches$.

# <b>reduce. </b> Write a list comprehension which reduces the list $l$ by summing up all lenghts.<br/>
# <i>Hint: for using the reduce function, you need to import it first by: from functools import reduce</i>

# <b>List reverse.</b> Given the following list $a=[0,1,2,3,4,5]$. Write a function which reverses the list.

# <b>Zipping of lists.</b> Given the following two lists, wher eone list represents the $x-Coordinate$ and another one the $y-Coordinate$:<br/>
# * $xcoors = [0,1,2,3,4,5]$
# * $ycoors = [6,7,8,9,10,11]$
# 
# Write a function which zips the  two lists to a list of coordinate-tuples:<br/>
# * $xycoors = [(0,6),(1,7),(2,8),(3,9),(4,10),(5,11)]$

# <b>Unzipping of lists.</b> Now, we are given a list of data points where the first dimension of each data point represents the age of a person and the second dimension the amount of money spent for chocolate per month in euro:
# * $chocage = [(20,8), (33,18), (27,14),(66,23),(90,100)]$
# 
# Write a function which takes the  list and separates it into two lists, one containing the ages and another one containing its corresponding amount of money spent for chocolate. The result would be e.g.:
# * $age = [20,33,27,66,90]$
# * $money\_spent = [8,18,14,23,100]$

# <b>Object oriented programming I. </b> We deal now with object oriented programming in Python. For this purpose perform the following steps: 
# * Write a $Point$ class. A $Point$ class takes and $x$ and $y$ coordinate as an argument.
# * Further this class shall have a setter method $setXY$ which takes and $x$ and $y$ coordinate and sets the attributes to the new provided values.
# * The class shall also have a getter method $getXY$ which returns the current $x$ and $y$ coordiantes of the point.
# * Write a method distance which takes another $point$ object and returns the euclidean distance between the provided point and the point itself. <i>Hint: Take import math to use math.sqrt(value) in order to compute the square root.</i>

# <b>Object oriented programming II.</b> In a next step, the task is to create a class $Shape$. For this purpose perform the following steps:
# * Create a class $Shape$ which takes a name and a color as parameters.
# * Define a method $area$ which just returns $0.0$.
# * Define a method $perimeter$ which just return $0.0$.
# 
# Now, create a class Rectangle which inherits from $Shape$ and in which you $implement$ the $area$ and $perimeter$ methods.

# <b>Numpy I - some basic functions</b>. In this block, you will become familiar with the numpy library and some of its basic functionality. Please also consider to consult the documentation  https://docs.scipy.org/doc/numpy-dev/index.html if needed. Solve the following tasks:
# * Create an numpy array of floats containing the numbers from $0$ to $4$.
# * Create the following matrix as a numpy matrix: $M = [[1,2,3], [4,5,6]]$.
# * Get the shape of the matrix $M$.
# * Check if the value $2$ is in $M$.
# * Given the array $a = np.array([0,1,2,3,4,5,6,7,8,9], float)$. Reshape it to an $5\times2$ matrix.
# * Transpose the previously introduced matrix $M$.
# * Flatten matrix $M$.
# * Given the array $b = np.array ([0,1,2,3], float)$. Increase the dimensionality of $b$.
# * Create and $3\times3$ identity matrix.

# <b>Numpy II - linear algebra and statistics. </b> This assignemtn has its focus on numpy function of the linear algebra and statistics domain. Solve the following tasks using numpy:
# * Given the following two numpy array: $a=np.array([1,2,3], float)$, $b=([4,5,6],float)$. Compute the dot product of $a$ and $b$
# * Given the following matrix $M = [[1,2,3], [4,5,6], [7,8,9]]$, compute the determinant of $M$ by using the $linalg$ package of the numpy library.
# * Compute the eigenvalues and eigenvectors of $M$
# * Compute the inverse of $M$
# * Given the numpy array $c=np.array([1,4,3,8,3,2,3], float)$, compute the mean of $c$
# * using $c$, compute the median.
# * given the following matrix $C=[[1,1], [3,4]]$, compute the covariance of $C$.

# <b>Matplotlib - Plotting figures in Python. </b> In this assignment we are finally going to become familiar with the plotting library of Python. For this we solve the following tasks below. Please consider to consult the documentation if needed: https://matplotlib.org/contents.html.
# 
# * Given a list of data points : $dpts=[(3,3),(4,5),(4.5,6),(9,7)]$. Plot the function using $plt.plot(xcoors, ycoors)$
# * You are given two tiny clusters $c_1 = [(1,2),(3,1),(0,1),(2,2)]$ and $c_2=[(12,9),(8,10),(11,11), (14,13)]$. Plot them in a scatter plot using $plt.scatter(xcoors, ycoors)$, where $c_1$ and $c_2$ have different colors. The $x-axis$ represents the time spent at a parking lot in hours, and the $y-axis$ represents the money spent in euro. Create axis labels for your figure.
# * Take the two clusters $c_1$ and $c_2$ together and compute their pairwise distances, storing them in a matrix. Plot the resulting matrix as a heatmap using $plt.imshow(my\_matrix, cmap='coolwarm')$.

# # End of first Tutorial
