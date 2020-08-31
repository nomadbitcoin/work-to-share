from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import bs4, time
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument("profile")
options.add_argument("user-data-dir=./Browser/Profile")

driver = webdriver.Chrome(executable_path='./Browser/Driver/chromedriver', options=options)

url = input('Digite o link para a pesquisa: \n')
driver.get(url)
time.sleep(2)

results = []
count = 1
while True:
    #pega o html de cada pagina de resultado
    htmlPage = bs4.BeautifulSoup(driver.page_source, features='html.parser')

    results.extend(htmlPage.find_all('div', {'class':'section-result'}))
    
    button_status = htmlPage.find('button', {'jstcache':'348'})
    if button_status != None and button_status.get('disabled') == 'true':
        print('end')
        break
    
    next_page = driver.find_element_by_class_name('n7lv7yjyC35__button-next-icon')
    next_page.click()
    count+=1
    print('next to page {}'.format(count))
    time.sleep(2)
    
results = list(set(results))

data = []
for count, r in enumerate(results):
    name = r.find('h3', {'class':'section-result-title'}).text
    address = r.find('span', {'class':'section-result-location'}).text
    details = r.find('span', {'class':'section-result-details'}).text
    fone = r.find('span', {'jstcache':'167'}).text
    link = r.find('a').get('href')
    
    data_result = {'name': name, 'fone': fone, 'address': address, 'link': link, 'details': details}
    data.append(data_result)


dataframe_name = str(input('nome para o dataframe: (sem .csv)\n'))

data = pd.DataFrame(data)
data.reset_index(drop=True, inplace=True)
data.to_csv(dataframe_name + '.csv', index=None)