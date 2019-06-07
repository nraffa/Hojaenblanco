# Python 3
# tutorial en youtube, https://www.youtube.com/watch?v=9N6a-VLBa2I
import json

states_string = '''
{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL",
      "area_codes": ["205", "251", "256", "334", "938"]
    },
    {
      "name": "Alaska",
      "abbreviation": "AK",
      "area_codes": ["907"]
    },
    {
      "name": "Arizona",
      "abbreviation": "AZ",
      "area_codes": ["480", "520", "602", "623", "928"]
    },
    {
      "name": "Arkansas",
      "abbreviation": "AR",
      "area_codes": ["479", "501", "870"]
    },
    {
      "name": "California",
      "abbreviation": "CA",
      "area_codes": ["209", "213", "310", "323", "408", "415", "424", "442", "510", "530", "559", "562", "619", "626", "628", "650", "657", "661", "669", "707", "714", "747", "760", "805", "818", "831", "858", "909", "916", "925", "949", "951"]
    },
    {
      "name": "Colorado",
      "abbreviation": "CO",
      "area_codes": ["303", "719", "720", "970"]
    },
    {
      "name": "Connecticut",
      "abbreviation": "CT",
      "area_codes": ["203", "475", "860", "959"]
    },
    {
      "name": "Delaware",
      "abbreviation": "DE",
      "area_codes": ["302"]
    },
    {
      "name": "Florida",
      "abbreviation": "FL",
      "area_codes": ["239", "305", "321", "352", "386", "407", "561", "727", "754", "772", "786", "813", "850", "863", "904", "941", "954"]
    },
    {
      "name": "Georgia",
      "abbreviation": "GA",
      "area_codes": ["229", "404", "470", "478", "678", "706", "762", "770", "912"]
    },
    {
      "name": "Hawaii",
      "abbreviation": "HI",
      "area_codes": ["808"]
    },
    {
      "name": "Idaho",
      "abbreviation": "ID",
      "area_codes": ["208"]
    },
    {
      "name": "Illinois",
      "abbreviation": "IL",
      "area_codes": ["217", "224", "309", "312", "331", "618", "630", "708", "773", "779", "815", "847", "872"]
    },
    {
      "name": "Indiana",
      "abbreviation": "IN",
      "area_codes": ["219", "260", "317", "463", "574", "765", "812", "930"]
    },
    {
      "name": "Iowa",
      "abbreviation": "IA",
      "area_codes": ["319", "515", "563", "641", "712"]
    },
    {
      "name": "Kansas",
      "abbreviation": "KS",
      "area_codes": ["316", "620", "785", "913"]
    },
    {
      "name": "Kentucky",
      "abbreviation": "KY",
      "area_codes": ["270", "364", "502", "606", "859"]
    },
    {
      "name": "Louisiana",
      "abbreviation": "LA",
      "area_codes": ["225", "318", "337", "504", "985"]
    },
    {
      "name": "Maine",
      "abbreviation": "ME",
      "area_codes": ["207"]
    },
    {
      "name": "Maryland",
      "abbreviation": "MD",
      "area_codes": ["240", "301", "410", "443", "667"]
    },
    {
      "name": "Massachusetts",
      "abbreviation": "MA",
      "area_codes": ["339", "351", "413", "508", "617", "774", "781", "857", "978"]
    },
    {
      "name": "Michigan",
      "abbreviation": "MI",
      "area_codes": ["231", "248", "269", "313", "517", "586", "616", "734", "810", "906", "947", "989"]
    },
    {
      "name": "Minnesota",
      "abbreviation": "MN",
      "area_codes": ["218", "320", "507", "612", "651", "763", "952"]
    },
    {
      "name": "Mississippi",
      "abbreviation": "MS",
      "area_codes": ["228", "601", "662", "769"]
    },
    {
      "name": "Missouri",
      "abbreviation": "MO",
      "area_codes": ["314", "417", "573", "636", "660", "816"]
    },
    {
      "name": "Montana",
      "abbreviation": "MT",
      "area_codes": ["406"]
    },
    {
      "name": "Nebraska",
      "abbreviation": "NE",
      "area_codes": ["308", "402", "531"]
    },
    {
      "name": "Nevada",
      "abbreviation": "NV",
      "area_codes": ["702", "725", "775"]
    },
    {
      "name": "New Hampshire",
      "abbreviation": "NH",
      "area_codes": ["603"]
    },
    {
      "name": "New Jersey",
      "abbreviation": "NJ",
      "area_codes": ["201", "551", "609", "732", "848", "856", "862", "908", "973"]
    },
    {
      "name": "New Mexico",
      "abbreviation": "NM",
      "area_codes": ["505", "575"]
    },
    {
      "name": "New York",
      "abbreviation": "NY",
      "area_codes": ["212", "315", "332", "347", "516", "518", "585", "607", "631", "646", "680", "716", "718", "845", "914", "917", "929", "934"]
    },
    {
      "name": "North Carolina",
      "abbreviation": "NC",
      "area_codes": ["252", "336", "704", "743", "828", "910", "919", "980", "984"]
    },
    {
      "name": "North Dakota",
      "abbreviation": "ND",
      "area_codes": ["701"]
    },
    {
      "name": "Ohio",
      "abbreviation": "OH",
      "area_codes": ["216", "220", "234", "330", "380", "419", "440", "513", "567", "614", "740", "937"]
    },
    {
      "name": "Oklahoma",
      "abbreviation": "OK",
      "area_codes": ["405", "539", "580", "918"]
    },
    {
      "name": "Oregon",
      "abbreviation": "OR",
      "area_codes": ["458", "503", "541", "971"]
    },
    {
      "name": "Pennsylvania",
      "abbreviation": "PA",
      "area_codes": ["215", "267", "272", "412", "484", "570", "610", "717", "724", "814", "878"]
    },
    {
      "name": "Rhode Island",
      "abbreviation": "RI",
      "area_codes": ["401"]
    },
    {
      "name": "South Carolina",
      "abbreviation": "SC",
      "area_codes": ["803", "843", "854", "864"]
    },
    {
      "name": "South Dakota",
      "abbreviation": "SD",
      "area_codes": ["605"]
    },
    {
      "name": "Tennessee",
      "abbreviation": "TN",
      "area_codes": ["423", "615", "629", "731", "865", "901", "931"]
    },
    {
      "name": "Texas",
      "abbreviation": "TX",
      "area_codes": ["210", "214", "254", "281", "325", "346", "361", "409", "430", "432", "469", "512", "682", "713", "737", "806", "817", "830", "832", "903", "915", "936", "940", "956", "972", "979"]
    },
    {
      "name": "Utah",
      "abbreviation": "UT",
      "area_codes": ["385", "435", "801"]
    },
    {
      "name": "Vermont",
      "abbreviation": "VT",
      "area_codes": ["802"]
    },
    {
      "name": "Virginia",
      "abbreviation": "VA",
      "area_codes": ["276", "434", "540", "571", "703", "757", "804"]
    },
    {
      "name": "Washington",
      "abbreviation": "WA",
      "area_codes": ["206", "253", "360", "425", "509"]
    },
    {
      "name": "West Virginia",
      "abbreviation": "WV",
      "area_codes": ["304", "681"]
    },
    {
      "name": "Wisconsin",
      "abbreviation": "WI",
      "area_codes": ["262", "414", "534", "608", "715", "920"]
    },
    {
      "name": "Wyoming",
      "abbreviation": "WY",
      "area_codes": ["307"]
    }
  ]
}
'''
data = json.loads(states_string)
#indent los ordena por nivel
#sort key los ordena alfabeticamente
newnew_string = json.dumps(data,indent=2,sort_keys=True) 
print(newnew_string)
quit()
#object a dict
print (type(data))
#array a list, osea states es una list
print (type(data['states']))

#imprime por separado lo que busque
#en este caso, le pedi la abreviacion
for state in data['states'] :
    print (state['abbreviation'])

#elimino el codigo de area y el nombre de los datos
for state in data['states']:
     del state['area_codes']
     del state['name']
#redefino los datos modificados
new_string = json.dumps(data, indent=2) #para que es el dumps?

print(new_string)



