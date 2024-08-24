# Slicing (Slicing involves the selection of the rows from the dataframe by using colon sign)
# slicing with list:
# The slicing with list involves the selection of elements from the row or one dimensional array
list=[2,4,6,8,9,10,12,14,15]
print(list[2:6])

import numpy as np

# Create a sample 2D NumPy array
arr = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15]])

# Slicing to select rows 1 and 2
rows_slice = arr[1:3, :]
print(rows_slice)

# Slicing to select columns 1 and 2
cols_slice = arr[:, 1:3]
print(cols_slice)

# # Slicing to select a subarray (rows 1 to 2 and columns 1 to 2)
# subarray_slice = arr[1:3, 1:3]
# print(subarray_slice)
# When slicing a 2D NumPy array, the syntax array[row_start:row_end, col_start:col_end] is used:
#row_start:row_end specifies the range of rows you want to select.
#col_start:col_end specifies the range of columns you want to select.
#If you use a colon alone (:) for either the row or column part, it means "select all" in that dimension.

import numpy as np
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# Access a subarray (rows 0 to 1 and columns 1 to 2)
subset = arr[0:2, 1:3]
print(subset)  # Output: [[1, 2], [4, 5]]
# is mn sab sai phlai woh wali rows lain gai hum jo hamai chahy r phir un mn sai us rows mn sai un column ko lai lain gai jo colon kai bad mn define kiay gai hn
# yani kai un rows r un columns ka utna portion(subset) lai lain gai

import numpy as np

# Create a 3D NumPy array
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
])

# Print the array
print("Original 3D Array:")
print(arr_3d)
print()

# Example of slicing to select a subarray
subset_3d = arr_3d[1:, 0:1, 1:3]
print("Subset (slicing to select elements):")
print(subset_3d)

import numpy as np

# Create a 3D NumPy array
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
])

# Print the array
# print("Original 3D Array:")
# print(arr_3d)
# print()

# Example of slicing to select a subarray
subset_3d = arr_3d[1:, 0:1, 1:3]
print("Subset (slicing to select elements):")
print(subset_3d)

import numpy as np

# Create a 3D NumPy array
arr_3d = np.array([
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
    [[30, 31, 32], [33, 34, 35], [36, 37, 38]],
    [[40, 41, 42], [43, 44, 45], [46, 47, 48]]
])

# Slice a part of the array
subset_3d = arr_3d[1:3, 1:3, 1:3]
print("Subset (slicing depths 1 to 2, rows 1 to 2, columns 1 to 2):")
print(subset_3d)

# loc, iloc, slicing, and indexing are all ways to access data in pandas DataFrames or Series, but they have different behaviors and purposes:
# Indexing: Refers to accessing a single element or a subset of elements from a DataFrame or Series using its index or column names. For example, df['column_name'] accesses the column named 'column_name'.
# Slicing: Refers to selecting a range of rows or columns using their positions. For example, df.iloc[1:5] selects rows 1 through 4 (index positions 1, 2, 3, and 4).
# loc: Uses labels (index or column names) to access data. It is primarily label-location based. For example, df.loc['row_label', 'column_label'] accesses the element at the specified row and column labels.
# iloc: Uses integer positions to access data. It is primarily integer-location based. For example, df.iloc[row_index, column_index] accesses the element at the specified row and column indices.
# Key Differences:
# loc and iloc both provide ways to access data, but loc uses labels (names), while iloc uses integer indices.
#loc includes the end label in slices (start:end), while iloc does not (start:end-1).
#iloc is similar to traditional Python indexing (0-based), where slicing does not include the endpoint.
#Indexing and slicing are more general terms that apply to accessing elements in Python data structures, while loc and iloc are specific to pandas DataFrames and Series.
#In summary, while loc and iloc can be used for indexing and slicing, they offer different ways to access data: loc uses labels, and iloc uses integer positions. These methods are essential for efficiently manipulating and accessing data within pandas structures.


# loc and iloc
import pandas as pd

# Example DataFrame
data = {
    'A': [10, 20, 30, 40],
    'B': [50, 60, 70, 80],
    'C': [90, 100, 110, 120]
}
df = pd.DataFrame(data, index=['X', 'Y', 'Z', 'W'])

# Using loc
# Accessing a single element
print(df.loc['Y', 'B'])  

# # Accessing a row slice with specific columns
print(df.loc['Y':'Z', 'B':'C'])


# # # Accessing specific rows and columns
print(df.loc[['X', 'W'], ['A', 'C']])

# # # Using iloc
# # # Accessing a single element
print(df.iloc[1, 2]) 

# # # Accessing a row slice with specific columns
print(df.iloc[1:3, 1:3])


# Understanding iloc
# iloc with Slicing: When using slicing with iloc, the endpoint is not included. For example, df.iloc[0:2] will include rows at positions 0 and 1, but not 2.
# iloc with Lists: When using a list of indices, iloc selects exactly those indices.

# # # Accessing specific rows and columns by position
print(df.iloc[[0, 3], [0, 2]])






