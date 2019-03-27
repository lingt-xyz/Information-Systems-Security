"""
Read domain name from website
"""
import requests
from bs4 import BeautifulSoup

class domain_loader:
    alexa_root = 'https://www.alexa.com/'

    def __init__(self):
        pass

    def get_top_domain_from_alexa(self, url=None):
        domains = []

        if url is None:
            url = self.alexa_root + '/topsites'
        
        #open with GET method 
        resp=requests.get(url) 
        
        #http_respone 200 means OK status 
        if resp.status_code==200: 
        
            # we need a parser,Python built-in HTML parser is enough . 
            soup=BeautifulSoup(resp.text,'html.parser')     
    
            # l is the list which contains all the text i.e news  
            l=soup.findAll("div",{"class":"td DescriptionCell"}) 
        
            #now we want to find only the text part of the anchor. 
            #find all the elements of a, i.e anchor 
            for i in l:
                c = i.find("a")
                domains.append(c.text)
        else: 
            print("Error") 
        
        return domains

    def get_category_top_domain_from_alexa(self):
        urls = []
        domains = []

        url='https://www.alexa.com/topsites/category'
        
        #open with GET method 
        resp=requests.get(url) 
        
        #http_respone 200 means OK status 
        if resp.status_code==200: 
        
            # we need a parser,Python built-in HTML parser is enough . 
            soup=BeautifulSoup(resp.text,'html.parser')     
    
            # l is the list which contains all the text i.e news  
            l=soup.findAll("ul",{"class":"subcategories span3"}) 
        
            #now we want to print only the text part of the anchor. 
            #find all the elements of a, i.e anchor 
            for i in l:
                li = i.findAll("a")
                for a in li:
                    urls.append(self.alexa_root + a.get('href'))
            
            for h in urls:
                category_domains = self.get_top_domain_from_alexa(h)
                domains.extend(category_domains)
        else: 
            print("Error") 
        
        return domains

    def get_block_domain_from_wiki(self):
        pass
