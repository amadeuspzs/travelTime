#!/usr/bin/python
import urllib, json, time, argparse

# Create CLI interface
parser = argparse.ArgumentParser(description='Capture realtime traffic data')
parser.add_argument('-q', action='store_true', help='Quiet mode, only output successful csv')
parser.add_argument('origin', help='Where are you starting your journey')
parser.add_argument('destination', help='Where are you ending your journey')

args = parser.parse_args()

origin = args.origin
destination = args.destination
quiet = args.q

# Enter your Google Maps API key below:
apiKey=""
if not apiKey:
  print "Enter your API key for traffic data!"
  exit(1)

# Try to grab realtime traffic from Google:
params = urllib.urlencode(
    {'origin': origin, 
     'destination': destination, 
     'mode': 'driving', 
     'key': apiKey, 
     'departure_time':'now'})

url = "https://maps.googleapis.com/maps/api/directions/json?%s" % params

timestamp = int(time.time()) # capture when the request is made

try:
  response = urllib.urlopen(url)
except IOError, e:
  if not quiet:
    print e
  exit(1)

if response.getcode() == 200:
  data = json.loads(response.read())
else:
  if not quiet:
    print "Error %s" % response.getcode()
  exit(1)

# Process response data
if 'error_message' in data:
  if not quiet:
    print data['error_message']
  exit(1)

if not 'routes' in data or len(data['routes']) < 1:
  if not quiet:
    print "Route data not returned. Check locations?"
  exit(1)
elif not 'duration_in_traffic' in data['routes'][0]['legs'][0]:
  if not quiet:
    print "Traffic data not returned"
  exit(1)
else:
  print "%s,%s" % (timestamp, data['routes'][0]['legs'][0]['duration_in_traffic']['value'])