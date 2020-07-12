from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=6
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
            
        # notifyMe("Yogesh","Lets stop the spread of this virus together")
        myHtmlData=getData('https://www.mohfw.gov.in/')
        soup=BeautifulSoup(myHtmlData,'html.parser')
        # print(soup.prettify())

        myDataStr= ""
 
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList= myDataStr.split("\n\n")

        states=['Chandigarh','Telangana','Uttar Pradesh']
        for item in itemList[0:36]:
            dataList=item.split('\n')
            if dataList[1] in states:
                # print(dataList)
                nTitle='Cases of covid-19'
                nText=f"State {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\n Cured:{dataList[4]}\n Death:{dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(5)

        time.sleep(20)

        #     # print (table)