import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
def acceder_planilla_google(nombre_planilla):

    '''

    Pregunta a ChatGPT: Quiero usar Google Sheets con la API de Google
    BOT: cuenta-drive-sheets-prueba@prueba-automatizacion-495320.iam.gserviceaccount.com

    '''

    # Alcances // SCOPES: Permisos a los que tenes acceso.
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # Credenciales
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )

    # Cliente
    client = gspread.authorize(creds)

    # Abrir spreadsheet
    spreadsheet = client.open(nombre_planilla)

    # Abrir hoja
    sheet = spreadsheet.sheet1

    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

def update_planilla_google(df,nombre_planilla):
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # Credenciales
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )

    # Cliente
    client = gspread.authorize(creds)

    # Abrir spreadsheet
    spreadsheet = client.open(nombre_planilla)

    # Abrir hoja
    sheet = spreadsheet.sheet1
    sheet.update(
    [df.columns.values.tolist()] +
    df.values.tolist()
    )

    print("planilla_actualizada")
