import pandas as pd


people = {
    "first": ["Charlie", "Jane", "John"],
    "last": ["Becker", "Doe", "Doe"],
    "email": ["CharlieBecker@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
}

print(people["email"])

df = pd.DataFrame(people)

print(df)

# both are the same
print(df["email"])
print(df.email)

print(type(df["email"]))                # a series

print(df[["last", "email"]])
print(type(df[["last", "email"]]))          # a dataframe

# to get names of the columns
print(df.columns)

# to get the rows
print(df.iloc[0])           # to get the row using index
print(df.iloc[[0, 1]])
print(df.iloc[[0, 1], 2])       # to get the third column of the first two rows

print(df.loc[0])
print(df.loc[[0, 1]])
print(df.loc[[0, 1], "email"])
print(df.loc[[0, 1], ["email", "last"]])
