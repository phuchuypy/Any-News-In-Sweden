from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
import webbrowser

news_source = "https://www.thelocal.se/category/sweden-news/"
file_name = "news_titles.txt"

def main():
    news_titles = get_news_titles(news_source)
    if os.path.isfile("./" + file_name):
        new_titles, urls = compare_news_titles(news_titles,file_name)
        for title in new_titles:
            print(title)
        for url in urls:
            webbrowser.open(url)
    #save_news_titles_to_file(news_titles)

def get_news_titles(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    page_soup = BeautifulSoup(webpage, "html.parser")
    # TODO: change the below attribute(s) depending on different news sources
    # The purpose here is to get all of the titles of the articles
    news_links = page_soup.findAll("a",attrs={"class":"article-link-event"})

    # Get rid of new line character (/n) in the elements
    titles = []
    urls = []
    for index in range(len(news_links)):
        url = news_links[index].get("href")
        title = news_links[index].text.replace("\n","")
        if title.strip() != "": # Only append non-empty elements
            titles.append(title.strip())
            urls.append(url)
    return titles, urls

def save_news_titles_to_file(titles):
    file = open(file_name,"w")
    for index in range(len(titles)):
        if index == len(titles) - 1:
            file.write(f"{titles[index]}")
        else:
            file.write(f"{titles[index]},")
    file.close()

def compare_news_titles(today_titles,file):
    new_titles = []
    yesterday_titles = open(file, "r").read()
    yesterday_titles = yesterday_titles.split(",")
    for index in range(len(today_titles)):
        if today_titles[index] not in yesterday_titles:
            new_titles.append(today_titles[index])
    return new_titles
    
main()