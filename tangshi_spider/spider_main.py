import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self): # 123
        self.urls = url_manager.UrlManager()    # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # url下载器
        self.parser = html_parser.HtmlParser()    # url解析器
        self.outputer = html_outputer.HtmlOutputer()   # 输出器

    def craw(self, root_url):  # 爬虫调度程序
        count = 1
        self.urls.add_new_url(root_url)  # 把入口url添加进url管理器
        while self.urls.has_new_url():  # 启动爬虫循环
            # noinspection PyBroadException
            try:
                new_url = self.urls.get_new_url()  # 获取一个待爬取的url
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)  # 启动下载器下载页面存储在html_cont中
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 调用解析器解析数据，得到新的url列表和新的数据
                self.urls.add_new_urls(new_urls)  # 新的url继续添加到url管理器（批量的添加）
                self.outputer.collect_data(new_data)  # 收集数据
                if count == 10:
                    break
                count = count + 1
            except:
                print('craw faild')

        self.outputer.output_html()


if __name__ == "__main__":
    # 入口url
    root_url = "http://www.shicimingju.com/chaxun/list/2973.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
