import requests, pandas
from bs4 import BeautifulSoup

r = requests.get("https://news.ycombinator.com/newest")
c= r.content
soup = BeautifulSoup(c, "html.parser")

stories = soup.find_all("a",{"class":"storylink"})
storiesFrom = soup.find_all("span",{"class":"sitebit comhead"})
storylist = []
for i in range(10):
    newsdict = {}
    newsdict["Headline"]= stories[i].text
    newsdict["Source"]= storiesFrom[i].text
    if "http" not in stories[i].attrs['href']:
        newsdict["Url"]= "https://news.ycombinator.com/"+stories[i].attrs['href']
    else:
        newsdict["Url"]= stories[i].attrs['href']
    storylist.append(newsdict)

df = pandas.DataFrame(storylist)
df.to_csv("TechTop10.csv")
