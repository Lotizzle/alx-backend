#!/usr/bin/env python3
"""
This module contains the Server class, get_page method,
and the get_hyper method
"""

import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start index and end index
    corresponding to the range of indexes to return for pagination.

    Page numbers are 1-indexed.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """

    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    start_index = (page-1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.

        Args:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The list of rows corresponding to the requested page.
        """

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary containing some key, value pairs

        Args:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            Dict[str, Any]: Dict of certain key value pairs
        """

        data_page = self.get_page(page, page_size)
        data_length = len(data_page)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if data_length == data_length else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': data_length,
            'page': page,
            'data': data_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
