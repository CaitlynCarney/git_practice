import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1. How many negative numbers are there?
number_of_negs = a < 0
count = np.count_nonzero(number_of_negs)
count

#2. How many positive numbers are there?
number_of_pos = a > 0
count = np.count_nonzero(number_of_pos)
count

#3. How many even positive numbers are there?
even_and_pos_numbers = a > 0 & a % 2 == 0
count = np.count_nonzero(even_and_pos_numbers)
count
#or
number_of_pos = a > 0
count_pos = np.count_nonzero(number_of_pos)
print(f"Amount of positive numbers: ",count_pos)
number_of_even = a % 2 == 0
count_even = np.count_nonzero(number_of_even)
print(f"Amount of even numbers: ", count_even)

#4. If you were to add 3 to each data point, how many positive numbers would there be?
add_three = a + 3
new_positive_numbers = add_three > 0

count = np.count_nonzero(new_positive_numbers)
count

#5. If you squared each number, what would the new mean and standard deviation be?
sqred_numbers = a ** 2
print(np.mean(sqred_numbers))
print(np.std(sqred_numbers))

#6. A common statistical operation on a dataset is centering. This means to adjust the data such 
#that the mean of the data is 0. This is done by subtracting the mean from each data point. Center 
#the data set. See this link for more on centering.
data_centering = a - a.mean()
data_centering
#or
data_centering.mean()
#or
z = (a - a.mean()) / a.std()
z

#7. Calculate the z-score for each data point. Recall that the z-score is given by: Z = (x − μ) / σ
mean = np.mean(a)
std = np.std(a)
zscore = (a-mean)/std
zscore

#- Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
def evens_in_a(a) :
    new_a = []
    for i in a :
        if i % 2 == 0 :
            new_a.append(i)
    return new_a
print(evens_in_a(a))
#or
        ## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
        ## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

#- Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
    #sum_of_b = 0
    #for row in b:
        #sum_of_b += sum(row)
b = np.array(b)
b.sum()

#- Exercise 2 - refactor the following to use numpy. 
    #min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
b.min()

#- Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
    #max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
b.max()

#- Exercise 4 - refactor the following using numpy to find the mean of b
    #mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
b.mean()

#- Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
    #product_of_b = 1
    #for row in b:
        #for number in row:
            #product_of_b *= number
np.prod(b)
#np.prod multiplies everything in the array (put this in notes)

#- Exercise 6 - refactor the following to use numpy to find the list of squares 
    #squares_of_b = []
    #for row in b:
        #for number in row:
            #squares_of_b.append(number**2)
squares_of_b = [x**2 for x in b]
squares_of_b

#- Exercise 7 - refactor using numpy to determine the odds_in_b
    #odds_in_b = []
    #for row in b:
        #for number in row:
            #if(number % 2 != 0):
                #odds_in_b.append(number)
odds_in_b = (b[b%2!=0])
odds_in_b

#- Exercise 8 - refactor the following to use numpy to filter only the even numbers
    #evens_in_b = []
    #for row in b:
        #for number in row:
            #if(number % 2 == 0):
                #evens_in_b.append(number)
evens_in_b = (b[b%2==0])
evens_in_b

#- Exercise 9 - print out the shape of the array b.
b.shape

#- Exercise 10 - transpose the array b.
np.transpose(b)

#- Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(b, (1, 6))

#- Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(b, (6, 1))



            ### Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#- HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)
c

#- Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = c.min()
max_of_c = c.max()
sum_of_c = c.sum()
product_of_c = np.prod(c)

print(f"Minimum of c is ", min_of_c)
print(f"Maximum of c is ", max_of_c)
print(f"The sum of c is ", sum_of_c)
print(f"The product of c is ", product_of_c)

#- Exercise 2 - Determine the standard deviation of c.
stdev_of_c = c.std()
print(f"Standard deviation of c is ", stdev_of_c)

#- Exercise 3 - Determine the variance of c.
variance_of_c = np.var(c)
variance_of_c

#- Exercise 4 - Print out the shape of the array c
c.shape

#- Exercise 5 - Transpose c and print out transposed result.
transposed_c = np.transpose(c)
print(transposed_c)

#- Exercise 6 - Get the dot product of the array c with c. 
dot_product_of_c = np.dot(c, c)
dot_product_of_c

np.dot(c, c).sum()

#- Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
product_of_sum = np.prod(c)
transposed_product = np.transpose(product_of_sum)
sum_of_product = product_of_sum + transposed_product
sum_of_product

#- Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


            ## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

#- Exercise 1 - Find the sine of all the numbers in d
np.sin(d)

#- Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)

#- Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)

#- Exercise 4 - Find all the negative numbers in d
d = np.array(d)
d[d < 0]

#- Exercise 5 - Find all the positive numbers in d
d[d > 0]

#- Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)

#- Exercise 7 - Determine how many unique numbers there are in d.
d.shape

#- Exercise 8 - Print out the shape of d.
d.T.shape

#- Exercise 9 - Transpose and then print out the shape of d.
np.transpose(d)

#- Exercise 10 - Reshape d into an array of 9 x 2
