import re
import urllib.request
from urllib.parse import urljoin

from bs4 import BeautifulSoup

page_url = "http://www.shicimingju.com/chaxun/list/2973.html"
response = urllib.request.urlopen(page_url)
html_cont = response.read()

soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

links = soup.find_all('a', href=re.compile(r"/chaxun/list/\d+\.html"))
for link in links:
    new_url = link['href']
    new_full_url = urljoin(page_url, new_url)
    print("完整url路径：" + new_full_url)
