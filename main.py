import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = '/home/clem/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/clem/.config/google-chrome")
options.add_argument('--no-sandbox')

try:
    browser = webdriver.Chrome(chromedriver, options=options)
except Exception as e:
    print(f'No found chromedriver in this environment.')
    print(f'Install on your machine. exception: {e}')
    sys.exit()

#
browser.set_window_size(1280, 1024)
time.sleep(4)
browser.get('https://www.instagram.com/username/')
time.sleep(4)
html = browser.page_source
soup = BeautifulSoup(html, features="html.parser")
posts = soup.select_one("meta[property='og:description']").get("content").split()[4]
start = int(posts)

print(f'posts at start up: {posts}')print('now waiting...')

# waits for a new post
while (int(posts)) == start:
    browser.get('https://www.instagram.com/username/')
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")
    posts = soup.select_one("meta[property='og:description']").get("content").split()[4]
    if (int(posts)) != start:
        print('{} {}'.format(posts, start))
    time.sleep(1.5)
print('hes posted')

# finds the most recent post made
first = soup.find_all("div", class_="v1Nh3 kIKUG _bz0w")[0].find_all("a")[0].get("href")
checkbool = browser.get('https://www.instagram.com'+first)
html = browser.page_source
soup = BeautifulSoup(html, features="html.parser")

# places the comment
commentArea = browser.find_element_by_class_name('Ypffh')
commentArea.click()
commentArea = browser.find_element_by_class_name('Ypffh')
commentArea.send_keys("ME!!")
commentArea.send_keys(Keys.ENTER)

time.sleep(5)
