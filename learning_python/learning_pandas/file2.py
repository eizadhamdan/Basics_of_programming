import pandas as pd


df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

pd.set_option('display.max_columns', 84)
pd.set_option('display.max_rows', 85)

# print(df)
# print(schema_df)

# print(df.shape)
print(df.columns)

# print(df["LearnCode"])
print(df["YearsCode"].value_counts())
print(df.loc[[0, 1, 2, 3, 4, 5], "YearsCode"])

print(df.loc[0:10, "YearsCode"])
print(df.loc[0:5, "Age":"YearsCode"])
