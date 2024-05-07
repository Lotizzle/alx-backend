#!/usr/bin/env python3
"""
This module conatins the class Server which returns the
appropriate page of the dataset.
"""

import csv
import math
from typing import List


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
