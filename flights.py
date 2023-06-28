import pandas as pd


data_directory = '/Users/jenu21/Desktop/tableau_migration'
csv_files = ['1987.csv', '1989.csv', '1990.csv', '1991.csv', '1992.csv', '1993.csv', '1994.csv', '1995.csv', '1996.csv']

dataframes = []
for file in csv_files:
    # year = file.split('/')[-1].split('.')[0]  # Extract the year from the file name
    df = pd.read_csv(file)
    # dataframes[year] = df
    dataframes.append(df)

for i, df in enumerate(dataframes, start=1987):
    year = str(i + 1987)
    # print(f"Data for {year}:")
    # print(df.head())
    # print()

for i, df in enumerate(dataframes):
    null_records_count = df.isnull().any(axis=1).sum()
    print("Number of records containing NULL values:", null_records_count)

    df = df.dropna(axis=1, how='all')
    df = df.fillna(0)
    dataframes[i] = df

    # print(f"Modified dataframe for {year}:")
    # print(df.head())
    # print()

columns_set = set(dataframes[0].columns)

for df in dataframes:
    if set(df.columns) != columns_set:
        df = df.reindex(columns=dataframes[0].columns)

    if df.dtypes.to_dict() != dataframes[0].dtypes.to_dict():
        df = df.astype(dataframes[0].dtypes.to_dict())

    dataframes[i] = df

master_df = pd.concat(dataframes, ignore_index=True)

# num_records_csv = len(master_df)
# print("Number of records in the combined_data.csv file:", num_records_csv)


# print("Column names in master_df :", master_df.columns)

print("Master dataframe:")
print(master_df.head())
master_df.to_csv('combined_data.csv', index = False)


