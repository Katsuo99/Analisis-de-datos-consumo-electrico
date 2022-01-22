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

# for j in columnas:
#     for i in years:
#         result=datos.loc[i,j]
#         plt.figure(figsize=(10,6))
#         plt.plot(result,color = 'tab:purple')
#         plt.xlabel('Año')
#         plt.ylabel(j)
#         plt.title(j+'-'+i)
#         plt.savefig(j+"-"+i+".jpg", bbox_inches='tight')
#         plt.show()

result=datos.loc['2007','Global_intensity']
result2=datos.loc['2008','Global_intensity']
result3=datos.loc['2009','Global_intensity']
result4=datos.loc['2010','Global_intensity']
fig, ax = plt.subplots(2, 2, sharey = True)
ax[0, 0].plot(result,color = 'tab:purple')
ax[0, 1].plot(result2,color = 'tab:purple')
ax[1, 0].plot(result3,color = 'tab:purple')
ax[1, 1].plot(result4,color = 'tab:purple')
plt.savefig("Global_intensity.jpg", bbox_inches='tight')
plt.show()     