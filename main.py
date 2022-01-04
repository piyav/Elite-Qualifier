#This program finds which posts are related to the Omicron variant in r/Coronavirus

from bs4 import BeautifulSoup
import requests
import lxml # Used in BS4 on line 13

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}

urls = 'https://www.reddit.com/r/Coronavirus/'

response = requests.get(urls, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

def displayData():
  for item in soup.select('.Post'):
    #print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
    myfind = item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text() #refers to title
    InitCapOmi  = myfind.find("Omicron") #finds wht title has "Omicron" in heading
    if InitCapOmi > 0: #Originally, func. displayed number. This statement prints whole statement
      #print(myfind)
      print('----------------------------------------')
      print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
      print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
      print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())
      print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])	
    smallcaseOmi = myfind.find("omicron") 
    if smallcaseOmi > 0: #same thing just lowercase "omicron"
      #print(myfind)
      print('----------------------------------------')
      print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
      print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
      print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())
      print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])	

  print('----------------------------------------')

displayData()

#Sources:
#Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
