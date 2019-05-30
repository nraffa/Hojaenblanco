#duda para que el request?? (urllib.request)
#duda para que el .read()

#import urllib.request, json #para que seria el ,json?
import urllib2
import json
url = 'https://data.seattle.gov/resource/tmmm-ytt6.json'
json_obj0 = urllib2.urlopen(url)
data0 = json.loads(json_obj0.read())
print data0['checkoutyear']
#for item in data0['usageclass']:
 #   print item['checkoutyear']
#print(json.dumps(rawcheckout, indent=4, sort_keys=True))
#print(rawcheckout[1])


quit()
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
print data

print data ['data']