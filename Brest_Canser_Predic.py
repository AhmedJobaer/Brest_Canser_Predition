# -*- coding: utf-8 -*-
"""ML_Assignment-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lyzxRsL1dftn9IIouqdA7Ub9S97uqQZ9
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
plt.style.use('ggplot')



"""# EDA"""

# Import and see the top 5 row in the dataset
df = pd.read_csv("Breast_cancer_data.csv")
df.head()

#how many number of columns and  row
df.shape

#All columns name
df.columns

#Check for missing value
df.isna().sum()

#Check the location if there is  any duplicated value
df.loc[df.duplicated()].count()

#check Data types
df.dtypes

df.describe()

# see the corelltion between columns 
df_corr = df[['mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area',
       'mean_smoothness', 'diagnosis']].corr()
sns.heatmap(df_corr, annot=True)



"""# Build and check performances for ML Models


---

1. Artificial Neural Network
2. Deep Neural Network
3. Naiive Bayes
4. Decision Trees.
"""



"""Import all dependency """

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Split the data into features and labels
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""**ANN**"""

# Define the neural network architecture
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluation of Neural Network
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy of Neural Network:', test_acc)

# Make predictions on the test set
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=-1)

# Compute precision, recall, F1-score
from sklearn.metrics import accuracy_score, f1_score
confusion_matrix_ann = confusion_matrix(y_test, y_pred)
print("Confusion Matrix for Neural Network (ANN):")
print(confusion_matrix_ann)
print("\n Accuracy: ", accuracy_score(y_test, y_pred))
print("F1-Score: ", f1_score(y_test, y_pred))
print("\n Precision: ", precision_score(y_test, y_pred))
print("Sensitivity (Recall): ", recall_score(y_test, y_pred))
print("\n")



"""DNN"""

# Define the DNN model architecture
dnn_model = Sequential()
dnn_model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],)))
dnn_model.add(Dense(64, activation='relu'))
dnn_model.add(Dense(32, activation='relu'))
dnn_model.add(Dense(1, activation='sigmoid'))

# Compile the model
dnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
dnn_model.fit(X_train, y_train, epochs=10, batch_size=32)

# Make predictions on the test set
y_pred_prob = dnn_model.predict(X_test)
y_pred = np.round(y_pred_prob).astype(int)

# Evaluate the DNN
confusion_matrix_dnn = confusion_matrix(y_test, y_pred)
print("Confusion Matrix for DNN:")
print(confusion_matrix_dnn)
print("\n Accuracy: ", accuracy_score(y_test, y_pred))
print("F1-Score: ", f1_score(y_test, y_pred))
print("\n Precision: ", precision_score(y_test, y_pred))
print("Sensitivity (Recall): ", recall_score(y_test, y_pred))



"""Naiive Bayes(NB)

"""

# Define the Naive Bayes classifier
gnb = GaussianNB()

# Train the classifier
gnb.fit(X_train, y_train)

# Make predictions on the test set
y_pred = gnb.predict(X_test)

# Evaluate the Naive Bayes classifier
confusion_matrix_nb = confusion_matrix(y_test, y_pred)
print("Confusion Matrix for Naive Bayes:")
print(confusion_matrix_nb)
print("\n Accuracy: ", accuracy_score(y_test, y_pred))
print("F1-Score: ", f1_score(y_test, y_pred))
print("\n Precision: ", precision_score(y_test, y_pred))
print("Sensitivity (Recall): ", recall_score(y_test, y_pred))



""" Decision Trees."""

# Define the Decision Tree classifier
dt = DecisionTreeClassifier()

# Train the classifier
dt.fit(X_train, y_train)

# Make predictions on the test set
y_pred = dt.predict(X_test)

# Evaluate the Decision Tree classifier
confusion_matrix_dt = confusion_matrix(y_test, y_pred)
print("Confusion Matrix for Decision Tree:")
print(confusion_matrix_dt)
print("\n Accuracy: ", accuracy_score(y_test, y_pred))
print("F1-Score: ", f1_score(y_test, y_pred))
print("\n Precision: ", precision_score(y_test, y_pred))
print("Sensitivity (Recall): ", recall_score(y_test, y_pred))