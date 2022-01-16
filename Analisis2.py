import pandas as pd
import matplotlib.pyplot as plt
datos=pd.read_csv('household_power_consumption.csv'
                  ,infer_datetime_format=True
                  ,index_col=['datetime'])

print(datos.columns[0])
for i in range(len(datos.columns)):
    print(i)