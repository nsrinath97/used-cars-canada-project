from selenium_driver import get_driver
import time
from bs4 import BeautifulSoup as bs
import math
import re


def get_page(url):
    """Get the html document for a page"""

    driver = get_driver()
    driver.get(url)                             # Connect to the url and grab the page
    time.sleep(3)                               # delay so the page can load
    page_html = driver.page_source              # Grab the HTML
    bs4_doc = bs(page_html, 'html.parser')      # Parse the HTML
    return bs4_doc



def get_posts(url, page='0'):
    """Get an individual link for each car ad posted on the day"""

    url = url + page            # Get the first page 
    bs4_doc = get_page(url)

    posts = bs4_doc.find_all('a', class_='titlestring')     # Find all posts on the page
    if not posts:                                           # If there are no posts, return none for now
                                                            # TODO find another way to deal with having no posts on the day
        return
    
    # Create a list of all the post links
    posts_list = []
    for post in posts:
        link = post.get('href')
        posts_list.append(link)


    num_posts = bs4_doc.find('span', class_='cl-page-number').text                              # Total number of posts
    num_pages = math.ceil(int(''.join(re.findall(r'\d+', num_posts.split(' ')[-1]))) / 120)     # Total number of pages
    if num_pages > 1:
        for i in range(1, num_pages):                               # For looping through all the pages
            page = i
            url = url[:-3] + page + url[-2:] 
            bs4_doc = get_page(url)
            posts = bs4_doc.find_all('a', class_='titlestring')
            
            for post in posts:
                link = post.get('href')
                posts_list.append(link)
    else:
        return posts_list

    return posts_list



def scrape_post(url):
    """Scrape each individual ad for vehicle details"""

    bs4_doc = get_page(url)
    
    attrs = bs4_doc.find_all('p', class_='attrgroup')
    desc = bs4_doc.find('section', id='postingbody')
    
    title = attrs[0].text.split('\n')
    title = [i for i in title if i.strip()]
    title = ''.join(["Vehicle Name: "] + title)

    attrs_list = attrs[1].text.split('\n')
    attrs_list = [i for i in attrs_list if i.strip()]
    post_description = desc.text.replace('\n', ' ')

    posting_details = title + attrs_list + [url] + [post_description]

    keys = []
    values = []
    for attr in posting_details:
        attr = attr.split(':')
        keys.append(attr[0])
        values.append(attr[1])
    
    details_dict = dict(zip(keys, values))
        
    return details_dict