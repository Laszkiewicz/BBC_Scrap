from bs4 import BeautifulSoup
import requests
import re
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

# article_time_posted = [time.getText().split('h')[0] for time in soup.find_all(name="span", class_="gs-c-timestamp gs-o-bullet gs-o-bullet- nw-c-timestamp")]
article_time_posted = [time.getText().split('h')[0] for time in soup.find_all(name="span", class_="gs-c-timestamp gs-o-bullet gs-o-bullet- nw-c-timestamp")]
print(article_texts)
print(article_links)


article_time_posted = article_time_posted[2:-2]

oldest_posted = max(article_time_posted)
newest_posted = min(article_time_posted)
new = article_time_posted.index(oldest_posted)
new2 = article_time_posted.index(newest_posted)
print(article_texts[new])
print(article_texts[new2])
