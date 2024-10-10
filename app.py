# import the libraires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# load the dataset
df = pd.read_csv('winequality-red.csv')

df.head()

# find the size of dataset (rows, columns)
print(df.shape)

# find the infomation of dataset (no. of null values, datatype, dataset size)
df.info()

# describe the dataset (for statistical values, mean, mode, std, min, max, ...)
df.describe()

# check the correlation between features
plt.figure(figsize=(10, 8))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')

# find the value for 'quality' and plot 
df['quality'].value_counts()

# draw the plot for 'quality' 
plt.figure(figsize=(5,5))
sns.catplot(x='quality', data=df, kind='count')

# select the feature
X = df.drop('quality', axis=1)
y = df['quality'].apply(lambda value : 1 if value >= 7 else 0) # we select from this dataset 'quality' >= 7 only good quality otherwise not good

y.value_counts()

# split the data as train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# create the fit model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# find the predict value and error
y_pred = model.predict(X_test)

acc_score = accuracy_score(y_pred, y_test)
print("Accuracy Score : ", acc_score)

# for web 

# libraries
import streamlit as st
from PIL import Image

# web app code
st.title('Wine Quality Prediction Model')
img = Image.open('wine_quality.jpg')
st.image(img, width=120, use_column_width=True)

input_values = st.text_input('Enter all Wine Features')
input_values_list = input_values.split(',')
featuers = np.asarray(input_values_list)
prediction = model.predict(featuers.reshape(1, -1))

if prediction[0] == 1 :
    st.write('Good Quality Wine')
else :
    st.write('Bad Quality Wine')