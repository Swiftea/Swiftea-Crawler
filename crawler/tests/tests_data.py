#!/usr/bin/python3

from shutil import rmtree

from package.data import DIR_DATA, DIR_OUTPUT, DIR_LINKS, DIR_CONFIG

base_links = """http://swiftea.alwaysdata.net/0
http://swiftea.alwaysdata.net/1
http://swiftea.alwaysdata.net/2
http://swiftea.alwaysdata.net/3
http://swiftea.alwaysdata.net/4
http://swiftea.alwaysdata.net/5
http://swiftea.alwaysdata.net/6
http://swiftea.alwaysdata.net/7
http://swiftea.alwaysdata.net/8
http://swiftea.alwaysdata.net/9
http://swiftea.alwaysdata.net/10
http://swiftea.alwaysdata.net/11
http://swiftea.alwaysdata.net/12
http://swiftea.alwaysdata.net/13
http://swiftea.alwaysdata.net/14
"""

suggestions = ['http://suggestions.net/page1.html', 'http://suggestions.net/page2.html']

code1 = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="Description" content="Moteur de recherche">
        <title>Swiftea</title>
        <link rel="stylesheet" href="public/css/reset.css">
        <link rel="icon" href="public/favicon.ico" type="image/x-icon">
    </head>
    <body>
        <a href="demo">CSS Demo</a>
        <h1>Gros titre</h1>
        <h2>Moyen titre</h2>
        <h3>petit titre</h3>
        <p><strong>strong </strong><em>em</em></p>
        <a href="index">
            <img src="public/themes/default/img/logo.png" alt="Swiftea">
        </a>
        <a href="about/ninf.php" rel="noindex, nofollow">Why use Swiftea ?</a>
        <a href="about/ni.php" rel="noindex">Why use Swiftea ?</a>
        <a href="about/nf.php" rel="nofollow">Why use Swiftea ?</a>
        <img src="public/themes/default/img/github.png" alt="Github Swiftea">
        <img src="public/themes/default/img/twitter.png" alt="Twitter Swiftea">
    </body>
</html>
"""

code2 = """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-language" content="en">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-16 LE" />
        <link rel="shortcut icon" href="public/favicon2.ico" type="image/x-icon">
    </head>
    <body>
    </body>
</html>
"""

code3 = """<!DOCTYPE html>
<html>
    <head>
        <meta name="language" content="fr">
    </head>
    <body>
    </body>
</html>
"""

inverted_index = {'EN': {'T': {'ti': {'titre': {0: 0.375}}}, 'S': {'st': {'strong': {0: 0.125}}, 'sw': {'swiftea': {0: 0.125}}}, 'P': {'pe': {'petit': {0: 0.125}}}, 'G': {'gr': {'gros': {0: 0.125}}}, 'M': {'mo': {'moyen': {0: 0.125}}}}}

USER = ''
PASSWORD = ''
HOST_FTP = 'ftp'
HOST_DB = 'mysql'
NAME_DB = 'bdd'

def reset():
    rmtree(DIR_DATA)
    rmtree(DIR_CONFIG)
    rmtree(DIR_OUTPUT)
    rmtree(DIR_LINKS)
