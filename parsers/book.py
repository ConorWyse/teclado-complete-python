import re

from locators.book_locators import BookLocators

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
        self.parent = parent
    
    def __repr__(self) -> str:
        available = 'available' if self.available else 'out of stock'
        return f'<Book {self.title}, {self.rating} stars, at £{self.price}, {available}>'

    @property
    def title(self) -> str:
        locator = BookLocators.TITLE
        item_link = self.parent.select_one(locator).attrs['title']
        return item_link
    
    @property
    def href(self) -> str:
        locator = BookLocators.LINK
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link
    
    @property
    def price(self) -> float:
        locator = BookLocators.PRICE
        item = self.parent.select_one(locator).text
        matches = re.search('£(\d+\.\d+)', item)
        return float(matches.group(1))
    
    @property
    def rating(self) -> int:
        locator = BookLocators.RATING
        item_link = self.parent.select_one(locator)
        classes = item_link.attrs['class']
        rating_classes = [className for className in classes if className != 'star-rating']
        rating_value = BookParser.RATINGS.get(rating_classes[0]) # None if not found
        return rating_value

    # Somewhat pointless as all books are "in stock"; and because the tutor meant
    # "next book" when he said "next AVAILABLE book"
    @property
    def available(self) -> bool:
        locator = BookLocators.AVAILABLE
        item_link = self.parent.select_one(locator)
        classes = item_link.attrs['class']
        return 'instock' in classes
