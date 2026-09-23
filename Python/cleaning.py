import pandas as pd

# 1. Load
df = pd.read_csv('recruitment_data.csv')
print(f"Original rows: {len(df)}")

# 2. Check nulls
print(df.isnull().sum())

# 3. Remove duplicates
df.drop_duplicates(inplace=True)

# 4. Fix dates
df['Application_Date'] = pd.to_datetime(df['Application_Date'])
df['Offer_Date'] = pd.to_datetime(df['Offer_Date'])

# 5. Create new column
df['Time_to_Hire'] = (df['Offer_Date'] - df['Application_Date']).dt.days

# 6. Clean text - remove extra spaces
df['Source'] = df['Source'].str.strip()
df['Status'] = df['Status'].str.strip()

# 7. Remove negative time (wrong data)
df = df[df['Time_to_Hire'] > 0]

# 8. Save cleaned
df.to_csv('cleaned_recruitment.csv', index=False)
print(f"Cleaned rows: {len(df)}")
print("Saved as cleaned_recruitment.csv")