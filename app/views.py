# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from apiclient.discovery import build
# import requests as req
# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
import asyncio




@login_required(login_url="/login/")
def index(request):
    session = HTMLSession()
    melike = []
    search_term = ''
    api_key = "AIzaSyAEz72lGXN65r0gVAVJqAD2wkdbpDkGm3M"

    if 'search' in request.GET:
        search_term = request.GET['search']
        print(search_term)
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=search_term, cx='015884101015322067297:8e-wesmmldu' ).execute()
        for item in result['items']:
             melike.append(list_title_link(item))
        print(melike)
        
        # browser = webdriver.Firefox()
        # browser.get("https://www.bhphotovideo.com/c/buy/Computer-Memory/ci/13341/N/3835434469")
        # for elem in browser.find_elements_by_xpath('/html/body/div[2]/main/section/div/div/div/div[4]/section/div[2]/div[1]'):
        #     /html/body/div[1]/main/section/div/div/div/div[4]/section/div[2]/div[3]
        #     print (elem.text)
        # r = session.get('https://www.bhphotovideo.com/c/buy/Computer-Memory/ci/13341/N/3835434469')
        # aa = r.html.xpath('.//span[@data-selenium="uppedDecimalPriceFirst"]')
        # bb = r.html.xpath('.//span[@data-selenium="miniProductPageProductName"]')
        
        # for x in aa:
        #     print(x.find('span', first=True).text)
        # for y in bb:
        #     print(y.find('span', first=True).text)
       
      

    return render(request, "index.html")

def  list_title_link(data):
    # session = HTMLSession()
    asession = AsyncHTMLSession()
    dict_data = dict()
    r = asession.get(data['link'])
    aa = r.html.xpath('.//span[@data-selenium="uppedDecimalPriceFirst"]')
    bb = r.html.xpath('.//span[@data-selenium="miniProductPageProductName"]')
        
    for x in aa:
             dict_data['price'] = x.find('span', first=True).text
    for y in bb:
              dict_data['pro'] = y.find('span', first=True).text
            
    return dict_data



    # browser = webdriver.Firefox()
    # b = browser.get(data['link'])
    # a=[];
    # print(b)
    # try:
    #     a = browser.find_element(By.XPATH, '/html/body/div[1]/main/section/div/div/div/div[4]/section/div[2]/div[1]/div/div[3]/div[1]/div/div').text
    #     print(a)
    # except Exception as err:
    #     print(err)

    # # a = requests.get(data['link'])
    # # dict_data['web'] = a

    #     # dict_data['src'] =  data['pagemap']['metatags']



@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))

