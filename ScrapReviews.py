# COMPANY REVIEWS DATA:

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

# 1. OPENS 25 PAGES OF JOB POSTINGS AND GETS A LIST OF WEBLINKS OF COMPANY REVIEWS 
# 2. FEEDS WEBLINKS INTO A LOOP TO GET FULL REVIEW TEXTS FOR EACH OF THE 25 PAGES
# 3. SAVES REVIEW TEXTS ON HARD DRIVE IN A .TXT FILE

for p in range(0,24):  #defining number of pages to crawl - we do not want it to crawl ALL pages
    n = p

    base_url="https://www.indeed.com/jobs?q=data+scientist&explvl=entry_level&limit=%d"%(n+50)
    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, "html.parser")

    for div in soup.find_all(name="div", attrs={"data-tn-component":"organicJob"}):
        for h2 in div.find_all(name="h2", attrs={"class":"jobtitle"}):
            for a in h2.find_all(name = "a"):
                    
                links = "https://www.indeed.com%s"%a["href"] # list of individual links to each job page
                jobpage = requests.get(links) #opens each job page
                jobsoup = BeautifulSoup(jobpage.text, "html.parser") #parses each job page
                for div in jobsoup.find_all(name="div", attrs={"data-tn-component":"jobHeader"}):
                    for a in div.find_all(name="a"):# retrieves full job posts texts
                            
                        all_rev_urls = "https://www.indeed.com%s"%a["href"] #gets the links of reviews for each job
                        revpage = requests.get(all_rev_urls) #opens each review page
                        revsoup = BeautifulSoup(revpage.text, "html.parser") #parses review page
                        for span in revsoup.find_all(name="span", attrs={"class":"cmp-review-text"}):
                            with open('all_reviews.txt', 'a') as rt: #'a':append so that the file will not need overwritten everytime the loop starts
                                rev = span.text.strip()
                                reviews = rev.encode('utf-8')
                                rt.write(reviews)
