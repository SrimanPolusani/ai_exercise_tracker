import gspread

from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("./keys.json", scopes=SCOPE)


# <----THIS OBJECT CAN READ AND WRITE IN GOOGLE SHEETS---->
class ReadWrite:
    def __init__(self):
        self.file = gspread.authorize(CREDS)

        self.workbook = self.file.open("workoutAI")
        self.sheet = self.workbook.sheet1

    def write(self, lst: list):
        for sub_list in lst:
            self.sheet.append_row(sub_list)
