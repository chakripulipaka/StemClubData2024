# -*- coding: utf-8 -*-
"""STEM CLUB 5/15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16lF_SxwYS5PWdram0ozgM3-_1f6m1NkD
"""

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/chakripulipaka/stemclubdata/main/STEM%20Club%20ML%20Data%20-%20Sheet1.csv')

df.head()

import pandas as pd

df = pd.read_csv("STEM Data.csv")

yes_no_cols = ["School sport", "Job", "Caffine"]

for col in yes_no_cols:
  df[col] = df[col].apply(lambda x: 1 if x == "Yes" else 0)

df.head()

from sklearn.linear_model import LinearRegression

# Separate the data into features and target
X = df.drop(['HoursSleep'], axis=1)
y = df['HoursSleep']

# Create a linear regression model
model = LinearRegression()

"""
# Train the model
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Evaluate the model
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y, predictions)
print("Mean squared error:", mse)
"""

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Train the model on the training set
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

print("Mean squared error:", mse)
print("R-squared:", r2)

X_test

def predict_sleep_hours(ap_classes, school_sport, clubs, job, caffine):
  """
  Predicts the number of hours of sleep based on the given input features.

  Args:
    ap_classes: Number of AP classes taken.
    school_sport: Whether the student participates in a school sport (1 for yes, 0 for no).
    clubs: Number of clubs the student is involved in.
    job: Whether the student has a job (1 for yes, 0 for no).
    caffine: Whether the student consumes caffeine (1 for yes, 0 for no).

  Returns:
    The predicted number of hours of sleep.
  """

  # Create a DataFrame with the input features
  data = {
    "AP Classes": [ap_classes],
    "School sport": [school_sport],
    "Clubs": [clubs],
    "Job": [job],
    "Caffine": [caffine]
  }
  df_new = pd.DataFrame(data)

  # Predict the number of hours of sleep
  predicted_sleep_hours = model.predict(df_new)[0]

  return predicted_sleep_hours

# Example usage

predicted_sleep_hours = predict_sleep_hours(0, 0, 0, 0, 0)
print("Predicted sleep hours:", predicted_sleep_hours)

