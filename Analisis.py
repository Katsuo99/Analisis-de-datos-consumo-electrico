import pandas as pd
import matplotlib.pyplot as plt
datos=pd.read_csv('household_power_consumption6.txt', sep=',')
#print(datos)
#print(datos.columns)
columnas=['Global_active_power', 'Global_reactive_power',
       'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2',
       'Sub_metering_3']
#print(datos['Voltage'].describe())
#print(datos['Voltage'].mean())


l=0

#datos.to_csv('new-data.csv', na_rep='0')
#datos.replace('?',0,inplace=True)
#datos['Voltage'].replace('?',0, inplace=True)

#print(pd.to_numeric(datos['Voltage']).describe())
#print(datos['Voltage'])

#datos.plot();
# print(datos['Voltage'])
#for i in datos['Voltage']:
#     print(float(i))

# x_values = datos['Date'].unique()
# y_values = datos['Time'].unique()
# plt.bar(x_values, y_values)
# plt.show()
# plt.close('all')
# print(datos['Global_active_power'])
for i in columnas:
    fig, ax1 = plt.subplots() # prepara un gráfico de matplotlib
    
    datos[i].plot()
    
    # realiza ajustes al gráfico con matplotlib:
    ax1.tick_params(labelsize=10, pad=1)
    fig.suptitle(i, fontsize=15)


# for i in columnas:
#     my_plot = datos[i].plot()
#     plt.show() # no necesariamente en Jupyter Notebooks

