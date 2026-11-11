import random
import warnings

import pandas as pd
from numpy.ma.core import size
from openpyxl.styles.builtins import warning

warnings.filterwarnings("ignore")
# using list
product_data=[['e-book', 2000], ['plants', 6000], ['Pencil', 3000]]
# 2d list, similar to 2d array
indexes=[1,2,3]
columns_name=['product', 'unit_sold']
product_df = pd.DataFrame(data=product_data, index=indexes,
columns=columns_name)
print(product_df)


# using dictionaries
product_data={'product': ['e-book', 'plants', 'Pencil'], 'unit_sold':
[2000, 5000, 3000]}
product_df = pd.DataFrame(data=product_data)
print(product_df)

# using numpy array
import numpy as np
products = np.array([['','product','unit_sold'], [1, 'E-book',2000],
[2, 'Plants', 6000], [3, 'Pencil', 3000]])
product_pf = pd.DataFrame(data=products[1:,1:],index=products[1:,0 ],
columns=products[0,1:])
print(product_pf) # output is same as of first case


df = pd.read_csv('dirtydata (2).csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated())

#Removing Rows
new_df = df.dropna()
print(new_df.to_string())

#Replace Empty Values
df = pd.read_csv('dirtydata (2).csv')
df.fillna(130)
print(df.to_string())

#Replace Only For Specified Columns
df = pd.read_csv('dirtydata (2).csv')
print(df["Calories"].fillna(130))

#Replace Using Mean, Median, or Mode
df =  pd.read_csv('dirtydata (2).csv')
x = df["Calories"].mean()
df["Calories"].fillna(x)

df =  pd.read_csv('dirtydata (2).csv')
x = df["Calories"].median()
df["Calories"].fillna(x)

df =  pd.read_csv('dirtydata (2).csv')
x = df["Calories"].mode() [0]
df["Calories"].fillna(x)

#Convert Into a Correct Format
df = pd.read_csv('dirtydata (2).csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())

#Removing Rows
df.dropna(subset=['Date'], inplace=True)
print(df.to_string())

#Replacing Values
df.loc[7, 'Duration'] = 45
for x in indexes:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

#Removing Rows
for x in indexes:
    if df.loc[x, "Duration"] < 120:
        df.drop(index=x, inplace=True)
print(df.duplicated())
df.drop_duplicates(inplace=True)



#Practical 7.2
import matplotlib.pyplot as plt
# Draw a line in a diagram from position (0,0) to position (6,250)
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()

# Default X-Points
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()

# using 'marker'
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()

#Add a plot title and labels for the x- and y-axis
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

#subplot() Function
#Draw 2 plots on top of each other:
import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(x,y)

#Draw 6 plots:
import matplotlib.pyplot as plt
import numpy as np
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()

#COLOR
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.show()

# create an array with values (from 0 to 100), one value for
#each point in the scatter plot:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.show()

#set the color for the bar
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "red")
plt.show()


# Say you ask for the height of 250 people
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()
#using pie function to draw pie charts
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()


import ssl
import certifi
import seaborn as sns

ssl._create_default_https_context = (
    lambda: ssl.create_default_context(cafile=certifi.where())
)
ssl._create_default_https_context = ssl._create_unverified_context
data = sns.load_dataset("iris")
print(data.head())