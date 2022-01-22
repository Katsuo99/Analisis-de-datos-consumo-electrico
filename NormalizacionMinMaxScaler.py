import pandas as pd
from sklearn import preprocessing
import seaborn as sns 
import matplotlib.pyplot as plt
columnas=['Global_active_power', 'Global_reactive_power',
       'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2',
       'Sub_metering_3']

datos=pd.read_csv('household_power_consumption_2.csv',header=0)
df=pd.DataFrame(datos)
fig,(ax1,ax2)=plt.subplots(ncols=2,figsize=(6,5))
ax1.set_title('Antes De Normalizar')
sns.kdeplot(df['Global_intensity'],ax=ax1)
print(df['Global_intensity'].describe())

scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
df[columnas]=scaler.fit_transform(df[columnas])
print("*"*10)
print(df['Global_intensity'].describe())
ax2.set_title('Despues De Normalizar')
sns.kdeplot(df['Global_intensity'],ax=ax2)

datos.to_csv('household_power_consumption_Normalizada01.csv')