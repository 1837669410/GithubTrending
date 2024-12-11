import json

import requests
from fake_useragent import UserAgent
from lxml import etree


class GithubTrending:

    def __init__(self):

        self.base_url = 'https://github.com/trending'
        self.headers = {
            'User-Agent': UserAgent().random,
        }
        self.trend_information = {}

    def collect(self, language, date='daily'):
        url = f'{self.base_url}/{language}?since={date}'

        response = requests.get(url, self.headers).text

        tree = etree.HTML(response)
        project_list = tree.xpath('//div[@class="Box"]/div[2]/article')
        for project in project_list:
            project_name = project.xpath('./h2/a/text()')[1].strip()
            project_desc = project.xpath('./p/text()')[0].strip()
            project_info = {
                'language': language,
                'stars_num': project.xpath('./div[2]/a[1]/text()')[0].strip(),
                'forks_num': project.xpath('./div[2]/a[2]/text()')[0].strip(),
                'today_stars_num': project.xpath('./div[2]/span[3]/text()')[1].strip()
            }
            self.trend_information[project_name] = {
                'desc': project_desc,
                'info': project_info
            }

        with open(f'./{language}_GithubTrending.json', 'w', encoding='utf-8') as f:
            json.dump(self.trend_information, f, ensure_ascii=False, indent=4)

    def batch_collect(self, language_list, date='daily'):
        for language in language_list:
            self.collect(language, date)
            # clean self.trend_information
            self.trend_information = {}


if __name__ == '__main__':

    gt = GithubTrending()

    # gt.collect('Go', 'daily')
    gt.batch_collect(language_list=['C++', 'java', 'python'])