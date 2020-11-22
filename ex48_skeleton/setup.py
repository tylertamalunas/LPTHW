try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'descrption': 'My Project',
    'author': 'Tyler Tamalunas',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'tylertamalunas@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'lexicon test'
}

setup(**config)