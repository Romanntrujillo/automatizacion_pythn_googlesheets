import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

def google_open_client():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    cred = Credentials.from_service_account_file("credentials.json", scopes=scope)

    cliente_bot = gspread.authorize(cred)
    return cliente_bot

def acceder_planilla_google(archivo_excel, numero_planilla = 0 ):
    client = google_open_client()
    spreadsheet = client.open(archivo_excel)

    sheet = spreadsheet.get_worksheet(numero_planilla)

    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

def cargar_mes_actual(archivo_excel, numero_planilla = 0):
    pass

def update_planilla_google(df,archivo_excel, numero_planilla=0):

    client = google_open_client()
    # Abrir spreadsheet
    sheet = client.open(archivo_excel).get_worksheet(numero_planilla)

    sheet.update(
    [df.columns.values.tolist()] +
    df.values.tolist()
    )
    print("planilla_actualizada")

def create_spreadsheet(archivo_excel, nombre_pestania, df):
    client = google_open_client()
    spreadsheet = client.open(archivo_excel)

    data = [df.columns.values.tolist()] + df.values.tolist()
    rows = len(data) + 10
    cols = len(df.columns) + 10

    new_worksheet = spreadsheet.add_worksheet(nombre_pestania, rows, cols)
    new_worksheet.update(data)