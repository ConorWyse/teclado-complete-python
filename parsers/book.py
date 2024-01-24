import logging
import re

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    Given one of the specific quote divs, find out the data about
    the book (title, rating, price).
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent) -> None:
        # 'parent' is a BeautifulSoup object
        #logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent
    
    def __repr__(self) -> str:
        available = 'available' if self.available else 'out of stock'
        price = "{:,.2f}".format(self.price)
        return f' • {self.rating} stars, £{price} : {self.title}'

    @property
    def title(self) -> str:
        logger.debug('Finding book name...')
        locator = BookLocators.TITLE
        item_link = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found book name, `{item_link}`.')
        return item_link
    
    @property
    def href(self) -> str:
        logger.debug('Finding book URL...')
        locator = BookLocators.LINK
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book URL, `{item_link}`.')
        return item_link
    
    @property
    def price(self) -> float:
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE
        item = self.parent.select_one(locator).text
        matches = re.search('£(\d+\.\d+)', item)
        bookprice = float(matches.group(1))
        logger.debug(f'Found book price, `{bookprice}`.')
        return bookprice
    
    @property
    def rating(self) -> int:
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING
        item_link = self.parent.select_one(locator)
        classes = item_link.attrs['class']
        rating_classes = [className for className in classes if className != 'star-rating']
        rating_value = BookParser.RATINGS.get(rating_classes[0]) # None if not found
        logger.debug(f'Found book rating, `{rating_value}`.')
        return rating_value

    # Somewhat pointless as all books are "in stock"; and because the tutor meant
    # "next book" when he said "next AVAILABLE book"
    @property
    def available(self) -> bool:
        logger.debug('Finding book availability...')
        locator = BookLocators.AVAILABLE
        item_link = self.parent.select_one(locator)
        classes = item_link.attrs['class']
        is_in_stock = 'instock' in classes
        logger.debug(f'Found book availability, `{is_in_stock}`.')
        return is_in_stock
