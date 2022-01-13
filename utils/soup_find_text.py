from bs4 import BeautifulSoup


def get_soup_text(source, tag, className):
    html = source.find(tag, class_=className)
    if html:
        return html.get_text()
    return ''