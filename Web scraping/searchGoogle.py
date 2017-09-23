from bs4 import BeautifulSoup
import re
import requests
import random
import sys
sys.path.insert(0,'../Utils')  # Add the path of files to be imported to the system path

from readFromFile import getDataFromText

def search_google():

    names = getDataFromText()        # Get the input names from the text

    # Browsers for searching
    agents = [
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
        'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7']

    # Randomly select browser from list
    u = random.randint(0, len(agents) - 1)

    # Assign headers
    headers = {'User-Agent': agents[u]}

    links = []
    # For each name in the list
    for name in names:

        query = name + ' ' + sys.argv[2]          # Get the name + another search term (e.g. Wikipedia)

        reg = re.compile(".*&sa=")                # Get a string to be searched
        query = query.strip().split()             # Split the query string into individual words
        query = "+".join(query)                   # Add a '+' between the split words
        url = "https://www.google.co.in/search?site=&source=hp&q=" + query + "&gws_rd=ssl"  # Get the URL to be searched. Works only for google

        response = requests.get(url, headers=headers)        #Get the html of the search page
        soup = BeautifulSoup(response.text, "lxml")          # Convert that into lxml format
        results = soup.find_all("h3", class_="r")            # From the lxml file get all the strings having 'h3'. This is the list of all web search links

        if len(results) > 0:                                 # If more than one result is present

           url = results[0].find_all('a', href=True)         # Gets the first link from the list
           temp = url[0]['href'][:]
           index = temp.index('http')
           # print "index", index
           url = url[0]['href'][index:]          # Trim till the 'index' location
           # print "url3", url
           # print"len url", len(url)
           temp= reg.match(url)
           if(temp != None):
               url = (reg.match(url)).group()    # delete the other trails
               url = url[:-4]                    # trim the last characters
               links.append(url)
        else:
               links.append(None)

    return links

if __name__=='__main__':
    link = search_google()
    print link