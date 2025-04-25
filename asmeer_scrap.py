import csv
import requests
from bs4 import BeautifulSoup
with open("bookdetail.csv","a") as f:
    csv_writer=csv.writer(f)
    url="https://www.thriftbooks.com/b/biographies-and-memoirs/"
    response=requests.get(url).content
    soup=BeautifulSoup(response,"lxml")
    blocks=soup.find_all("a",class_="LandingPage-bookCard")
    for block in blocks:
        title=block.find("div",class_="LandingPage-bookCardTitle").text
        author=block.find("div",class_="LandingPage-bookCardAuthor").text
        price=block.find("p",class_="BookSlider-price").find("strong").text
        csv_writer.writerow([title,author,price])
        print(price,author)