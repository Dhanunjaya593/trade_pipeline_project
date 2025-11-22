import pandas as pd
import re

# Correct path to your Excel file
raw_path = "data/raw/Siddharth_Associates_sample data.xlsx"
df = pd.read_excel(raw_path)

# Function to parse GOODS DESCRIPTION
def parse_goods_description(text):
    if pd.isna(text):
        return None, None, None, None
    desc = str(text).lower()

    model = re.search(r'model\s*\w+', desc)
    capacity = re.search(r'\d+\s*(ml|kg|kva|pcs|nos)', desc)
    material = re.search(r'(glass|steel|plastic|wood|polyhouse)', desc)
    usd_price = re.search(r'usd\s*\d+(\.\d+)?', desc)

    return (
        model.group(0) if model else None,
        capacity.group(0) if capacity else None,
        material.group(0) if material else None,
        usd_price.group(0) if usd_price else None
    )

# Apply parsing to the correct column name
df[['Model', 'Capacity', 'Material', 'USD Price']] = df['GOODS DESCRIPTION'].apply(
    lambda x: pd.Series(parse_goods_description(x))
)

# Standardize UNIT column
df['UNIT'] = df['UNIT'].str.lower().replace({
    'nos': 'pcs',
    'pieces': 'pcs',
    'piece': 'pcs'
})

# Save cleaned data
cleaned_path = "data/cleaned/cleaned_data.csv"
df.to_csv(cleaned_path, index=False)