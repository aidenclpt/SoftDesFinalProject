from googleplaces import GooglePlaces, types, lang
from geopy.geocoders import Nominatim
from PIL import Image
import io

YOUR_API_KEY = 'AIzaSyDQBb_fJ3Ppby0et4BAHtj-0Lvtpd97Dc0'
geolocator = Nominatim()
latlong="42,-71"
location = geolocator.reverse(latlong)
print(location.address)
#print(location.raw)
google_places = GooglePlaces(YOUR_API_KEY)
query_result = google_places.nearby_search(
    location=latlong, keyword='Restaurants',
    radius=1000, types=[types.TYPE_RESTAURANT])

if query_result.has_attributions:
   print (query_result.html_attributions)


for place in query_result.places:
    # print (place.name)
    # print (place.geo_location)
    print (place.vicinity)
    print(place.rating)
    place.get_details()
    print (place.photos)
    for photo in place.photos:
          photo.get(maxheight=500, maxwidth=500)
          image = Image.open(io.BytesIO(photo.data))
          image.show()
