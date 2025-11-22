import pandas as pd

# Step 1: Read the cleaned file from Task 1
df = pd.read_csv("data/cleaned/cleaned_data.csv")

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Fill empty values with "NA"
df = df.fillna("NA")

# Step 4: Make text in GOODS DESCRIPTION small letters
df["GOODS DESCRIPTION"] = df["GOODS DESCRIPTION"].str.lower()

# Step 5: Save new file
df.to_csv("data/cleaned/transformed_data.csv", index=False)

print("Task 2 done. File saved as transformed_data.csv")