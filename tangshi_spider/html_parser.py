# html解析器
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # http://www.shicimingju.com/chaxun/list/2973.html
        links = soup.find_all('a', href=re.compile(r"/chaxun/list/\d+\.html"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # 标题
        title_node = soup.find('div', id="item_div").find('h1')
        res_data['title'] = title_node.get_text()
        # 作者年代
        author = soup.find("div", class_="niandai_zuozhe")
        res_data['author'] = author.get_text()
        # 内容
        summary_node = soup.find('div', class_="item_content")
        res_data['summary'] = summary_node.get_text()

        return res_data
