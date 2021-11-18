import requests
from bs4 import BeautifulSoup
def main():
    Titles = []
    for i in range(1,50 + 1):
        r = requests.get(f"http://books.toscrape.com/catalogue/page-{i}.html")
        soup = BeautifulSoup(r.content,'html.parser')
        
        wewe= soup.find_all('article',class_='product_pod')
        Titles.append([element.find('h3').text for element in wewe])
        print(f"Page {i} Done")

    with open("titles.txt","w") as file:
        for j in Titles:
            for Title in j:
                file.write(Title + "\n") 


main()