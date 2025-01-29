# geolocation utility

using Open Weather Geocoding API to get the geolocation informations


## Prerequisites
1. Python 3 is installed
2. Ensure the pip tool is installed for Python.
3. Install pytest and other dependencies using the provided requirements.txt.


## installation
1. Create a Python virtual enviroment(recommended not required)
tutorial : https://docs.python.org/3/library/venv.html

2. activate your PVE and Clone the repository or download the utility script:
```bash
git clone https://github.com/brian891019/Fetch_SDET_take_home.git
cd geolocation-utility
```
3. Install the necessary dependencies:
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
## Testing
This section describes how to run integration tests on the geolocation utility to ensure it functions correctly under various scenarios. The tests cover valid and invalid inputs, including city/state combinations and zip codes.

1. Place the test script (test_geoloc_util.py) in the same directory as your utility script (geoloc_util.py).

2. Run the test using Pytest
```bash
python -m pytest test_geoloc_utility.py 
```

3. (optional)increase verbosity of output. -v shows more detailed information about each test, including their names and outcomes.
```bash
python -m pytest test_geoloc_utility.py -v
```

## Error messages
In case of errors, the utility will print a message identifying the issue. Common errors are related to invalid input or issues with the OpenWeather API.

Refer to this https://restfulapi.net/http-status-codes/ Status Code Reference for understanding the API error codes.