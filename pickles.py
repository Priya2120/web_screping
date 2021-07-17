from bs4 import BeautifulSoup
import requests
import json 
import pprint

def pical_web():
    link = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    shr=requests.get(link)
    shra=BeautifulSoup(shr.text,"html.parser")
    main_1=shra.find("div",class_="1gx7").span.get_text()
    div=main_1.split()
    a=int(div[1])
    b=a//32+1
    s=0
    list1=[]
    while s<=b:
        web_pical="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
        web=requests.get(web_pical)
        web2=BeautifulSoup(web.text,"html.parser")
        