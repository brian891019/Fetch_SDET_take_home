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
    

def get_location_by_name(city_state: str):
    """
    get geolocation data through city and state

    :return: geolocation data if found, else None.
    :rtype: JSON
    """
    url: str = "http://api.openweathermap.org/geo/1.0/direct"
    parammeters = {'q': city_state, 'appid': "f897a99d971b5eef57be6fafa0d83239",'limit': 1}
    response = requests.get(url,params=parammeters)

    #4xx Status Codes (Client Error)
    if response.status_code  >= 400:
        return f"location cannot be find. API returned ERROR. Error message {response.reason}, Error number {response.status_code}"
    else:
        return response.json()


if __name__ == '__main__':
    print(get_location_by_zip_code("60640"))
    print(get_location_by_name("Chicago, IL"))