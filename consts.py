from enum import Enum

class bookType(Enum):
    TWO_DAYS = 1
    FIVE_DAYS = 2
    TEN_DAYS = 3

class bookName(Enum):
    bookID = 0
    bookName = 1
    Author = 2
    yearPublished = 3
    bookType = 4
    isLoaned = 5