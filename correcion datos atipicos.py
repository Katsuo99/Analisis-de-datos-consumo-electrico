import pandas as pd
import matplotlib.pyplot as plt
datos=pd.read_csv('p1.csv'
                  ,infer_datetime_format=True
                  )
p2=['0','2.148','.235','244.078','9.071','7.274','7.12','14.895']
p3=['0','.034','.010','237.599','.183','-1','-1','-1']
columnas=['Global_reactive_power',
       'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2',
       'Sub_metering_3']
# for i in datos.columns:
#     print(i+datos[i].describe())
# print((len(datos)))
# print(datos.loc[23,'Voltage'])
df=pd.DataFrame(datos)
# for i in range(len(df.columns)):
#     if i == 0:
#         i = 0
#         print('datetime ah sido omitido')
#     else:
#         for j in range(len(df)):
#             print(str(j) + datos.columns[i]+'='+str(df.loc[j,df.columns[i]]))
#             if j == 500000 or j == 1000000 or j == 1500000 or j == 2000000 :
#                 print(j)
#             if float(df.loc[j,df.columns[i]])>float(p2[j]):
#                 df.loc[j,df.columns[i]]=float(p2[j])
#             if float(df.loc[j,df.columns[i]])<float(p3[j]):
#                 df.loc[j,df.columns[i]]=float(p3[j])
#     print(datos.columns[i])
na=2
for i in columnas:
    print(i)
    for j in range(len(df)):
        if j == 500000 or j == 1000000 or j == 1500000 or j == 2000000 :
            print(j)
        if float(df.loc[j,i])>float(p2[na]):
            df.loc[j,i]=float(p2[na])
        if float(df.loc[j,i])<float(p3[na]):
            df.loc[j,i]=float(p3[na])
    na+=1
df.to_csv('final.csv')

# for i in range(len(datos.columns)):
#     print(i)
#     print(datos.columns[i])

# for i in range(1000):
#     if i == 500 or i == 700 or i == 900:
#         print(i)