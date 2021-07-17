from task1 import scrape_top_list
from task_2 import scrape_top_list_1
# from bs4 import BeautifulSoup
import json


scrapped_data=scrape_top_list()
movie_by_year=scrape_top_list_1(scrapped_data)
def scrape_top_list_2(movie):
    moviedec={}
    list1=[]
    for year in movie:
        mod=year%10
        decade=year-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    # print(list1)
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movie:
            if x<=dec10 and x>=i:
                for v in movie[x]:
                    moviedec[i].append(v)
        with open("task_3.json","w")as file:
            json.dump(moviedec,file,indent=4)
    return moviedec

scrape_top_list_2(movie_by_year)

