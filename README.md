# geolocation utility

using Open Weather Geocoding API to get the geolocation informations


## Prerequisites
1. Python 3 is installed
2. Ensure the pip tool is installed for Python.

## installation

1. Clone the repository or download the utility script:

```bash
git clone https://github.com/brian891019/Fetch_SDET_take_home.git
cd geolocation-utility
```
2. Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Command Line Arguments

The geoloc-util command-line utility accepts an optional argument --locations or positional arguments. You can specify either zip codes or city/state information to fetch geolocation data.


Examples


Using the --locations optional argument:

```bash
python geoloc_util.py --locations "Madison, WI" "12345"
```

Using positional arguments without the --locations flag:


```bash
python geoloc_util.py "Madison, WI" "12345" "Chicago, IL" "10001"
```



Sample Outputs


```bash
[
    {
        "place name": "Madison, WI",
        "country": "US",
        "lat": 43.073051,
        "lon": -89.40123
    },
    {
        "place name": "Schenectady, NY",
        "country": "US",
        "lat": 42.8142432,
        "lon": -73.9395687
    },
    {
        "place name": "Chicago, IL",
        "country": "US",
        "lat": 41.878113,
        "lon": -87.629799
    },
    {
        "place name": "New York, NY",
        "country": "US",
        "lat": 40.712776,
        "lon": -74.005974
    }
]
```


## Error messages
In case of errors, the utility will print a message identifying the issue. Common errors are related to invalid input or issues with the OpenWeather API.

Refer to this https://restfulapi.net/http-status-codes/ Status Code Reference for understanding the API error codes.