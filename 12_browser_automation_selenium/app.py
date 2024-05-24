import logging
import requests

from pages.books_page import BooksPage

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    level=logging.INFO,
    filename='logs.txt'
)

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = BooksPage(page_content)

books = page.books
page_count = page.page_count

# We have page 1 already, so start from 2. We want to go to 50 but we need
# to add 1 to the 50 because Python thinks we are in the 1960s still.
for page_num in range(2, page_count+1):
    url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
    page_content = requests.get(url).content
    page = BooksPage(page_content)
    books.extend(page.books)
