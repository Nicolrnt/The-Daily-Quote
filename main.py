# -*- coding: utf-8 -*-
#
# Author : Nicolas Laurent <nicolas-laurent@outlook.fr>
# File   : main.py
#

import requests
import json

def updateIndex(quote, author):
	template = open("./template/template.html", "r")
	index = open("./template/index.html", "w")

	code = template.read()
	code = code.replace("{quote}", quote)
	code = code.replace("{author}", author)
	index.write(code)

def updateStyle(background):
	template = open("./template/assets/css/template.css", "r")
	style = open("./template/assets/css/main.css", "w")

	code = template.read()
	code = code.replace("{background}", background)
	style.write(code)

def main():
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
	# ret = requests.get(url)
	# Get Variables
	obj = json.loads(ret)
	quote = obj["contents"]["quotes"][0]["quote"]
	author = obj["contents"]["quotes"][0]["author"]
	date = obj["contents"]["quotes"][0]["date"]
	background = obj["contents"]["quotes"][0]["background"]
	# Update Website
	updateIndex(quote, author)
	updateStyle(background)

# Launcher
if __name__ == "__main__":
	main()

# pip3 install requests