import pandas as pd
import matplotlib.pyplot as plt
datos=pd.read_csv('household_power_consumption_Normalizada01.csv')
                  # ,infer_datetime_format=True
                  # ,index_col=['datetime'])
columnas=['Global_active_power', 'Global_reactive_power',
       'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2',
       'Sub_metering_3']
for i in columnas:
    fig, ax1 = plt.subplots() # prepara un gráfico de matplotlib
    
    datos[i].plot()
    
    # realiza ajustes al gráfico con matplotlib:
    ax1.tick_params(labelsize=10, pad=1)
    fig.suptitle(i, fontsize=15)

