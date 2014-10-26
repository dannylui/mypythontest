#!/usr/bin/python

import sys
import getopt
import json
import urllib
import urllib2
import simplejson

def main(argv):
	address = ''
	try:
		opts, args = getopt.getopt(argv,"hi:")
	except getopt.GetoptError:
		print 'test.py -i "<address>"'
		sys.exit()
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i "<address>"'
			sys.exit()
		elif opt in ("-i"):
			address = arg

	if address == '':
		print 'test.py -i "<address>"'
		sys.exit()

	print 'DEBUG: address is :', address
	
	url = 'http://maps.googleapis.com/maps/api/geocode/json'
	print 'DEBUG: url is :', url


	parms = urllib.urlencode({'address' : address})
	print 'DEBUG: url encoded is: ', parms

	try:
		req = urllib2.Request(url + "?" + parms)
		response = urllib2.urlopen(req)
	except:
		print 'ERROR: Failed to fetch: ', url
		sys.exit()

	json_data = response
	
	#responseraw = response.read()
	#print responseraw

	try:
		data = json.load(json_data)
	except:
		print 'ERROR: response is not json'
		sys.exit()

	json_data.close()

	if data["status"] == "OK":
		print 'I found the following results:'
		for i in (data["results"]):
			print 'Coords: (', i["geometry"]["location"]["lat"], ', ', i["geometry"]["location"]["lng"] , ')'
	else:
		print 'Sorry, I did not find any results, blah'

if __name__ == "__main__":
	main(sys.argv[1:])

