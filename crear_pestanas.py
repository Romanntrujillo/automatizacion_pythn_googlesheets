import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

cred = Credentials.from_service_account_file("credentials.json", scopes=scope)

cliente_bot = gspread.authorize(cred)

spreadsheet = cliente_bot.open("Churn Prueba 2")

print(spreadsheet.worksheets())

'''
Hay dos formas de acceder a las pestañas del excel, por nombre y por posición
'''
hojas = len(spreadsheet.worksheets())
print (hojas)

hoja1 = spreadsheet.get_worksheet(0) #por posición
print((hoja1.get_all_records()))

hoja2 = spreadsheet.worksheet("productos") #por nombre
print (hoja2.get_all_records())

now = datetime.now().strftime("%m/%Y") #queremos la fecha actual con formato dia/mes/año
hoja_nueva = spreadsheet.add_worksheet(f"registro-{now}",100,10)