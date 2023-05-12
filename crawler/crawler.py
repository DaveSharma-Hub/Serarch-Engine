import requests
from bs4 import BeautifulSoup

class URLClass:
    def __init__(self, url, title):
        self.url = url
        self.title = title

# class Object:
#     def add(self,key,value):
#         self[key] = value
#     def get(self,key):
#         val = self[key]
#         return val

def web_scrape(URL):
    page = requests.get(URL).text
    soup = BeautifulSoup(page,"lxml")

    linkList = []
    for links in soup.findAll("a"):
        link_url = links.get("href")
        link_title = links.get("title")
        urlObj = URLClass(link_url,link_title)
        linkList.append(urlObj)
    return linkList

def read_and_append_url():
    read_file = open("urlList.txt","r")
    append_file = open("urlList.txt","a")
    for url in read_file:
        linkList = web_scrape(url)
        for links in linkList:
            append_file.write(links)
    read_file.close()
    append_file.close()

print(web_scrape("https://www.tutorialspoint.com/jqueryui/jqueryui_draggable.htm"))