import re
from bs4 import BeautifulSoup

from locators.books_page_locator import BooksPageLocators
from parsers.book import BookParser


class BooksPage:
    def __init__(self, page) -> None:
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BooksPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self) -> int:
        content = self.soup.select_one(BooksPageLocators.PAGER).string
        match = re.search(' of (\d+)', content)
        return int(match.group(1))
