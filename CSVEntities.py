import csv
from datetime import date
from dateutil.parser import parse

import ClassNews

FIELDNAMES_READ = ['date', 'title', 'link', 'article', 'links']
FIELDNAMES_WRITE = ['date', 'title', 'link', 'article', 'links']


def csv_to_python(articles_list, csv_file):
    """This function inserts news to the source csv file that has never been seen in it."""
    articles_list_from_csv = []
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file, FIELDNAMES_READ, delimiter='\t')
        for items in reader:
            r = ClassNews.MyArticle(dict(items))
            #print(r.links)
            articles_list_from_csv.append(r)

    union_list = articles_list_from_csv[:]
    #print(articles_list_from_csv)
    for item in articles_list:
        if item not in articles_list_from_csv:
            union_list.append(item)

    #print(union_list)
    with open(csv_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES_WRITE, delimiter='\t')
        for item in union_list:
            writer.writerow(item.__dict__)


def return_news_to_date(input_date, csv_file, limit):
    article_list_by_date = []
    datetime_input=date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file, FIELDNAMES_READ, delimiter='\t')
        article_counter=0
        for items in reader:

            article_from_file = ClassNews.MyArticle(dict(items))

            date_time = parse(article_from_file.date)
            date_from_file = date_time.date()

            if date_from_file == datetime_input:
                article_counter+=1
                article_list_by_date.append(article_from_file)

            if limit == article_counter:
                print(article_list_by_date)
                return article_list_by_date
    return article_list_by_date