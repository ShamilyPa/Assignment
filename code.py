import requests
import sys

# Assigning the omdbapi url with movie name to a variable
url = 'http://www.omdbapi.com/?apikey=44bf33cb&t='+sys.argv[1]

k = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = k.json()

# Print rotten tomatoes ratings

for match,s  in json_data.items():
       if match == 'Ratings':
            print s[1].get('Source') + ':' +  s[1].get('Value')


