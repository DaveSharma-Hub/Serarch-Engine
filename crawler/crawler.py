import requests
from bs4 import BeautifulSoup
import numpy as np

class URLClass:
    def __init__(self, url, title):
        self.url = url
        self.title = title

    def getUrl(self):
        return self.url

    def getTitle(self):
        return self.title
# class Object:
#     def add(self,key,value):
#         self[key] = value
#     def get(self,key):
#         val = self[key]
#         return val

def web_scrape(URL):
    page = requests.get(URL).text
    soup = BeautifulSoup(page,"html.parser")

    linkList = []
    for links in soup.findAll("a"):
        link_url = links.get("href")
        link_title = links.get("title")
        urlObj = URLClass(link_url,link_title)
        linkList.append(urlObj)
    return linkList

def read_and_append_url_from_file():
    read_file = open("urlList.txt","r")
    append_file = open("urlList.txt","a")
    for url in read_file:
        linkList = web_scrape(url)
        for links in linkList:
            append_file.write(links.getUrl())
    read_file.close()
    append_file.close()

def getNewData(new, old):
    arr = np.array(new)
    return arr[len(old):]

def read_and_append_url_from_databse():
    req = requests.get("http://localhost:3000/getUrlList")
    urlList = req.json()
    urlsStillLeft = True
    while urlsStillLeft:
        for urls in urlList:
            linkList = web_scrape(urls["url"])
            for links in linkList:
                linkData = {"url":links.getUrl(), "title":links.getTitle()}
                requests.post("http://localhost:3000/addUrl", json=linkData)
        urlList2 = requests.get("http://localhost:3000/getUrlList").json()
        if(len(urlList2) == len(urlList)):
            urlsStillLeft = False
        else:
            urlList = getNewData(urlList2,urlList)

if __name__ == "main":
    read_and_append_url_from_databse()