import argparse
import re
import xml.etree.ElementTree as ET
import requests
import json

import RssReaderExceptions as rre
import ClassNews

VERSION = 1.1

# Parse our arguments
parser = argparse.ArgumentParser()
parser.add_argument("sourse", help="RSS URL")
parser.add_argument('--version', action='store_true', help='Print version info')
parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
parser.add_argument('--verbose', action='store_true', help='Outputs verbose status messages')
parser.add_argument('--limit', type=int, help='Limit news topics if this parameter provided')

args = parser.parse_args()


if args.version:
    print("Current version: "+str(VERSION))
# if args.json:
#     print('json')
if args.verbose:
    print('verbose')
if args.limit:
    print('LIMIT is: '+str(args.limit))

try:
    '''Check if the request is valid'''
    if not re.match("(https|http):\/\/((\w+).)+(com|org|ru)(\/(\w+))+", args.sourse):
        raise rre.NotRequest
    #reque = requests.get(args.sourse, timeout=(1, 10))

    # Get request
    rss_request = requests.get(args.sourse)

    # Check status code
    status_code = rss_request.status_code
    print(status_code)
    # if status_code == 404:
    #     raise requests.exceptions.HTTPError
    rss_request.raise_for_status()

    # Here we check the type of response. To correctly process it
    print(rss_request.headers['content-type'])
    root = ET.fromstring(rss_request.content)

    # Here we get title of api
    for child in root.iter('channel'):
        for item in child:
            if item.tag == 'title':
                main_title = item.text

    my_articles = ClassNews.xml_arguments_for_class(root, 10)
    # Here we have a dictionary of articles
    print(my_articles)

    print("\nFeed: {}".format(main_title))
    for article in my_articles:
        print(ClassNews.MyArticle(article))
    if args.json:
        json_articles = json.dumps(my_articles, indent=4)
        print(json_articles)
except rre.NotRequest as exc:
    print(str(exc))
except requests.exceptions.ConnectTimeout:
    print('Time to connect is out')
except requests.exceptions.ReadTimeout:
    print('Time to read is out')
except requests.exceptions.HTTPError as httpserr:
    print("Sorry, page not found")
    print(httpserr.response.content)
except requests.exceptions.InvalidURL:
    print("Sorry, that's not valid url")
except requests.exceptions.ConnectionError:
    print("Sorry, you have an proxy or SSL error")
    # A proxy or SSL error occurred.



