import gspread
from oauth2client.service_account import ServiceAccountCredentials

s = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',s)
client = gspread.authorize(creds)

sheet = client.open("Clinic Reminder Bot").sheet1
# finding the length of filled cells so that you know where to find next empty one to fill in
row_values = sheet.row_values(1)
col_values = sheet.col_values(1)
row_filled = len(col_values)
col_filled = len(row_values)

def save_reminder_date(date):
    sheet.update_cell(row_filled+1, 1, date)
    print("Saved date!")
    return 0

def reminder_body(msg):
    sheet.update_cell(row_filled+2, 2, msg)
    print("Saved reminder message")
    return 0
