#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'ipyProject',
    'author':'DemonLee',
    'url':'https://google.com.hk',
    'download_url':'https://google.com.hk',
    'author_email':'leodemon_c@126.com',
    'version':'0.1',
    'install_requires':['nose','pip','distribute'],
    'packages':['ipyPro'],
    'scripts':[],
    'name':'ipyProject'
}

setup(**config)

