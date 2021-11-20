from consts import *
import requests
from bs4 import BeautifulSoup

     

def brain(gen_name): 
    r = requests.get(f"https://books.toscrape.com/catalogue/category/books/{gen_name}/index.html")
    soup = BeautifulSoup(r.content,"html.parser")
    pager = soup.find("ul", class_="pager")
    books = []

    if pager == None:
        books.append(soup.find_all("article",class_="product_pod"))
        titles = [element.find("h3").find('a').get("title") for element in books[0]]
        links = [element.find("a").get("href")[9:] for element in books[0]]
    else:
        sw = pager.find("li",class_="current").text.strip()
        pages_count = int(sw[-1])
        
        for page_number in range(1,pages_count + 1):
            r = requests.get(f"https://books.toscrape.com/catalogue/category/books/{gen_name}/page-{page_number}.html")
            soup = BeautifulSoup(r.content,"html.parser")
            books.append(soup.find_all("article",class_="product_pod"))
        

        page_number = int(input(f"{pages_count} Pages, What Page do you want: "))
        titles = [element.find("h3").find('a').get("title") for element in books[page_number - 1]]
        links = [element.find("a").get("href")[9:] for element in books[page_number - 1]]
    number_of_books_in_page = len(titles) 

    if titles == []:
        print("No books detected")
        return

    for title_n in range(number_of_books_in_page):
        print(f"Book: {title_n} name: {titles[title_n]} ")

    user_book_choice = int(input("Choose a book number: "))

    if user_book_choice <= number_of_books_in_page:
        link = f"https://books.toscrape.com/catalogue/{links[user_book_choice]}"
        r = requests.get(link)
        soup = BeautifulSoup(r.content,"html.parser")
        Description = soup.find_all("p")[3].text
        print(f"""
        Description: {Description}
        Link: {link}
        """)



def main():
    print(ui_text["ui1"])
    user_genere_number = input(ui_text["ui2"])
    if user_genere_number not in geners.keys():
        print("Wrong Choice")
        return
    user_genere = geners[user_genere_number]
    
    brain(user_genere)

    print(ui_text["ui3"])

main()
