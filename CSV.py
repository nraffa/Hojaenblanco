#PROVINCIA,TRANSITORIAS,TEMPORARIAS,PERMANENTES,TOTAL
import pandas as pd
import numpy as np

lectura = pd.read_csv('residencias-otorgadas---1-trimestre---ano-2019.csv', delimiter = ',', names = ['PROVINCIA','ABREVIACION','TRANSITORIAS','TEMPORARIAS','PERMANENTES','TOTAL'])
#.head indica cuantas filas se imprimen (arrancando en 0 por supuesto)
lectura1 = lectura.head(3)

# Get the series
#print lectura['PROVINCIA']
prov = lectura['ABREVIACION']
tran = lectura['TRANSITORIAS']
temp = lectura['TEMPORARIAS']
perm = lectura['PERMANENTES']
tot = lectura['TOTAL']

print prov[2] #Cordoba
#Filtering
# print lectura[lectura.source == 'SAN JUAN'] no sale y no se porque


import matplotlib.pyplot as plt

#provin = [prov]
#trans = [tran]
x = prov
y = tran
plt.bar(x, y, label = 'Transitorias')
plt.bar(x, temp, label = 'Temporarias')
plt.bar(x, perm, label = 'Permanentes')
#plt.bar(x, tot, label = 'Total')

plt.xlabel ('Provincias')
plt.ylabel('Residencias Transitorias')
plt.title('Residencias')
plt.legend()
plt.show()
