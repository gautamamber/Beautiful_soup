from bs4 import BeautifulSoup
soup = BeautifulSoup("<html><p>amber gautam</p></html>", 'html.parser')
print soup.prettify()