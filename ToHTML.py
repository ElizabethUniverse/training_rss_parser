import glob
from dominate import document
from dominate.tags import *

photos = glob.glob('photos/*.jpg')
def print_article_list_to_html(list_articles, path):
    with document(title='RssReader') as doc:
        for item in list_articles:
            div("Title: %s" % item.title)
            div("Date: %s" % item.date)
            div( "Link: %s" % item.link)
            div("%s" % item.article)
            for idx, link in enumerate(item.links):
                div("[%d]:%s" % (idx, link))
            div()
            # for path in range(5):
            #     div(img(src=path), _class='photo')


    with open('gallery.html', 'w') as f:
        f.write(doc.render())