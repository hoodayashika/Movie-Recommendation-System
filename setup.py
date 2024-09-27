from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Yashika Hooda'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'hoodayashika28@gmail.com',
    description = 'A small example package of movie recommendation syste',
    long_description = 'text/markdown',
    package = [SRC_REPO],
    package_requires = '>=3.12.5',
    install_requires = LIST_OF_REQUIREMENTS,
)