# -*- coding: utf-8 -*-
#
# Author : Nicolas Laurent <nicolas-laurent@outlook.fr>
# File   : main.py
#

# Imports
from apscheduler.scheduler import Scheduler
import webbrowser
import requests
import time
import json
import os

# Quote Config
hour = 13
minute = 45

# Start the scheduler
sched = Scheduler()
sched.start()

# Update Index
def updateIndex(quote, author):
	template = open("./template/template.html", "r")
	index = open("./template/index.html", "w")

	code = template.read()
	code = code.replace("{quote}", quote)
	code = code.replace("{author}", author)
	index.write(code)

# Update Style
def updateStyle(background):
	template = open("./template/assets/css/template.css", "r")
	style = open("./template/assets/css/main.css", "w")

	code = template.read()
	code = code.replace("{background}", background)
	style.write(code)

# Create Quote
def createQuote():
	url = "http://quotes.rest/qod.json?category=inspire"
	ret = """{
		"success": {
			"total": 1
		},
		"contents": {
			"quotes": [
				{
					"quote": "If you get up in the morning and think the future is going to be better, it is a bright day. Otherwise, it's not.",
					"length": "113",
					"author": "Elon Musk",
					"tags": [
						"inspire",
						"positive-thinking"
					],
					"category": "inspire",
					"date": "2018-12-05",
					"permalink": "https://theysaidso.com/quote/mbtVO88S_KNdB4gBMyXaUgeF/elon-musk-if-you-get-up-in-the-morning-and-think-the-future-is-going-to-be-bette",
					"title": "Inspiring Quote of the day",
					"background": "https://theysaidso.com/img/bgs/man_on_the_mountain.jpg",
					"id": "mbtVO88S_KNdB4gBMyXaUgeF"
				}
			],
			"copyright": "2017-19 theysaidso.com"
		}
	}"""

	# Make Request
	ret = requests.get(url)
	print(ret.text)
	# Get Variables
	obj = json.loads(ret.text)
	quote = obj["contents"]["quotes"][0]["quote"]
	author = obj["contents"]["quotes"][0]["author"]
	background = obj["contents"]["quotes"][0]["background"]
	# Update Website
	updateIndex(quote, author)
	updateStyle(background)
	# Open Window
	webbrowser.open("file://" + os.path.realpath("./template/index.html"))

# Main
def main():
	#createQuote()
	#sched.add_cron_job(createQuote, hour=hour, minute=minute)
	#sched.add_cron_job(createQuote, second=0)
	while (True):
		time.sleep(1)

# Launcher
if __name__ == "__main__":
	main()

# pip3 install requests
# pip install apscheduler==2.1.2
