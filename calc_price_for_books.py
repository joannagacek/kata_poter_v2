from typing import List

'''
Count price for a given book set. Books are represented by the integers e.g. [1,2] - two different books. 
Implementation details at https://codingdojo.org/kata/Potter/
'''


def calc_price_for_books(book_list: List[int], discount: List[float]) -> float:
    sell_price = 0.0
    book_series = []

    for _, book in enumerate(book_list):
        book_exists = False
        for j, book_set in enumerate(book_series):
            if not (book in book_series[j]):
                book_series[j].append(book)
                if _check_if_it_can_be_cheaper(book_set, book_series, j):
                    book_series[j + 1].append(book_series[j].pop(4))
                book_exists = True
                break
        if not book_exists:
            book_series.append([book])

    for book_set_index in book_series:
        sell_price += 8 * len(book_set_index) * discount[len(book_set_index)]

    return sell_price


def _check_if_it_can_be_cheaper(book_set, book_series, index: int) -> bool:
    return 5 == len(book_set) and index + 1 < len(book_series) and len(book_series[index + 1]) == 3
