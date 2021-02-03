# Meraki time-based Content Filtering Policy

## INTRODUCTION

This project presents a simple Python script to update Meraki Content Filtering Policy. Used in conjuction with a scheduler such as Linux cron, or Windows Task Scheduler, it allows for time-based Meraki content filtering without the overhead of creating a full blown Meraki client based group policy configuration.

## EXTERNAL DEPENDENCIES

Only dependencies are Python 3 with 'requests' and 'json' packages.

## USAGE

Usage is as follows: 
setMerakiCF.py [ work | play | printallcategories | printpolicy ]
       work: Set content filtering policy for work hours
       play: Set content filtering policy for non-work hours
       printallcategories: Prints all content filtering category names & IDs
       printpolicy: Prints blocked categories in your content filtering policy

To set your content filtering policy, simply modify 'PlayTime_CF' and 'WorkTime_CF' constants in the code to match your policy.

To print existing blocked categories in your content filtering policy, use the 'printpolicy' argument.

To print a list of all available category names & IDs, use the 'printallcategories' argument. 

