import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create a Request
url_site = "https://cafimafi.com/about"

site = requests.get(url_site)
soup = BeautifulSoup(site.text, 'html.parser')


# Scrapping The Website
x = soup.find('div' , {'class': 'bg-white rounded shadow-sm font-11 h-100 p-4'})
x2 = x.find_all('p')

L1 = []
for i in x2:
    L1.append(i)

df = pd.DataFrame(L1)
df.to_excel("E:\\dataset\\cafimafi.xlsx")

# Find The Picture Of The Each Items That We Want
x3 = soup.find('div', {'class': 'container-fluid'})
x4 = x.find_all('a', {'class': 'product'})

x4[1].find('img')['alt']
x4[0].img['alt']

List = []
Price = []
for i in range(15):
    List.append(x4[i].img['alt'])

df = pd.DataFrame(List)
df.to_excel("E:\\dataset\\cafimafi2.xlsx")



# Find The Price Of The Each Items That We Want
x3 = x2[0].find('div', {'class': 'product_price'})
x4 = x3.find('span', {'class': 'font-weight-bold'})

x4 = x4.replace('\n', '')
x4 = x4.replace('\t', '')

Price = []

for i in range(15):
    try:
        x3 = x2[i].find('div', {'class': 'product_price'})
        x4 = x3.find('span', {'class': 'font-weight-bold'})
        x4 = x4.text
        x4 = x4.replace('\n', '')
        x4 = x4.replace('\t', '')
    except:
        x4 = ' '

    Price.append(x4)

D1 = {
    'name' : List,
    "price": Price
}

df = pd.DataFrame(D1)
df.to_excel("E:\\dataset\\cafimafi3.xlsx")

