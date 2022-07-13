import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)

def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    return response


def parse_results(response):
    # Hardcoding the css classes for the elements
    result_box_identifier = ".tF2Cxc"
    title_identifier = "h3"
    link_identifier = ".yuRUbf a"
    text_identifier = ".VwiC3b"
    
    results = response.html.find(result_box_identifier)
    final_results = []

    for result in results:
        # Debugging
        text = result.find(text_identifier, first=True)
        link = result.find(link_identifier, first=True)
        
        # Check for null values
        if text == None or link == None:
            item = {
                'title': result.find(title_identifier, first=True).text ,
                'link': '',
                'text': ''
            }
        else:
            item = {
                'title': result.find(title_identifier, first=True).text ,
                'link': link.attrs['href'],
                'text': text.text
            }
        
        final_results.append(item)

    return final_results

def google_search(query):
    res = get_results("data science")
    return parse_results(res)

