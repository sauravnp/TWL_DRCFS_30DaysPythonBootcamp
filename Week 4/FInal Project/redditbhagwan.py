# import module
import requests
from bs4 import BeautifulSoup
Headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

def get_data(url):
    r = requests.get(url, headers = Headers )
    return r.content              
link = "https://www.reddit.com/r/Nepal/comments/zyx0ne/imagehattiban/"

html_data = get_data(link)
soup = BeautifulSoup(html_data, 'html.parser')

title = str(soup.find('h1', class_="_eYtD2XCVieq6emjKBH3m").get_text())
x = str(soup.find('span',{"class": "_19bCWnxeTjqzBElWZfIlJb"}).get_text())
sub_name = x.split("/")[1]
y  = str(soup.find('span',{"class": "FHCV02u6Cp2zYL0fhQPsO"}).get_text())
comments = y.split(" ")[0]
i = soup.find('a',{"class": "_3m20hIKOhTTeMgPnfMbVNN"})
image_link = i['href']
with open("redditgahana.csv", "w") as writer:
    writer.write("Image Link: " + image_link +  "\n")
    writer.write("No of comments: " + comments + "\n")
    writer.write("Title: " + title + "\n")
    writer.write("Name of SubReddit: " + sub_name + "\n")

