import argparse
import requests, sys, json

def get_location_by_zip_code(zip_code: str):
    """
    get geolocation data through zipcode

    :return: geolocation data if found, else None.
    :rtype: JSON
    """
    url: str = "http://api.openweathermap.org/geo/1.0/zip"
    parammeters = {'zip': zip_code, 'appid': "f897a99d971b5eef57be6fafa0d83239",'country': "US"}
    response = requests.get(url,params=parammeters)

    #4xx Status Codes (Client Error)
    if response.status_code  >= 400:
        print(f"location cannot be find. API returned ERROR. Error message {response.reason}, Error number {response.status_code}")
        return None
    else:
        return response.json()
    

def get_location_by_name(city: str, state: str):
    """
    get geolocation data through city and state

    :return: geolocation data if found, else None.
    :rtype: JSON
    """
    url: str = "http://api.openweathermap.org/geo/1.0/direct"
    
    parammeters = {'q': f"{city},{state},{'US'}", 'appid': "f897a99d971b5eef57be6fafa0d83239",'limit': 1}
    response = requests.get(url,params=parammeters)

    #4xx Status Codes (Client Error)
    if response.status_code  >= 400:
        return f"location cannot be find. API returned ERROR. Error message {response.reason}, Error number {response.status_code}"
    else:
        return response.json()

def check_zip_city(locations):
    result = []
    formatted_data = None  
    for location in locations:
        if "," in location:
            location = location.split(",")
            geolocation_data = get_location_by_name(city = location[0].strip(), state = location[1].strip())
            if geolocation_data:
                formatted_data = {
                        'place name': f"{geolocation_data[0]['name']}, {geolocation_data[0].get('state', '')}",
                        'country': geolocation_data[0]['country'],
                        'latitude': geolocation_data[0]['lat'],
                        'longitude': geolocation_data[0]['lon']
                    }
            else:
                print('error finding location')
        else:
            geolocation_data = get_location_by_zip_code(location)
            if geolocation_data:
                formatted_data = {
                        'place name': geolocation_data['name'],
                        'country': geolocation_data['country'],
                        'latitude': geolocation_data['lat'],
                        'longitude': geolocation_data['lon']
                    }
            else:
                print('error finding location')
        result.append(formatted_data)
       

    return result



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Geolocation Utility")
    
    # Define an optional --locations argument
    parser.add_argument('--locations', nargs='*')
    
    # Define an argument without --locations flag
    parser.add_argument('positional_locations', nargs='*')
    args = parser.parse_args()
    locations = args.locations if args.locations else args.positional_locations
    
    if not locations:
        print("Please provide at least one location either with --locations or as positional arguments.")
    else:
        print(json.dumps(check_zip_city(locations), indent=4, ensure_ascii=False))

    

