from bs4 import BeautifulSoup
import requests
import json

def python():
    
    api="https://en.wikipedia.org/wiki/Python_(programming_language)"
    page=requests.get(api)
    code=BeautifulSoup(page.text,"html.parser")
    table=code.find("table",class_="infobox vevent")
    table_1=table.find_all("th",class_="infobox-label")
    menu=[]
    for i in table_1:
        a=i.get_text()
        menu.append(a)   
    table_2=table.find_all("td",class_="infobox-data")
    k=0
    dict={}
    for j in table_2:
        b=j.get_text()
        c=menu[k]
        dict[c]=b
        k+=1
    for m in dict:
        # print(m," "*10,dict[m])
        with open("task_4.json","w") as file:
                json.dump(dict,file,indent=6)
    return  dict 
python()         
    
    