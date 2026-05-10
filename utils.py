import datetime
from dateutil.relativedelta import relativedelta

def get_mes_id_now():
    now = datetime.datetime.now()
    '''
    month = now.month
    year = now.year

    mes_id = (year*100)+month
    return mes_id
    '''
    mes_id = convertir_date_a_mes_id(now)
    return mes_id

def convertir_mes_id_a_date (mes_id):
    mes_id_string = str(mes_id)
    year_string = mes_id_string[0:4]
    month_string = mes_id_string[4:6]
    fecha = f"{year_string}-{month_string}-01"
    fecha_datetime = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    return fecha_datetime

def convertir_date_a_mes_id(date):
    month = date.month
    year = date.year
    mes_id = (year * 100) + month
    return mes_id

def restar_meses (mes_id,meses):
    fecha = convertir_mes_id_a_date(mes_id)
    fecha_restada = fecha+relativedelta(months=-meses)
    mes_id_restado = convertir_date_a_mes_id(fecha_restada)
    return mes_id_restado




