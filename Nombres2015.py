from matplotlib import pyplot as plt 
import pandas as pd 

lectura = pd.read_csv('nombres-2015.csv', delimiter = ',', names = ['nombre', 'cantidad', 'anio'])
lectura.head()



query = str(input('What name are you searching?'))

query1 = lectura[lectura.nombre == str(query)]
print query1

name1 = query1['nombre']    
print name1

quantity1 = query1['cantidad']
print quantity1


query = str(input('What name are you searching?'))

query2 = lectura[lectura.nombre == str(query)]
print query2

name2 = query2['nombre']    
print name2

quantity2 = query2['cantidad']
print quantity2

n = int(input('How many names are you searching?'))




import matplotlib.pyplot as plt

plt.bar(name1, quantity1 , label = name1)
plt.bar(name2, quantity2 , label = name2)

plt.xlabel ('Nombres')
plt.ylabel('Cantidad')
plt.title('Nombres 2015' )
plt.legend()
plt.show()