# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:44:58 2016

@author: dweiss89
"""
import urllib2
from bs4 import BeautifulSoup
import re
from sys import argv
import math

script, first, second = argv

print first
# get links to all articles into a list
urlBase = "http://www.vox.com/authors/" + first + "/archives/"
# urlBase = "http://www.vox.com/authors/Joseph-Stromberg/archives/"

url = urllib2.urlopen(urlBase + "1")
soup = BeautifulSoup(url)

pageCount = soup.find("span", {"class": "m-pagination__count"}).text
pageCount = int(math.ceil(int(pageCount.replace("Showing 1 - 5 of ", ""))/5.0))

nums = range(1, pageCount + 1)
articleLink = re.compile(r"http://www.vox.com/\d{4}")

articles = []
for num in nums:
    print num
    url = urllib2.urlopen(urlBase + str(num))
    soup = BeautifulSoup(url)
    links = soup.find_all('a', href=True)
    for link in links:
        if articleLink.search(link.get('href')) != None \
                and link.get('href') not in articles:
            articles.append(link.get('href'))

# get text from articles and write them to a text file

for val, link in enumerate(articles):
    print val
    url = link
    soup = BeautifulSoup(urllib2.urlopen(url).read())

    if soup.find("h1") != None:
        title = soup.find('h1').get_text()
    else:
        title = soup.find('h2').get_text()
    title = title.encode('utf-8')
    name = "article" + str(val)
    with open('Vox Scrape/' + second +
            "/" + name + '.txt', 'w') as f:
        # with open('Stromberg/' + name + '.txt', 'w') as f:
        f.write(title + '\n')
        for tag in soup.find_all('p'):
            if tag.text.encode('utf-8') != "Awesome, share it:":
                f.write(tag.text.encode('utf-8') + '\n')
            else:
                break
