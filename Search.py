import sys
import json
import requests
import re
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Crawler():
    
    def retrieveHtmlPage(self, url):
        html = requests.get(url, timeout=5)
        try:
            if "http://newhaven.edu" in url:
                return html.content
        except Exception as e:
            print(e)
            return ""
        return html.content.decode('latin-1')

    def links(self, url):
        htmlPage = self.retrieveHtmlPage(url)
        parsed = urlparse(url)
        base = "http://newhaven.edu"
        soup = BeautifulSoup(base)
        links = []
        for link in soup.findAll('a'):
            print
            link.get('href')
            new_url = urljoin(base, link)
            self.queued.append(new_url)
            links.insert(link)


    def extract(self, url):
        if "http://newhaven.edu":
            html = requests.get(url,timeout=5).content
            return html

    def crawl(self, url):
        links = self.get_links(url)
        if link in self.get_links("http://newhaven.edu"):
            self.visited.add(link)
            try:
                print(link)
                info = self.extract_info(link)
                f_dict['url'] = link
                f_info = str(info)
                hdoc = fromstring(f_info)
                f_dict['keywords'] = N(hdoc.xpath("//meta[@name='Keywords']/@content"))
                f_dict['title'] = N(hdoc.xpath("//meta[@property='og:title']/@content"))
                f_dict['type'] = N(hdoc.xpath("//meta[@property='og:type']/@content"))
                f_dict['description'] = N(hdoc.xpath("//meta[@property='og:description']/@content")) 
                if not "newhaven.edu" in link:
                    self.get_links(link)
                else:
                    print(" Present")
                self.count += 1
            except Exception as e:
                print(e)
                print("Error")
        else:
            self.get_links(url)

    
if __name__ == "main":
    
    crawler = Crawler()
    crawler.crawl("http://newhaven.edu")
