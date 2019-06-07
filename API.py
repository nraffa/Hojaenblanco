#duda: hay urllib 1, 2 y 3, diferencia?
#1 importo library para abrir urls
import urllib2 
#2 abro la url 
urllib2.urlopen('https://apis.datos.gob.ar/series/api/series/?ids=defensa_FAA_0006&limit=5000')
#duda como identificar el formato de la API (json, xml, csv )
#3 importo library json, porque la api labura con formato json
import json
# imprimo lo mismo que me apareceria si abriera la pagina, con toda la data 
# importante json.load(urllib2.urlopen('url'))
#print json.load (urllib2.urlopen('https://apis.datos.gob.ar/series/api/series/?ids=defensa_FAA_0006&limit=5000'))

# basicamente lo mismo pero mas estructurado
url = 'https://apis.datos.gob.ar/series/api/series/?ids=defensa_FAA_0006&limit=5000'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
print json.dumps(data,indent=2,sort_keys=True)
quit()
print data ['data']
print type(data)

#Performs the following translations in decoding by default:

#JSON / Python
#object/ dict
#array / list
#string / unicode
#number(int) / int, long
#number (real)/float
#true/True
#false/False
#null/None


