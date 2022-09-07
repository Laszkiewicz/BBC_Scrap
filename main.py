from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.bbc.com/news/world-60525350")

bbc_web_page = response.text

soup = BeautifulSoup(bbc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_time_posted = [time.getText() for time in soup.find_all(name="span", class_="gs-c-timestamp gs-o-bullet gs-o-bullet- nw-c-timestamp")]

print(article_texts)
print(article_links)
print(article_time_posted)