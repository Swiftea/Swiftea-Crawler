#!/usr/bin/env python3

import atexit
from urllib.parse import urlparse
import json


import click


from crawler.swiftea_bot import module
from crawler.crawler_base import Crawler
from crawler.crawler_domain import CrawlerDomain

def save(crawler):
	crawler.file_manager.save_inverted_index(
		crawler.index_manager.get_inverted_index()
	)

@click.command()
@click.option('-u', '--url')  # initial url
@click.option('-sd', '--sub-domain', default=True)  # True or False
@click.option('-l', '--level', default=0)
@click.option('-tl', '--target-level', default=1)
@click.option('-um', '--use-mongodb', default=False)
@click.option('-l1', '--loop-1', default=50)
@click.option('-l2', '--loop-2', default=10)
def main(url, sub_domain, level, target_level, use_mongodb, loop_1, loop_2):
	with open('crawler-config.json') as json_file:
		config = json.load(json_file)
	module.create_dirs(config['DIR_DATA'])
	if url:
		crawl_option = dict()
		crawl_option['domain'] = urlparse(url).netloc
		crawl_option['sub-domain'] = sub_domain
		crawl_option['level'] = level
		crawl_option['target-level'] = target_level
		crawl_option['use-mongodb'] = use_mongodb
		crawler = CrawlerDomain(crawl_option, url)
	else:
		crawler = Crawler(loop_1, loop_2)
		print('Starting with base urls')
		module.def_links()
		atexit.register(save, crawler)
	crawler.start()


if __name__ == '__main__':
	main()
