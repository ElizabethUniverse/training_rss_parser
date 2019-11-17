import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
# metadata
    name='rss_reader',
    version='1.1',
    author='Elizaveta Lapunova',
    author_email='liza.lapunova99@gmail.com',
    url='https://github.com/ElizabethUniverse/FinalTaskRssParser',

    description='RSS parser',
    long_description=read("README.md"),
    license='BSD',
    platforms='any',

    #options
    packages=find_packages(),
    install_requires=['html2text==2019.9.26'],
    package_data={
         '': ['*.py', '*.txt']
    },
    entry_points={
        "console_scripts":
            "rss_reader=rss_reader.rss_reader:main"
    },
    #test_suite='rss_reader.test',
    zip_safe=False
)
