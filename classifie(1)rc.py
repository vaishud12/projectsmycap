#importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
%matplotlib inline

# using pandas to read the database stored in the same folder
data = pd.read_csv('mnist.csv')

# viewing coloumn heads
data.head()

# extracting data from the data from the dataset and viewing them up close
a = data.iloc[3,1:].values

# reshaping the extracted data into a reasonable size
a = a.reshape(28,28).astype('uint8')
plt.inshow(a)

# preparing the data
# separating labels and data values
df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]

# creating test amd train sizes/batches
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2, random_state=4)

# check data
y_train.head()

# call rf classifier
rf = RandomForestClassifier(n_estimators=100)

# fit the model
rf.fit(x_train, y_train)



