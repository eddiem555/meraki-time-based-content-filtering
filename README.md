# Meraki time-based Content Filtering Policy

## INTRODUCTION

This project presents a simple Python script to update Meraki Content Filtering Policy. Used in conjuction with a scheduler such as Linux cron, or Windows Task Scheduler, it allows for time-based Meraki content filtering without the overhead of creating a full blown Meraki client based group policy configuration.

## INSTALLATION

1. Ensure Python 3 is installed.
   * To download and install Python 3, please visit https://www.python.org.
2. Clone this repository, create a Python virtual environment and install Python dependencies.

```bash
git clone https://github.com/eddiem555/meraki-time-based-content-filtering.git

cd meraki-time-based-content-filtering

python3 -m venv venv

source venv/bin/activate

pip install requests
```
3. Insert your Meraki API Key & Network ID in setMerakiCF.py code, use existing MERAKI_API_KEY and MERAKI_NET_ID constant variables.
4. Optionally, use the provided crontab-sample.txt to modify your crontab to call setMerakiCF.py from the Linux cron scheduler.

## USAGE

Usage is as follows:
```
setMerakiCF.py [ work | play | printallcategories | printpolicy ]
       work: Set content filtering policy for work hours
       play: Set content filtering policy for non-work hours
       printallcategories: Prints all content filtering category names & IDs
       printpolicy: Prints blocked categories in your content filtering policy
```

  * To set your content filtering policy, simply modify 'PlayTime_CF' and 'WorkTime_CF' constants in the code to match your policy.
  * To print existing blocked categories in your content filtering policy, use the `'printpolicy'` argument.
  * To print a list of all available category names & IDs, use the `'printallcategories'` argument. 

