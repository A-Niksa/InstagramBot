# cloned from: https://github.com/Ninkuk/Instagram-Caption-Scraper/blob/master/CaptionSearch.py
# with chunks from: https://realpython.com/instagram-bot-python-instapy/
# edited a tad bit
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

# takes user input of username and string to search
def get_user_requirements():
    url = 'https://www.instagram.com/'
    username = input("Enter the username you wish to scrape:")
    url += str(username)
    get_links(url)


# scrolls through the user page and gathers all the posts' links
def get_links(url):
    links = []
    browser = webdriver.Firefox()

    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')
    login_link = browser.find_element_by_xpath("//a[text()='Log in']")
    login_link.click()
    time.sleep(2)
    username_input = browser.find_element("input[name='username']")
    password_input = browser.find_element("input[name='password']")
    username_input.send_keys("mft.project.nka")
    password_input.send_keys("23571113")
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    time.sleep(5)

    browser.get(url)
    last_height = browser.execute_script("return document.body.scrollHeight")

        
    while True:
        source = browser.page_source
        data = BeautifulSoup(source, 'html.parser')
        body = data.find('body')
        script = body.find('span')

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            script.findAll('a')
        except:
            print("Sorry! An unexpected error occurred. Please make sure you enter a valid username")
            break

        for link in script.findAll('a'):
            if re.match("/p", link.get('href')):
                to_add = 'https://www.instagram.com' + link.get('href')
                if to_add not in links:
                    links.append(to_add)

        time.sleep(3)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    print(len(links), "posts found")
    browser.close()
    filter_captions(links)


# this searches the string in the caption of all the posts
def filter_captions(links):
    filtered_links = []
    browser = webdriver.Firefox()
    for link in links:
        browser.get(link)
        source = browser.page_source
        data = BeautifulSoup(source, 'html.parser')
        for text in data.findAll('span'):
            if link not in filtered_links:
                filtered_links.append(link)

    print(len(filtered_links), 'results founds')
    browser.close()
    write_to_file(filtered_links)


# finally this stores the resulting links in a txt file
def write_to_file(filtered_links):
    file_name = "captions"
    with open(f"{file_name}.txt", 'w') as f:
        for item in filtered_links:
            f.write("%s\n" % item)


# Main method
if __name__ == '__main__':
    get_user_requirements()