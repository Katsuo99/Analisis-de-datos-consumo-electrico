import pandas as pd
import matplotlib.pyplot as plt
datos=pd.read_csv('household_power_consumption_Normalizada01.csv'
                   ,infer_datetime_format=True
                   ,index_col=['datetime']
                   ,parse_dates=True)
columnas=['Global_active_power', 'Global_reactive_power',
        'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2',
        'Sub_metering_3']
years=['2007','2008','2009','2010']  
meses=datos['Global_intensity'].resample('M').mean()
for i in years:
    plt.plot(meses[i].values,label='Año '+i,marker='o')
    plt.xlabel('Mes')
    plt.ylabel('Global_intensity')
    plt.title("Intensidad Global Año: "+i)
    plt.legend()
    plt.savefig("Global_intensity-"+i+"_2.jpg", bbox_inches='tight')
    plt.show()
    
    
# plt.plot(meses['2007'].values,label='Año 2007',marker='o')
# plt.plot(meses['2008'].values,label='Año 2008',marker='o')
# plt.plot(meses['2009'].values,label='Año 2009',marker='o')
# plt.plot(meses['2010'].values,label='Año 20010',marker='o')
# plt.xlabel('Mes')
# plt.ylabel('Global_intensity')
# plt.title("Intensidad Global 2007-2010 ")
# plt.legend()
# plt.savefig("Global_intensity.jpg", bbox_inches='tight')
# plt.show()

