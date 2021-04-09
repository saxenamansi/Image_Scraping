# TASK 1: Read a webpage and store the HTML content

import shutil
import tempfile
import urllib.request

url = 'https://en.wikipedia.org/wiki/Main_Page'
with urllib.request.urlopen(url) as response:
   html = response.read()

file = open("content.html","wb")
file.write(html)
file.close()

# TASK 2: Extract image urls from imgage tags in the HTML content

from bs4 import BeautifulSoup
import csv
soup = BeautifulSoup(open("content.html",  encoding="utf8"), features = 'lxml')

final_link = soup.a
final_link.decompose()

f = csv.writer(open("content.csv", "w"))
f.writerow(["Name", "Link"])
links = soup.find_all("img")
# print(links[0])
for index, link in enumerate(links):
    name = "image_" + str(index)
    Link = "http://" + link.get("src")
    f.writerow([name, Link])

# TASK 3: Download the images extracted from urls in the image tags

import pandas as pd 
df = pd.read_csv('content.csv')
import requests, os
shutil.rmtree("images")
os.mkdir("images")
for index, link in enumerate(df['Link']):
    response = requests.get(link)
    name = str(index) + ".png"
    path = "images/" + name
    file = open(path, "wb")
    file.write(response.content)
    file.close()
