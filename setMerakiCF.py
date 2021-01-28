#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Set Meraki Content Filter Policy based on argument passed in
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

MERAKI_API_KEY = ""
MERAKI_NET_ID = ""

#########################################################################
# Get Content Filtering policy and print
#########################################################################
def get_CF ():
  # Get Content Filtering Categories
  url = "https://api.meraki.com/api/v1/networks/{}/appliance/contentFiltering".format(MERAKI_NET_ID)
  payload = None

  headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-Cisco-Meraki-API-Key": MERAKI_API_KEY
  }
  response = requests.request('GET', url, headers=headers, data=payload)
  print(response.text.encode('utf8'))


#########################################################################
# Set Content Filtering policy
# Play Time Category restricted: 11-Adult, 27-Gambling
# Work Time Category restricted: 11-Adult, 27-Gambling, 34-Games
#########################################################################
def set_CF (policy):
  PlayTime_CF = '{"blockedUrlCategories":["meraki:contentFiltering/category/11","meraki:contentFiltering/category/27"]}'
  WorkTime_CF = '{"blockedUrlCategories":["meraki:contentFiltering/category/11","meraki:contentFiltering/category/27","meraki:contentFiltering/category/34"]}'

  url = "https://api.meraki.com/api/v1/networks/{}/appliance/contentFiltering".format(MERAKI_NET_ID)

  if policy == 'work':
    payload = WorkTime_CF
  else:Dlicy == 'play':
    payload = PlayTime_CF

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
    print("Usage: setMerakiCF [work | play]")
    sys.exit()
        
  arg = sys.argv[1]
  if ((arg != "work") and (arg != "play")):
    print("Usage: setMerakiCF [work | play]")
    sys.exit()

  if ((not MERAKI_API_KEY) or (not MERAKI_NET_ID)):
    print("Error: API key or Network ID missing")
    sys.exit()

  # Set Content Filter
  set_CF(arg)
