import requests
from bs4 import BeautifulSoup

url = "http://tv.niazitv.pk"
# Step 1: Get the HTML
# :- r = content of web site

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the Html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML tree travarsel
#
#
# Commonly used types of objects:
# 1: Tag
# 2: Navigable String
# 3: BeautifulSoup object
# 4: Comment

# Get the title
title = soup.title
# print(title)

# Get all the paragraphs
paras = soup.find_all('p')
# print(paras)

# Get all the anchor tags
anchors = soup.find_all('a')
all_links = set()
# Get all the links in the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "http://tv.niazitv.pk" + link.get('href')
        all_links.add(linkText)
        # print(linkText)
# print(anchors)

# Get first element of html page
# print(soup.find('p'))

# Get classes of any element of html page
# print(soup.find('p')['class'])

# Find all element with class Lead
# print(soup.find_all('p', class_='lead'))

# Get the text from the Elements i.e tags/soup
# print(soup.find('p').get_text())
# For all text in htm page(soup)
# print(soup.get_text())


navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)

# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents:
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
elem = soup.select('#loginModal')[0]
# print(elem)


