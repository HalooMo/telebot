#pip install phonenumbers
#pip install opencage
#pip install folium
import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "ru")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "ru"))

from opencage.geocoder import OpenCageGeocode

key = 'ec3ae7868562427a80d57a1a831241bf'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
