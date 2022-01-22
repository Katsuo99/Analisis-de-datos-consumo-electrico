import pandas as pd
import numpy as np
datos=pd.read_csv('household_power_consumption.csv'
                  ,index_col=['datetime'])#Abrir El Archivo

for i in datos:
   datos[i].fillna( datos[i].mean(),inplace=True)
datos.to_csv('household_power_consumption_2.csv')
