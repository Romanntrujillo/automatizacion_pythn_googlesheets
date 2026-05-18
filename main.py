from planillas_google import *  # acceder_planillas = ENCAPSULAMIENTO
from utils import restar_meses

'''
- descargar planillas
- cargar informacion de las planillas, discriminada
- generar backup mes anterior de la plantilla maestra
- cargar datos mes entrante vacio en base a informacion de las plantillas
- actualizar plantilla maestra
'''





df = acceder_planilla_google("Churn Prueba 2")
#print(df.head())

from utils import get_mes_id_now
mes_id_en_curso = get_mes_id_now() #invocamos la función

mes_id_restado = restar_meses(mes_id_en_curso,4) #4 = arumento / parámetro.

df_historico = df[df["MES_ID"]<mes_id_restado]
df_actual = df[df["MES_ID"]>=mes_id_restado]

# creacion del historico
nombre_pestania_historico = str(restar_meses(mes_id_restado, 1))
create_spreadsheet("Historico Prueba", nombre_pestania_historico, df_historico)
create_spreadsheet("Churn Prueba 2","respaldo", df)

update_planilla_google(df_actual,"Churn Prueba 2")

cargar_mes_actual("Churn Prueba 2")

lista_shv = []