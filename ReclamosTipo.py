# -*- coding: utf-8 -*-
import urllib2 as ur
url = 'https://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/RECLA-MENSU-POR-TIPO-DE/data.json?auth_key=44a38fbffd39c9f7d84e8e7dd2e1d02f0950e611&download=1'
data = ur.urlopen(url)


import json 

lectura = json.load(data)

print json.dumps(lectura, indent = 2, sort_keys=True) #imprime asi como viene 

sx = [] #ano
sy = [] #cantidad total


for reclamo in lectura :
    sx.append(int(reclamo['Año']))
    sy.append(int(reclamo['Total general']))

import matplotlib.pyplot as plt

fig = plt.figure()
graf1 = fig.add_subplot(111)
graf1.scatter(sx,sy, c='g', label = 'Reclamos x anio')
plt.legend(loc='upper left')
plt.show()
