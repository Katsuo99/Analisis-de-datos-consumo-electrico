import pandas as pd
import numpy as np
datos=pd.read_csv('household_power_consumption.txt', sep=';'
                  ,header=0,low_memory=False
                  ,infer_datetime_format=True
                  ,parse_dates={'datetime':[0,1]}
                  ,index_col=['datetime'])#Abrir El Archivo

print(datos.shape)
print(datos.head())

datos.replace('?', np.nan, inplace=True)
values=datos.values.astype('float32')

datos.to_csv('household_power_consumption.csv')
