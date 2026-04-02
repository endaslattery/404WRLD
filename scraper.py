import pandas as pd

# Replace this with your published CSV URL
CSV_URL = "PASTE_YOUR_CSV_LINK_HERE"

# Read the sheet into a DataFrame
df = pd.read_csv(CSV_URL)

# Print all artists
for index, row in df.iterrows():
    print("Artist:", row["Artist Name"])
    print("Image URL:", row["Image URL"])
    print("RA URL:", row["RA"])
    print("---")
