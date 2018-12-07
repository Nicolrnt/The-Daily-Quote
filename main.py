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
hour = 9
minute = 20

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
	sched.add_cron_job(createQuote, hour=hour, minute=minute)
	while (True):
		time.sleep(1)

# Launcher
if __name__ == "__main__":
	main()
