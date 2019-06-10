from matplotlib import pyplot as plt 
import pandas as pd 
import matplotlib.pyplot as plt

lectura = pd.read_csv('nombres-2015.csv', delimiter = ',', names = ['nombre', 'cantidad', 'anio'])
lectura.head()



#query = str(input('What name are you searching?'))

#query1 = lectura[lectura.nombre == str(query)]
#print query1

#name1 = query1['nombre']    
#print name1

#quantity1 = query1['cantidad']
#print quantity1

n = input('How many names are you searching?')
#if type(n) <> int:
 #       print 'That is not a number'
  #      n = int(input('How many names are you searching?'))

for i in range(n):
    query = str(input('What name are you searching?'))
    print lectura[lectura.nombre == str(query)]
    query1 = lectura[lectura.nombre == str(query)]
    name = query1['nombre']
    quantity = query1['cantidad']
    plt.bar(name, quantity , label = query)

    
    #if query <> lectura[lectura.nombre == str(query)]:
     #   print 'Name is not in data base'
    #else:
     #       print query 

    

plt.xlabel ('Nombres')
plt.ylabel('Cantidad')
plt.title('Nombres 2015' )
plt.legend()
plt.show()