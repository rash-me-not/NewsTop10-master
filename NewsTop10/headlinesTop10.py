import requests, pandas
from bs4 import BeautifulSoup

r = requests.get("http://www.reuters.com/news/archive/topNews")
c= r.content

soup = BeautifulSoup(c, "html.parser")

stories = soup.find_all("div",{"class":"story-content"})
storylist = []
for story, i in zip(stories,range(10)):
    newsdict = {}
    newsdict["Headline"]= story.find("h3",{"class":"story-title"}).text.strip()
    newsdict["StoryText"]= story.find("p").text.strip()
    newsdict["Full Artice"]= "http://www.reuters.com/"+story.find("h3",{"class":"story-title"}).find("a").attrs["href"]
    newsdict["Time"]= story.find("time").text.strip()
    storylist.append(newsdict)
df = pandas.DataFrame(storylist)
df.to_csv("Headlines.csv")
