import gspread
from google.oauth2.service_account import Credentials

# Connect to Google Sheets
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

creds = Credentials.from_service_account_file("creds.json", scopes=scope)
client = gspread.authorize(creds)

# Open your sheet
sheet = client.open("Techno Artist Dashboard").sheet1

# Get all rows
rows = sheet.get_all_records()

# Print artist names
for row in rows:
    print("Artist:", row["Artist Name"])
