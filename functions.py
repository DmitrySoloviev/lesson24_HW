import os.path
from typing import Iterable, Any
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def check_path(file_name) -> bool:
    if os.path.exists(DATA_DIR + os.sep + file_name):
        return True
    else:
        return False


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)


def map_query(value: str, data: Iterable[str]):
    return map(lambda x: x.split(' ')[int(value)], data)


def unique_query(data, *args: Any, **kwargs: Any):
    return set(data)


def sort_query(value: str, data: Iterable[str]):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def limit_query(value, data):
    return list(data)[:int(value)]

