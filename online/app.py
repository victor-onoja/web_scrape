from bs4 import BeautifulSoup
import requests

def get_services(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs_list = soup.find('ul', class_='jobs-list')
    job = jobs_list.find_all('a')
    for j in job:
        print(j['title'])

if __name__ == '__main__':
    user_link = input("Please provide the link: ")
    get_services(user_link)
