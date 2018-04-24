# INTERVIEW QUESTIONS/DATA: Another method to get data with bs4:
# USEFUL WHEN SCRAPPING VARIOUS WEB PAGES FROM DIFFERENT WEBSITES (DIFFERENT PAGE STRUCTURES)

# 1. INPUT IS A CSV FILE WITH ONE WEBLINK PER ROW
# 2. FUNCTION DETECTs TAGS COMMON TO ALL PAGES 
# 3. CODE OPENs THE WEBPAGE OF EACH WEBLINK AND FILTERS OUT TAGS FROM 2.

from bs4.element import Comment
import urllib

int_links= pd.read_csv("C:\\Users\\Aymone\\Desktop\\int_links.csv")  # input file

def spot_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


for l in int_links:
    for rowid in range(len(int_links)):
        try:
            n = rowid
            link = str(int_links.iloc[n,1])
            datapage = requests.get(link)
            datasoup = BeautifulSoup(datapage.text, "html.parser")
            text = datasoup.find_all(text=True)
            visible_texts = filter(spot_visible, text)
            with open("Interview_Questions.txt", "a") as d:
                d.write(str(visible_texts))
                
        except BaseException, e:
            n= n+1
            link = str(int_links.iloc[n, 1])
            datapage = requests.get(link)
            datasoup = BeautifulSoup(datapage.text, "html.parser")
            text = datasoup.find_all(text=True)
            visible_texts = filter(spot_visible, text)

            with open("Interview_Questions.txt", "a") as d:
                d.write(visible_texts))

        except requests.exceptions.SSLError, e1:
            n= n+1
            link = str(int_links.iloc[n, 1])
            datapage = requests.get(link)
            datasoup = BeautifulSoup(datapage.text, "html.parser")
            text = datasoup.find_all(text=True)
            visible_texts = filter(spot_visible, text)

            with open("Interview_Questions.txt", "a") as d:
                d.write(str(visible_texts))
