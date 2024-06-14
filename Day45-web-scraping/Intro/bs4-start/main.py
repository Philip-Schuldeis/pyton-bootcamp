from bs4 import BeautifulSoup

# with open("website.html", encoding="utf-8") as file:
#   contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)

# print(soup.title.string)

# print(soup.prettify())

# print(soup.p) # just gives the first paragraph

#How to get all paragraphs

# all_paragraphs = soup.find_all("p")
# # print(all_paragraphs)
#
# for tag in all_paragraphs:
#    print(tag.getText())
#
# # How do i handle hrefs
#
# all_anchor_tags = soup.find_all("a")
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# # search for id
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))
#
# conpany_url = soup.select_one(selector="p a")
# print(conpany_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# # Select all class with h1
#
# headings = soup.select(".heading")
# print(headings)

# Thanks to Charlie for this code
# https://www.udemy.com/course/100-days-of-code/learn/#questions/19476080


# Callange
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

print(soup.title.getText()) #getting the title of the website
article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):  # td with the class subtext is where the score is located
    if article.span.find(class_="score") is None: #finding the score class in that td and append it if 0
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0])) # if not split to get rid of the text (layout= 238 points) so i can order it by the upvote value

max_points_index = article_upvotes.index(max(article_upvotes)) # finding the article with the most upvotes
print(
    f"{article_titles[max_points_index]},\n "
    f"{article_upvotes[max_points_index]} points,\n "
    f"available at: {article_links[max_points_index]}."
)

# for legal reasons check the robots.txt: https://news.ycombinator.com/robots.txt or check if api is available if so rather use the api
# BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/