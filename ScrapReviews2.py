# REVIEWS DATA PER COMPANY, AS WELL AS AVERAGE RATINGS AND CATEGORIZED RATINGS:
import csv

# 1. OPENS 25 PAGES OF JOB POSTINGS
# 2. GETS A LIST OF WEBLINKS OF COMPANY REVIEWS 
# 2. OPENS EACH OF THE 25 PAGES OF REVIEWS
# 3. GETS COMPANY NAME, AVERAGE RATING, CATEGORIZED RATINGS AND REVIEW TEXT FOR EACH COMPANY ON ALL 25 PAGES
# 4. SAVES DATA IN A CSV FILE WHERE EACH ROW IS DATA ABOUT ONLY ONE COMPANY

for p in range(0,24):
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
                       # for div in revsoup.find_all(name="div", attrs={"id":"cmp-name-and-rating"}):
                        name = revsoup.find_all(name="div", attrs={"class":"cmp-company-name"})
                        average_rating = revsoup.find_all(name="span", attrs={"itemprop":"ratingValue"})
                        rating_per_cat = revsoup.find_all(name="span", attrs={"class":"cmp-ReviewCategories-rating"})
                        review_text= revsoup.find_all(name="span", attrs={"class":"cmp-review-text"})


                        for n in name:
                            try:
                                rowid = name.index(n)
                            
                                c_name = n.text.strip().encode('utf-8') #text.strip().encode('utf-8') removes tags attached and
                                                                     # avoids encoding error messages
                                
                                av_rating = average_rating[rowid].text.strip().encode('utf-8')
                                rev_text = review_text [rowid].text.strip().encode('utf-8')

                                WorkLife_Balance = rating_per_cat[rowid:rowid+5][0].text.strip().encode('utf-8')
                                Compensation_Benefits = rating_per_cat[rowid:rowid+5][1].text.strip().encode('utf-8')
                                JobSecurity_Advancement = rating_per_cat[rowid:rowid+5][2].text.strip().encode('utf-8')
                                Management = rating_per_cat[rowid:rowid+5][3].text.strip().encode('utf-8')
                                Culture = rating_per_cat[rowid:rowid+5][4].text.strip().encode('utf-8')
                            
                                lists = [c_name ,av_rating, WorkLife_Balance, Compensation_Benefits, JobSecurity_Advancement,
                                    Management, Culture, rev_text]
                            
                                with open ('reviews_data.csv','a') as f:  #reopens same file with headers, and 'appends' new rows
                                    writerd = csv.writer(f)
                                    writerd.writerow(lists)
                                    
                            except:
                                try: 
                                    rowid = name.index(n+1) # skips to next company if there is an eception error

                                    c_name = n.text.strip().encode('utf-8') 

                                    av_rating = average_rating[rowid].text.strip().encode('utf-8')
                                    rev_text = review_text [rowid].text.strip().encode('utf-8')

                                    WorkLife_Balance = rating_per_cat[rowid:rowid+5][0].text.strip().encode('utf-8')
                                    Compensation_Benefits = rating_per_cat[rowid:rowid+5][1].text.strip().encode('utf-8')
                                    JobSecurity_Advancement = rating_per_cat[rowid:rowid+5][2].text.strip().encode('utf-8')
                                    Management = rating_per_cat[rowid:rowid+5][3].text.strip().encode('utf-8')
                                    Culture = rating_per_cat[rowid:rowid+5][4].text.strip().encode('utf-8')

                                    lists = [c_name ,av_rating, WorkLife_Balance, Compensation_Benefits, JobSecurity_Advancement,
                                        Management, Culture, rev_text]

                                    with open ('reviews_data.csv','a') as f:  
                                        writerd = csv.writer(f)
                                        writerd.writerow(lists)
                                        
                                except Exception, e:
                                    print e
