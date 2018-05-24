# WebsiteComplexity
HAR Generator:
	Is composed of two main parts, a generator that takes an array (of websites) and a numer of repetition and creates two HAR files
	(performance and general information) for each website for each run.
	The second part is the HARParser, which reads throught the HAR files for each website, combine informations and prints them on the shell.
HAR Runable: 
	Accesses the HARGenerator to facilitate the execution of the code. it is ennough to specify an import of both generate method and parse.
	specify an array and an integer(number of repetition)

Note: 
	The chrome driver file need to be added directly to the python folder where the scripts are found
	The browser server mob proxy file need to be added anythwere and it's path specified in the HARGenerator code.
	The HAR files will be automatically saved to the python file. 

In order to install the diffrent libraries:
1-open cmd
2-access the script folder found in the python folder created during instalation.
Example: cd C:\Python34\Scripts

3-all the instalation instructions should be preceded by 'pip'

	-from browsermobproxy import Server: pip install browsermob-proxy
	-from selenium import webdriver: pip install selenium
	-from splinter import Browser: pip install splinter
	-import json: pip install simplejson
	-import argparse: pip install argparse
	-from urllib.parse import urlparse------------
	-import sys------------
	-import os------------
	-from haralyzer import HarPage: pip install haralyzer
	-from haralyzer import HarParser---------
	-from statistics import mean: pip install statistics
