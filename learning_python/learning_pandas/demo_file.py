import pandas as pd


df = pd.read_csv('data/survey_results_public.csv')

# print(df)

# provides information about the number of rows and columns in a DataFrame
print(df.shape)

# gives us the number of rows, columns and the data types of columns
print(df.info())

# to print out all columns
pd.set_option('display.max_columns', 85)
# print(df)

schema_df = pd.read_csv('data/survey_results_schema.csv')

# to print out all rows
pd.set_option('display.max_rows', 85)
# print(schema_df)

# first few rows
print(df.head())

# last few rows
print(df.tail())
