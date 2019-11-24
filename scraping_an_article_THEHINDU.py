import requests
import bs4 as bs
source = requests.get('https://www.thehindu.com/news/national/revocation-of-article-370-will-restore-long-term-peace-in-kashmir-amit-shah/article29689388.ece')
soup = bs.BeautifulSoup(source.text,'lxml')
print(soup.title.string)
intro = soup.find('h2', attrs={'class': 'intro'})
print(intro.text)
para = soup.find('div', attrs = {'class': 'article'})
article = ''
for i in para.findAll('p'):
    article = article + ' ' +  i.text
print(article)
