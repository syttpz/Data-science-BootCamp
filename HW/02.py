'''
HW Questions (Numpy):

    1. Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.
    2. Find common elements between A and B. [Hint: Intersection of two sets]
    3. Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]
    4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

HW Questions (Pandas):

    1. From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).

    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

    2. Replace missing values in Min.Price and Max.Price columns with their respective mean.

    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

    3. How to get the rows of a dataframe with row sum > 100?

    df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

'''
import numpy as np
import pandas as pd


# 1
A = np.array([[3, 7, 2], [8, 5, 13]])
B = np.array([[6, 1, 8], [4, 9, 12]])
Vert = np.concatenate((A,B), axis=0)
Horz = np.concatenate((A,B), axis=1)

# 2
common = np.intersect1d(A, B)

# 3
Range = A[(A > 5) & (A < 10)]

# 4
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
Filtered = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]


# Pandas Questions
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# 1
cols = ['Manufacturer','Model','Type']
filtered_df = df.loc[::20, cols]
# 2
df['Min.Price'] = df['Min.Price'].fillna(df['Min.Price'].mean())
df['Max.Price'] = df['Max.Price'].fillna(df['Max.Price'].mean())

# 3
df_sum = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
Rows_sum = df_sum[df_sum.sum(axis=1) > 100]



if __name__ == "__main__":
    print("Numpy")
    print("1.\n", Vert)
    print("  \n", Horz)
    print("2.\n", common)
    print("3.\n", Range)
    print("4.\n", Filtered)

    print("\nPandas")
    print("1.\n", filtered_df)
    print("2.\n", df[['Min.Price', 'Max.Price']])
    print("3.\n", Rows_sum)