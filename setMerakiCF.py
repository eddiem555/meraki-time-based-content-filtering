#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Set global Meraki Content Filter Policy based on argument passed in
Author:      eddiem@cisco.com
License:     Copyright (c) 2021 Cisco and/or its affiliates.
             This software is licensed to you under the terms of the Cisco Sample
             Code License, Version 1.1 (the "License"). You may obtain a copy of the
             License at https://developer.cisco.com/docs/licenses
             All use of the material herein must be in accordance with the terms of
             the License. All rights not expressly granted by the License are
             reserved. Unless required by applicable law or agreed to separately in
             writing, software distributed under the License is distributed on an "AS
             IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
             or implied.

"""

import sys
import os
import requests
import json

MERAKI_API_KEY = ""
MERAKI_NET_ID = ""

# Sample Play time blocked categories (11 - Adult, 27 - Gambling)
PlayTime_CF = {
               "blockedUrlCategories":["meraki:contentFiltering/category/11",
                                       "meraki:contentFiltering/category/27"]
              }

# Sample Work time blocked categories (11 - Adult, 27 - Gambling, 34 - Games)
WorkTime_CF = {
               "blockedUrlCategories":["meraki:contentFiltering/category/11",
                                       "meraki:contentFiltering/category/27",
                                       "meraki:contentFiltering/category/34"]
              }

#########################################################################
# Utility function to get all available Content Filtering Categories 
#########################################################################
def get_All_CF_Categories ():
  url = "https://api.meraki.com/api/v0/networks/{}/contentFiltering/categories".format(MERAKI_NET_ID)
  payload = None

  headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
  }
  response = requests.request('GET', url, headers=headers, data=payload)
  obj = json.loads(response.text.encode('utf8'))
  for cat in obj["categories"]:
    print ("Name: {}, ID: {}".format(cat["name"], cat["id"]))


#########################################################################
# Get existing Content Filtering policy and print
#########################################################################
def get_CF ():
  url = "https://api.meraki.com/api/v1/networks/{}/appliance/contentFiltering".format(MERAKI_NET_ID)
  payload = None

  headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
  }
  response = requests.request('GET', url, headers=headers, data=payload)
  obj = json.loads(response.text.encode('utf8'))
  for cat in obj["blockedUrlCategories"]:
    print ("Name: {}, ID: {}".format(cat["name"], cat["id"]))

#########################################################################
# Set Content Filtering policy
#########################################################################
def usage ():
  print("Usage: setMerakiCF.py [ work | play | printallcategories | printpolicy ]")
  print("       work: Set content filtering policy for work hours")
  print("       play: Set content filtering policy for non-work hours")
  print("       printallcategories: Prints all content filtering category names & IDs")
  print("       printpolicy: Prints blocked categories in your content filtering policy")
  print("")       
  sys.exit()
 
#########################################################################
# Set Content Filtering policy
#########################################################################
def set_CF (policy):
  url = "https://api.meraki.com/api/v1/networks/{}/appliance/contentFiltering".format(MERAKI_NET_ID)

  payload = json.dumps(WorkTime_CF)
  if policy == 'play':
    payload = json.dumps(PlayTime_CF)

  headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
  }

  response = requests.request('PUT', url, headers=headers, data=payload)

######################################################################
# MAIN
######################################################################
if __name__ == "__main__":

  if len(sys.argv) != 2:
    usage()
        
  arg = sys.argv[1]
  if ((arg != "work") and (arg != "play") and (arg != "printallcategories") and (arg != "printpolicy")):
    usage()

  if ((not MERAKI_API_KEY) or (not MERAKI_NET_ID)):
    print("Error: API key or Network ID missing")
    sys.exit()

  if (arg == "printallcategories"):
    get_All_CF_Categories()
    sys.exit()

  if (arg == "printpolicy"):
    get_CF()
    sys.exit()

  set_CF(arg)
