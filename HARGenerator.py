#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Har file generator
from browsermobproxy import Server
from selenium import webdriver
from splinter import Browser
import json
import argparse
from urllib.parse import urlparse
import sys
import os
from haralyzer import HarPage
from haralyzer import HarParser
from statistics import mean

#Creates the HAR Files
class HARGenerator():
    #create performance data

    def __init__(self, mob_path):
        #initialize
        from datetime import datetime
        print ("%s: Go "%(datetime.now()))
        self.browser_mob = mob_path
        self.server = self.driver = self.proxy = None

    @staticmethod
    def __store_into_file(args,title, result,repetition):
        #store data collected into file
        if 'path' in args:
        	har_file = open(str(repetition)+['path']+'/'+title + '.har', 'w')
        else:
        	har_file = open(str(repetition)+title + '.har', 'w')
        har_file.write(str(result))
        har_file.close()

    def __start_server(self):
        #prepare and start server
        self.server = Server(self.browser_mob)
        self.server.start()
        self.proxy = self.server.create_proxy()

    def __start_driver(self,args,website):
        #prepare and start driver
        
        #chromedriver
            print ("Browser: Chrome")
            print ("URL: {0}".format(website))
            #chrome driver needs to be dowloaded and path precised bellow
            chromedriver = os.getenv("CHROMEDRIVER_PATH", "C:\\Users\ines\Desktop\\chromedriver.exe")
            os.environ["webdriver.chrome.driver"] = chromedriver
            url = urlparse (self.proxy.proxy).path
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--proxy-server={0}".format(url))
            chrome_options.add_argument("--no-sandbox")
            desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
            desired_capabilities['proxy'] = {
                "httpProxy":url,
                "ftpProxy":url,
                "sslProxy":url,
                "noProxy":None,
                "proxyType":"MANUAL",
                "class":"org.openqa.selenium.Proxy",
                "autodetect":True
            }
            self.driver = webdriver.Chrome()
		
			

    def start_all(self,args,website):
        #start server and driver
        self.__start_server()
        self.__start_driver(args,website)

    def create_har(self,args,website,repetition):
        #start request and parse response
        self.proxy.new_har(website, options={'captureHeaders': True,'captureContent':True,'captureBinaryContent':True})
        self.driver.get('http:\\'+website)
        
        result = json.dumps(self.proxy.har, indent=4, sort_keys=True,ensure_ascii=True)
        self.__store_into_file('har',website+'har', result,repetition)
        
        performance = json.dumps(self.driver.execute_script("return window.performance"), ensure_ascii=True,indent=4)
        self.__store_into_file('Performance',website+'Performance', performance,repetition)

    def stop_all(self):
        #stop server and driver
        from datetime import datetime
        print ("%s: Finish"%(datetime.now()))
        
        self.server.stop()
        self.driver.quit()


def generator(websites,repetition):
    browser = Browser('chrome')
    parser = argparse.ArgumentParser(description='Performance Testing using Browsermob-Proxy and Python')
    args = vars(parser.parse_args())
    #browsermob-proxy needed as well
    path = os.getenv('BROWSERMOB_PROXY_PATH', 'C:\\Users\ines\Desktop\\browsermob-proxy\\bin\\browsermob-proxy')
    #number of runs for each website
    for repetition in range (0,repetition):
        #precise which array to use here
        for website in websites:
            RUN = HARGenerator(path)
            RUN.start_all(args,website)
            RUN.create_har(args,website,repetition)
            RUN.stop_all()
#------------------------------------------------------------------------------------------------------------------------------
#HAR Parser
def parser(websites, repetition):
    for dom in websites:
        print('################################################################');
        print (dom)
        jssize=[];
        cssize=[];
        imagesize=[];
        videosize=[];
        pagesize=[];
        jsnum=[];
        csnum=[];
        imagenum=[];
        videonum=[];
        pagenum=[];
        for i in range (0,repetition):
            #General har files 
            string=str(i)+dom+ 'har.har'
            with open(string, 'r') as f:
                har_parser = HarPage(dom, har_data=json.loads(f.read()))

            #for each har file of the web site under review
            #print ("Image Load time: " + str(har_parser.image_load_time))
            #print ("Html Load time: " + str(har_parser.html_load_time))

            #combines all the diffrent har files generated for that secific web site and shows average/min/max
            #for the size of the diffrent files
            jssize.append(har_parser.js_size);
            cssize.append(har_parser.css_size);
            imagesize.append(har_parser.image_size);
            videosize.append(har_parser.video_size);
            pagesize.append(har_parser.page_size);

            #for the number of diffrent files
            jsnum.append(len(har_parser.filter_entries( content_type='js.*', status_code='2.*')));
            csnum.append(len(har_parser.filter_entries( content_type='css.*', status_code='2.*')));
            imagenum.append(len(har_parser.filter_entries( content_type='image.*', status_code='2.*')));
            videonum.append(len(har_parser.filter_entries( content_type='video.*', status_code='2.*')));
            pagenum.append(len(har_parser.filter_entries( status_code='2.*')));
            h=har_parser.filter_entries( content_type='text.*', status_code='2.*')


        print ("Max page size: " + str( max(pagesize)),end='\n');
        print ("Max js size: " + str(max(jssize)),end='\n');
        print ("Max css size: " + str(max(cssize)),end='\n');
        print ("Max image size: " + str(max(imagesize)),end='\n');
        print ("Max video size: " + str(max(videosize)),end='\n');

        print ("Max page number: " + str(max(pagenum)),end='\n');
        print ("Max js number: " + str(max(jsnum)),end='\n');
        print ("Max css number: " + str(max(csnum)),end='\n');
        print ("Max image number: " + str(max(imagenum)),end='\n');
        print ("Max video number: " + str(max(videonum)),end='\n');
        print('--------------------------------------------------------------------');

        print ("Min page size: " + str(min(pagesize)),end='\n');
        print ("Min js size: " + str(min(jssize)),end='\n');
        print ("Min css size: " + str(min(cssize)),end='\n');
        print ("Min image size: " + str(min(imagesize)),end='\n');
        print ("Min video size: " + str(min(videosize)),end='\n');

        print ("Min page number: " + str(min(pagenum)),end='\n');
        print ("Min js number: " + str(min(jsnum)),end='\n');
        print ("Min css number: " + str(min(csnum)),end='\n');
        print ("Min image number: " + str(min(imagenum)),end='\n');
        print ("Min video number: " + str(min(videonum)),end='\n');
        print('--------------------------------------------------------------------');
        print ("Average page size: " + str(mean(pagesize)),end='\n');
        print ("Average js size: " + str(mean(jssize)),end='\n');
        print ("Average css size: " + str(mean(cssize)),end='\n');
        print ("Average image size: " + str(mean(imagesize)),end='\n');
        print ("Average video size: " + str(mean(videosize)),end='\n');
        
        print ("Average page number: " + str(mean(pagenum)),end='\n');
        print ("Average js number: " + str(mean(jsnum)),end='\n');
        print ("Average css number: " + str(mean(csnum)),end='\n');
        print ("Average image number: " + str(mean(imagenum)),end='\n');
        print ("Average video number: " + str(mean(videonum)),end='\n');
        print('--------------------------------------------------------------------');

        #har files with delay specification
        string2=str(i)+dom+ 'Performance.har'
        with open(string2) as data_file:
            data = json.load(data_file)
        #All in milliseconds
        #Calculate the total time required to load a page
        print("Total time required to load the page: " + str(data["timing"]["loadEventEnd"]-data["timing"]["navigationStart"]))
        #Calculate request response times
        print("Request response times: " + str(data["timing"]["responseEnd"]-data["timing"]["requestStart"]))
        #connect start: represents the moment the request to open a connection is sent to the network
        #responce Start: represents the moment the browser received the first byte of the response
        print("Time to first byte: " + str (data["timing"]["responseStart"]-data["timing"]["connectStart"]))

#to allow outside calls
if __name__ == '__main__':
    a_game = HARGenerator('C:\\Users\ines\Desktop\\browsermob-proxy\\bin\\browsermob-proxy')
    
