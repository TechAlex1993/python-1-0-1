import webbrowser

def find_city_google_maps(city):
    # Format the URL with the search query
    find_city_google_maps = f"https://earth.google.com/web/search/{city}"
    webbrowser.open(find_city_google_maps)

    # Find the city on Google Maps
find_city_google_maps(input("Enter the city name: "))
    
   
