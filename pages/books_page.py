import logging
import re
from bs4 import BeautifulSoup

from locators.books_page_locator import BooksPageLocators
from parsers.book import BookParser

logger = logging.getLogger('scraping.books_page')

class BooksPage:
    def __init__(self, page) -> None:
        logger.debug('Parsing page content with BeautifulSoup parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BooksPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self) -> int:
        content = self.soup.select_one(BooksPageLocators.PAGER).string
        logger.info(f'Found pager info: `{content}`.')
        match = re.search(' of (\d+)', content)
        count = int(match.group(1))
        logger.debug(f'Pages to scrape: `{count}`')
        return count
