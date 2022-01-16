import pandas as pd
import matplotlib.pyplot as plt
datos=pd.read_csv('household_power_consumption.csv'
                  ,infer_datetime_format=True
                  ,index_col=['datetime'])

# for i in datos:
#     fig, ax1 = plt.subplots() # prepara un gráfico de matplotlib
    
#     datos[i].plot()
    
#     # realiza ajustes al gráfico con matplotlib:
#     ax1.tick_params(labelsize=10, pad=1)
#     fig.suptitle(i, fontsize=15)

