from googleplaces import GooglePlaces, types, lang
from geopy.geocoders import Nominatim
import tkinter as tk
from PIL import Image, ImageTk
import io
YOUR_API_KEY = 'AIzaSyDQBb_fJ3Ppby0et4BAHtj-0Lvtpd97Dc0'
geolocator = Nominatim()
latlong="42,-71"



def reverse_search(latlong):
    """Reverse searches the Google Maps API,give it a latitude and longitude and returns an address"""
    location = geolocator.reverse(latlong)
    #print(location.address)

def find_attraction(latlong):
    """Searches google for nearby attractions as specified by user, ie. parks"""
    google_places = GooglePlaces(YOUR_API_KEY)
    query_result = google_places.nearby_search(
        location = latlong, keyword='Park',
        radius = 10000, types=[types.TYPE_PARK])
    #if query_result.has_attributions:
        #print (query_result.html_attributions)
    return query_result

def attraction_info(query_result):
    """For each google result, the program prints the address of the attraction, website, and rating. Then prints one photo per attraction mentioned. More photos can be printed by editing the statement if num<2."""
    window = tk.Toplevel()
    geo_root = tk.Toplevel()
    for place in query_result.places:
        num = 1
        place.get_details()
        # print(place.name)
        # print(place.vicinity)
        # print(place.website)
        # print(place.rating)
        for photo in place.photos:
            #print(photo)
            # print(photo.data)
            if num<2:
                if place.website:
                    #info=str(place.vicinity)+"/n" +str(place.website)+ "/n" +str(place.rating)
                    info="{}\n{}\n{}".format(str(place.vicinity),str(place.website),str(place.rating))
                else:
                    info="{}\n{}".format(str(place.vicinity),str(place.rating))
                photo.get(maxheight=500, maxwidth=500)
                window.title(str(place.name))
                w = tk.Label(geo_root, text=info)
                window.geometry("300x300")
                window.configure(background='grey')
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(photo.data)))
                print(type(img))
                panel = tk.Label(window, image = img)
                panel.pack(side = "right", fill = "x", expand = "yes")
                num=num+1
        w.pack()
        geo_root.mainloop()
        # return
        return img
if __name__ == "__main__":
    window = tk.Tk()
    geo_root = tk.Tk()

    address=reverse_search(latlong)
    att=find_attraction(latlong)
    attraction_info(att, geo_root, window)
    # z
