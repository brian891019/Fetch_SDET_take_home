import subprocess
import json
import os

def command_helper(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout

#regular scenario with --locations flag
def test_city_state():
    command = ["python", "geoloc_utility.py", "--locations", "Madison, WI"]
    output = command_helper(command)
    data = json.loads(output)
    assert data[0]['place name'] == "Madison, Wisconsin"
    assert data[0]['country'] == "US"
    assert data[0]['latitude'] == 43.074761
    assert data[0]['longitude'] == -89.3837613

def test_zip_code():
    command = ["python", "geoloc_utility.py", "--locations", "60640"]
    output = command_helper(command)
    data = json.loads(output)
    assert data[0]['place name'] == "Chicago"
    assert data[0]['country'] == "US"
    assert data[0]['latitude'] == 41.9719
    assert data[0]['longitude'] == -87.6624

#regular scenario with positional arguments
def test_city_state_positional():
    command = ["python", "geoloc_utility.py", "--locations", "Madison, WI"]
    output = command_helper(command)
    data = json.loads(output)
    assert data[0]['place name'] == "Madison, Wisconsin"
    assert data[0]['country'] == "US"
    assert data[0]['latitude'] == 43.074761
    assert data[0]['longitude'] == -89.3837613

def test_zip_code_positional():
    command = ["python", "geoloc_utility.py", "--locations", "60640"]
    output = command_helper(command)
    data = json.loads(output)
    assert data[0]['place name'] == "Chicago"
    assert data[0]['country'] == "US"
    assert data[0]['latitude'] == 41.9719
    assert data[0]['longitude'] == -87.6624

def test_multiple_input():
    #zip code 
    command = ["python", "geoloc_utility.py", "--locations", "60640", '12345','40840']
    #city state
    command_2 =["python", "geoloc_utility.py", "Chicago, IL", 'New york, Ny','Michigan, Mi']
    #mixed zipcode and city state
    command_3 =["python", "geoloc_utility.py", "--locations", "50320", 'New york, Ny','60654']
    output ,output2 ,output3 = command_helper(command), command_helper(command_2), command_helper(command_3)
    data, data2, data3 = json.loads(output), json.loads(output2), json.loads(output3)
    data_sets = [data, data2, data3]
    for data_set in data_sets:
        assert len(data_set) == 3
        for location in data_set:
            assert 'place name' in location 
            assert 'country' in location 
            assert 'latitude' in location
            assert 'longitude' in location

def test_invalid_input():
    command = ["python", "geoloc_utility.py", "--locations", "20"]
    output = command_helper(command)
    assert output == 'location cannot be find. API returned ERROR. Error message Not Found, Error number 404\n[]\n'

def test_invalid_input2():
    command = ["python", "geoloc_utility.py", "--locations", "Chicago"]
    output = command_helper(command)
    assert output == 'location cannot be find. API returned ERROR. Error message Not Found, Error number 404\n[]\n'

def test_invalid_input3():
    command = ["python", "geoloc_utility.py", "--locations"]
    output = command_helper(command)
    assert output == 'Please provide location\n'

def test_missing_comma():
    command = ["python", "geoloc_utility.py", "--locations", "Madison WI"]
    output = command_helper(command)
    assert output == 'location cannot be find. API returned ERROR. Error message Not Found, Error number 404\n[]\n'

#unmatch city and state
def test_incorrect_state():
    command = ["python", "geoloc_utility.py", "--locations", "New York, Nc"]
    output = command_helper(command)
    assert output == '[]\n'

#incorrect city name
def test_incorrect_city():
    command = ["python", "geoloc_utility.py", "--locations", "abcdefgj, Ny"]
    output = command_helper(command)
    assert output == '[]\n'

#zipcode with letter
def test_zip_with_number():
    command = ["python", "geoloc_utility.py", "--locations", "12fa8"]
    output = command_helper(command)
    assert output == 'location cannot be find. API returned ERROR. Error message Not Found, Error number 404\n[]\n'


if __name__ == "__main__":
    os.system("pytest test_geoloc_util.py")