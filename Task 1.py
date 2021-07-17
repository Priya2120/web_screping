# from bs4 import BeautifulSoup
# import os
# import requests
# import json
# import pprint

# def wed_event():
#     list = []
#     if os.path.isfile("e-commers.json"):
#         with open("e-commers.json","r")as f:
#             json.load(f)
#     else:
#         web_event_api = "https://webscraper.io/test-sites"
#         web_event_url = requests.get(web_event_api)
#         web_event_data = web_event_url.json
#         code = BeautifulSoup(web_event_url.text,"html.parser")
#         main_div = code.find("div",class_="container test-sites")
#         main = main_div.find_all('h2')
#         for i in main:
#             a=(i.get_text().strip)
#             b=("https://webscraper.io"+i.a["href"])
#             dict1={"name":a,"url":b}
#             list.append(dict1)
#             with open("e-commers.json","w")as f:
#                 json.dump(list,f,indent=3)
# pprint(wed_event())






