from django.views import View
from selenium import webdriver
from django.shortcuts import render, get_object_or_404, redirect
from selenium.webdriver.common.by import By
import requests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
import asyncio
from apiclient.discovery import build
import time
from django_q.tasks import async_task,result,fetch


class Search(View):
    def __init__(self):
        self.session = HTMLSession()
        self.melike = []
        self.search_term = ''
        self.dict_data = {}
        self.api_key = "AIzaSyAEz72lGXN65r0gVAVJqAD2wkdbpDkGm3M"
        self.deneme=[]




    def get(self,request):
        return render(request, "index.html")

    def post(self,request):
        search_term = request.POST['search']
        print(search_term)
        resource = build("customsearch", 'v1', developerKey=self.api_key).cse()
        resultx = resource.list(q=search_term, cx='015884101015322067297:8e-wesmmldu' ).execute()
        
        
        for item in resultx['items']:
             ac = async_task("core.services.testm",item['link'], timeout=100)
             ad = result(ac,wait=5000)
             self.melike.append(ad)
        return render(request, "index.html",{'data':self.melike})

      

    




