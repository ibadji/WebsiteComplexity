# WebsiteComplexity
## Description
In the research “Understanding Website Complexity: Measurements, Metrics, and Implications” by Michael Butkiewicz, Harsha V. Madhyastha and Vyas Sekar it was stated that extensive researches were made during the past years to understand website’s popularity and web traffic but little attention was given to website complexity. As such the research tackled the question focusing on two main aspects: content level (e.g., pages load times..) and service- level (e.g., number of servers/origins). Concluding that page load times were mainly affected by the number and type of content fetched by the website as well as the number of servers used (whether origin or not didn’t make a significant difference). 

## What is in the files
### HAR Generator:
	Is composed of two main parts, a generator that takes an array (of websites) and a numer of repetition and creates two HAR files
	(performance and general information) for each website for each run.
	The second part is the HARParser, which reads throught the HAR files for each website, combine informations and prints them on the shell.
### HAR Runable: 
	Accesses the HARGenerator to facilitate the execution of the code. it is ennough to specify an import of both generate method and parse.
	specify an array and an integer(number of repetition)

Note: 
	The chrome driver file need to be added directly to the python folder where the scripts are found
	The browser server mob proxy file need to be added anythwere and it's path specified in the HARGenerator code.
	The HAR files will be automatically saved to the python file. 

## Installation:
The following needs to be installed using pip
	- from browsermobproxy import Server: pip install browsermob-proxy
	- from selenium import webdriver: pip install selenium
	- from splinter import Browser: pip install splinter
	- import json: pip install simplejson
	- import argparse: pip install argparse
	- from haralyzer import HarPage: pip install haralyzer
	- from statistics import mean: pip install statistics
The chromedriver needs also to be downloaded as well as browsermod-proxy
