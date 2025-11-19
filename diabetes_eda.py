import codecademylib3
import pandas as pd
import numpy as np

# code goes here

#Data types for each column
#Pregnancies - int
#Glucose-int
#BloodPressure-int
#SkinThickness-int
#Insulin-int
#BMI-float
#Age-int
#Outcome-int (0 or 1)
#DiabetesPedigreeFunction-float

diabetes_data=pd.read_csv("diabetes.csv")
print(diabetes_data.head()) 
print("\n")

print("Number of columns: ") #finding out how many columns does the data contain
print(diabetes_data.shape[1])
print("\n")

#finding out how many rows does the data contain
print("Number of rows: ")
print(diabetes_data.shape[0])
print("\n")

# checking for missing values in each column of the data frame
print("Number of null values in each column: ")
print(diabetes_data.isnull().sum())
print("\n")

print("Patterns in missing data: ")
print("Some measurement columns may have 0 values that actually represent missing values.")

#display summary statistics for each numeric column (min, max, etc...) 
print(diabetes_data.describe())


#replacing all "0" values as missing with np.nan since 0 is not realistic
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

#re-checking the output for missing values
print("Number of null values in each column after replacing 0 with NaN: ")
print(diabetes_data.isnull().sum())
print("\n")

#.any(axis=1) checks each row, if any value in a row is missing, the result for that row is True 
print("Rows that contains at least one missing value: ")
print(diabetes_data[diabetes_data.isnull().any(axis=1)])
print("\n")

# .info() shows each column's name, data type and how many non-null values each column contains
print("Data types of each column: ")
print(diabetes_data.info())
print("\n")

print("Unique values in the Outcome column: ")
print(diabetes_data.Outcome.unique())
print("\n")


#convert any instance that its not int to int, to fix the issue with the data type
if diabetes_data.Outcome.dtype == "object":
    print("Unique Outcome values before conversion:", diabetes_data.Outcome.unique())
    diabetes_data['Outcome'] = pd.to_numeric(diabetes_data['Outcome'], errors='coerce')
    print("Unique Outcome values after conversion:", diabetes_data.Outcome.unique())

#show the count of each unique value, including NaNs
print(diabetes_data.Outcome.value_counts(dropna=False))

#checking min and max values in each column
print(diabetes_data.min())
print(diabetes_data.max())

#fill missing values in each column with the median of that column
missing_columns = diabetes_data.columns[diabetes_data.isnull().any()]
diabetes_data[missing_columns] = diabetes_data[missing_columns].fillna(
    diabetes_data[missing_columns].median())



















