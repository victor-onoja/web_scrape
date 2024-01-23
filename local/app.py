from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    questions_html_tags = soup.find_all('h3')
    for q in questions_html_tags:
        print(q.text)
