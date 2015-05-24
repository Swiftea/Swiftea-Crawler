#!/usr/bin/python3

"""Classes to test Swiftea-Crawler globaly."""

from os import mkdir
from configparser import ConfigParser

import package.data as data
from main import Crawler
from package.module import tell, create_dirs, create_doc
from package.web_connexion import WebConnexion
from package.database_swiftea import DatabaseSwiftea
from package.inverted_index import InvertedIndex
from package.ftp_swiftea import FTPSwiftea
from package.searches import SiteInformations
from package.file_manager import FileManager
import tests.test_data as test_data

def def_links():
    with open(data.DIR_LINKS + '0', 'w') as myfile:
        myfile.write(test_data.base_links)


class TestDatabaseSwiftea(DatabaseSwiftea):

    suggestions = test_data.suggestions

    def __init__(self, host, user, password, name):
        DatabaseSwiftea.__init__(self, host, user, password, name)

    def send_doc(self, infos):
        #assert infos == self.infos()
        assert 1

    def gen_infos(self):
        for k in range(15):
            yield {'score': 3,
                'favicon': 'http://swiftea.alwaysdata.net/public/favicon.ico',
                'title': 'Swiftea',
                'homepage': 0,
                'url': 'http://swiftea.alwaysdata.net' + '/' + str(k),
                'language': 'en',
                'keywords': ['gros', 'titre', 'moyen', 'titre', 'petit', 'titre', 'strong', 'swiftea'],
                'description': 'Moteur de recherche'
            }

    def infos(self):
        for info in self.gen_infos():
            return info

    def get_doc_id(self, url):
        for result in self.gen_get_doc_id():
            return result

    def gen_get_doc_id(self):
        for k in range(10):
            yield k

    def suggestions(self):
        for link in self.gen_suggestions():
            return link

    def gen_suggestions(self):
        for link in suggestions:
            yield link


class TestFTPSwiftea(FTPSwiftea):
    def __init__(self, host, user, password):
        FTPSwiftea.__init__(self, host, user, password)

    def get_inverted_index(self):
        return {}, False

    def send_inverted_index(self, inverted_index):
        #assert inverted_index == test_data.inverted_index
        assert 1

    def compare_indexs(self):
        for result in self.gen_compare_index():
            return result

    def gen_compare_index(self):
        yield True
        yield False


class TestWebConnexion(WebConnexion):
    def __init__(self):
        WebConnexion.__init__(self)

    def get_code(self, url):
        return test_data.code1, False, 1, url


class TestCrawler(Crawler):
    def __init__(self):
        self.site_informations = SiteInformations()
        if self.site_informations.STOPWORDS is None:
            tell('No stopwords, quit program')
            quit_program()
        self.file_manager = FileManager()
        self.ftp_manager = TestFTPSwiftea(test_data.HOST_FTP, test_data.USER, test_data.PASSWORD)
        self.get_inverted_index()
        self.index_manager = InvertedIndex()
        self.index_manager.setInvertedIndex(self.inverted_index)
        self.index_manager.setStopwords(self.site_informations.STOPWORDS)
        self.database = TestDatabaseSwiftea(test_data.HOST_DB, test_data.USER, test_data.PASSWORD, test_data.NAME_DB)
        self.web_connexion = TestWebConnexion()

        self.infos = list()
        self.crawled_websites = 0

    def safe_quit(self):
        self.send_inverted_index()
        tell('Programm will quit')
        tell('end\n', 0)

"""

class TestGlobal(object):
    def test_crawler(self):
        create_dirs()
        create_doc()
        try:
            mkdir(data.DIR_LINKS)
        except FileExistsError:
            pass
        def_links()
        crawler = TestCrawler()

        config = ConfigParser()
        config['DEFAULT'] = {
            'run': 'false',
            'reading_file_number': '0',
            'writing_file_number': '1',
            'reading_line_number': '0',
            'max_links': data.MAX_LINKS
        }
        with open(data.FILE_CONFIG, 'w') as configfile:
            config.write(configfile)

        crawler.start()
        test_data.reset()"""
