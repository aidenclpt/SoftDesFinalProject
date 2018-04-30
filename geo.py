from googleplaces import GooglePlaces, types, lang
from geopy.geocoders import Nominatim
from PIL import Image
import io
YOUR_API_KEY = 'AIzaSyDQBb_fJ3Ppby0et4BAHtj-0Lvtpd97Dc0'
geolocator = Nominatim()
latlong="42,-71"

def reverse_search(latlong):
    """Reverse searches the Google Maps API,give it a latitude and longitude and returns an address"""
    location = geolocator.reverse(latlong)
    print(location.address)

def find_attraction(latlong):
    """Searches google for nearby attractions as specified by user, ie. parks"""
    google_places = GooglePlaces(YOUR_API_KEY)
    query_result = google_places.nearby_search(
        location = latlong, keyword='Park',
        radius = 3000, types=[types.TYPE_PARK])
    if query_result.has_attributions:
        print (query_result.html_attributions)
    return query_result

def attraction_info(query_result):
    """For each google result, the program prints the address of the attraction, website, and rating. Then prints one photo per attraction mentioned. More photos can be printed by editing the statement if num<2."""
    for place in query_result.places:
        num = 1
        place.get_details()
        print (place.name)
        print (place.vicinity)
        print(place.website)
        print(place.rating)
        for photo in place.photos:
            if num<2:
                photo.get(maxheight=500, maxwidth=500)
                image = Image.open(io.BytesIO(photo.data))
                image.show()
                num=num+1
        return places
if __name__ == "__main__":
    address=reverse_search(latlong)
    att=find_attraction(latlong)
    z=attraction_info(att)
    z
