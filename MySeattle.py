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