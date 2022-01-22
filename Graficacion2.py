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
for i in years:
    result=datos.loc[i,'Global_intensity']
    plt.figure(figsize=(10,6))
    plt.plot(result,color = 'tab:purple')
    plt.xlabel('Año')
    plt.ylabel('Global_intensity')
    plt.title("Global_intensity")
    plt.savefig("Global_intensity-"+i+".jpg", bbox_inches='tight')
    plt.show()
