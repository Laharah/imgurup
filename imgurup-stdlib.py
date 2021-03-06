#!/usr/bin/python2
# coding: utf-8
# Author: David Davidson 
# Twitter: @dailydavedavids
# Licence: WTFPL
# Version: 20150731.1
import urllib2
import urllib
import base64
import json
import sys
import os

def upload(image_path, client_id):
    try:
        f = open(image_path, "rb") # open file for reading, binary mode
    except Exception: # I should do something with the exception. Later I will add logging for these
        sys.exit("{!} That file does not exist!") # for now, just bail
    b64image = base64.standard_b64encode(f.read()) # base64 encode the image data
    headers = {'Authorization': 'Client-ID '+client_id} # set the client id in auth header
    data = {'image': b64image, 'title': '%s' %(os.path.basename(image_path))} # make post data
    try:
        request = urllib2.Request(url="https://api.imgur.com/3/upload.json", data=urllib.urlencode(data), headers=headers) # create request
        response = urllib2.urlopen(request).read() # send request
    except Exception, e: # catch the exception if something goes wrong
        print "{-} Image Upload Failed. Printing stack trace and exiting..." # bail.
        sys.exit(str(e)) # print the stacktrace. Later, I should figure out what kind of exceptions happen and handle them and log them
    lol = json.loads(response) # get the json...
    print lol['data']['link'] # print the link

def main(args):
    # some of the logic in here is a bit backwards. I should probably fix this to make it more nice
    if len(args) != 2: # only 2 args needed
        sys.exit("use: %s /path/to/image/file.ext" %(args[0])) # exit with usage 
    else:
       pass # we can continue
    client_id_env_var = 'IMGUR_CLIENT_ID' 
    if client_id_env_var in os.environ.keys(): # check if env var exist
        client_id = os.environ[client_id_env_var] # get it and save it
    else:
        sys.exit("{!} Set environmental variable IMGUR_CLIENT_ID to your client_id :)")
    upload(image_path=args[1], client_id=client_id)

if __name__ == "__main__":
    main(args=sys.argv)
