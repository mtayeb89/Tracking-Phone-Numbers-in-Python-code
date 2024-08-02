import phonenumbers
from phonenumbers import geocoder,timezone, carrier
import folium
from opencage.geocoder import OpenCageGeocode
print('^_^ '*20)

entered_num='+201289454302'
phone_no=phonenumbers.parse(entered_num)
print(phone_no)
number_location=geocoder.description_for_number(phone_no,'en')
print(number_location)
print(carrier.name_for_number(phone_no,"en"))
print(timezone.time_zones_for_number(phone_no))
service_provider=phonenumbers.parse(entered_num)
print(service_provider)

#
geocoder=OpenCageGeocode('68b8780d854f4b38a47a699d02c2d8ef')
query=str(number_location)
result=geocoder.geocode(query)
# Latitude line
lat=result[0]['geometry']['lat']
# Longitude line
lng=result[0]['geometry']['lng']
print(lat,lng)
map_location=folium.Map(location=[lat,lng],zoom_start=11)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save('My_loc.html')