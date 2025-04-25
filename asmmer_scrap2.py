import csv
import requests
from bs4 import BeautifulSoup
url="https://www.thriftbooks.com/b/education-and-reference/"
with open("bookdetails2.csv","w") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["title","author","price"])
    response=requests.get(url).content
#print(response.status_code)
    soup=BeautifulSoup(response,"lxml")
    blocks=soup.find_all("div",class_="LandingPage-slideBookCardContainer")
    cells=soup.find_all("div",class_="LandingPage-slideBookCardContainer")
    for block in blocks:
        title=block.find("div",class_="LandingPage-bookCardTitle").text
    #print(title)
        author=block.find("div",class_="LandingPage-bookCardAuthor").text
    #print(author)
        price=block.find("p",class_="BookSlider-price").find("strong").text
        #print(price)
        csv_writer.writerow([title,author,price])