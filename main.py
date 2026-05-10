from planillas_google import acceder_planilla_google,update_planilla_google #acceder_planillas = ENCAPSULAMIENTO
from utils import restar_meses
import pandas as pd

df = acceder_planilla_google("Churn Prueba 2")
#print(df.head())

from utils import get_mes_id_now
mes_id_en_curso = get_mes_id_now() #invocamos la función
print(mes_id_en_curso)
mes_id_restado = restar_meses(mes_id_en_curso,4) #4 = arumento / parámetro.
df_historico = df[df["MES_ID"]<mes_id_restado]

print(df_historico)

df_actual = df[df["MES_ID"]>=mes_id_restado]
print(df_actual)

update_planilla_google(df_actual,"Churn Prueba 2")