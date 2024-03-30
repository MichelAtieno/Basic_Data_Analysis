import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1pcWBVxWvcHs-n1iyOgO4BAX2wWxptTv8XXKpIbpK38A"
sheet = client.open_by_key(sheet_id)
# print(sheet.worksheet("Basic Data Analysis").row_values(2))
# values_list = sheet.sheet2.row_values(2)
# values_list = sheet.worksheet("Basic Data Analysis").row_values(2)
values_list = sheet.worksheet("Basic Formatting").row_values(2)
print(values_list)

