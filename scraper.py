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
    driver.quit()
    return bs4_doc



def get_posts(url):
    """Get an individual link for each car ad posted on the day"""
 
    bs4_doc = get_page(url)

    posts = bs4_doc.find_all('a', class_='cl-app-anchor text-only posting-title')     # Find all posts on the page
    if not posts:                                           # If there are no posts, return none for now
                                                            # TODO find another way to deal with having no posts on the day
        return
    
    # Create a list of all the post links
    posts_list = []
    for post in posts:
        posts_list.append(post.get('href'))

    num_posts = bs4_doc.find('span', class_='cl-page-number').text                              # Total number of posts
    num_pages = math.ceil(int(''.join(re.findall(r'\d+', num_posts.split(' ')[-1]))) / 120)     # Total number of pages
    if num_pages > 1:
        for i in range(1, num_pages):                               # For looping through all the pages
            page = i
            url = url[:-3] + page + url[-2:] 
            bs4_doc = get_page(url)
            posts = bs4_doc.find_all('a', class_='cl-app-anchor text-only posting-title')
            
            for post in posts:
                link = post.get('href')
                posts_list.append(link)
    else:
        return posts_list

    return posts_list



def scrape_post(url):
    """Scrape each individual ad for vehicle details"""

    bs4_doc = get_page(url)
    
    attrs = bs4_doc.find_all('p', class_='attrgroup')           # Grab all the vehicle attributes in the post

    vehicle_name = attrs[0].text.split('\n')                           # vehicle name    
    vehicle_name = [i for i in vehicle_name if i.strip()]
    vehicle_name = [''.join(["Vehicle Name: "] + vehicle_name)]

    price = bs4_doc.find('span', class_='price')                # vehicle price
    vehicle_price = ['vehicle price: ' + price.text]

    posting_location = price.find_next_siblings()
    posting_location = ['city: ' + posting_location[0].text[2:-5]]

    attrs_list = attrs[1].text.split('\n')                      # Other attributes (cylinders, size, color etc.)    
    attrs_list = [i for i in attrs_list if i.strip()]
    attrs_list = ['delivery: available' if i == 'delivery available' else i for i in attrs_list]   # if delivery is available, then replace the phrase with something easier to put in dict
    attrs_list = ['cryptocurrency: ok' if i == 'cryptocurrency ok' else i for i in attrs_list]     # same as above but cryptocurrency
    attrs_list = ['odometer: broken' if i == 'odometer broken' else i for i in attrs_list]
    attrs_list = ['odometer: rolled over' if i == 'odometer rolled over' else i for i in attrs_list]

    posting_url = ['post link: ' + url]                          # link to the craigslist post

    desc = bs4_doc.find('section', id='postingbody')            # body of the craigslist post
    post_description = desc.text.replace('\n', ' ')
    post_description = ['description: ' + post_description]

    posting_details = vehicle_name + vehicle_price + posting_location + attrs_list + posting_url + post_description    # Put it all together in one list

    keys = []
    values = []
    for attr in posting_details:                    # Convert that list into a dictionary
        attr = attr.split(': ', 1)
        keys.append(attr[0])
        values.append(attr[1])
    
    details_dict = dict(zip(keys, values))
        
    return details_dict