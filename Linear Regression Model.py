import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# MULTIPLE LINEAR REGRESSION MODEL (loading dataset)
dataset=pd.read_csv(r'C:\Users\user\Desktop\Test Datasets\REGRESSION ML\Petrol _Consumption.csv')
dataset.head()
dataset.describe()  # to see statistical details such as mean standard deviation or max-min of dataset 

# Divide datset into attributes and labels 

X = dataset[['Petrol_tax', 'Average_income', 'Paved_Highways',
       'Population_Driver_licence(%)']]
y = dataset['Petrol_Consumption']

# Separate  dataset into train and test data 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model or the machine using fit() and importing Linear Regression from sklearn
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Create coefficients for the 4  attributes or independent variables  
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
coeff_df
print(coeff_df)

# create intercept of the model 
model = LinearRegression().fit(X, y)
model.score(X, y)
model.coef_
model.intercept_
print("intercept is",model.intercept_)

# Result of Intercept and Coefficients from randomly selected variables

                #Petrol_tax                     -40.016660
                #Average_income                  -0.065413
                #Paved_Highways                  -0.004741
                #Population_Driver_licence(%)  1341.86212
                # intercept is 377.29114647367317
 
 # The model: petrol consumption, y= 377.30-40.016660(x1)-0.065413(x2)-0.004741(x3)+1341.86212(x4)   

         
# Interpretation: Example, people tend to reduce their petrol consumption (by 40 gallons) for every unit increase in petrol_tax
#But gas consumption increases by 1341.86212 gallons for every 1% increase in Population_Driver_License.   


# to make output or label predictions using the parameters derived from the training data
y_pred = regressor.predict(X_test)
# to see difference between the actual output and predicted output  
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
