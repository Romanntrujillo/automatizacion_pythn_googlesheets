from planillas_google import acceder_planilla_google, create_spreadsheet  # acceder_planillas = ENCAPSULAMIENTO
from utils import restar_meses

df = acceder_planilla_google("Churn Prueba 2")
#print(df.head())

from utils import get_mes_id_now
mes_id_en_curso = get_mes_id_now() #invocamos la función

mes_id_restado = restar_meses(mes_id_en_curso,4) #4 = arumento / parámetro.

df_historico = df[df["MES_ID"]<mes_id_restado]
df_actual = df[df["MES_ID"]>=mes_id_restado]

nombre_pestania_historico = str(restar_meses(mes_id_restado, 1))

create_spreadsheet("Historico Prueba", nombre_pestania_historico, df_historico)

