import os.path
import re
from typing import Iterable, Any, Iterator, List
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def check_path(file_name: str) -> bool:
    if os.path.exists(DATA_DIR + os.sep + file_name):
        return True
    else:
        return False


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)


def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    return map(lambda x: x.split(' ')[int(value)], data)


def unique_query(data, *args: Any, **kwargs: Any) -> set[str]:
    return set(data)


def sort_query(value: str, data: Iterable[str]) -> List[str]:
    reverse: bool = value == 'desc'
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable[str]) -> List[str]:
    return list(data)[:int(value)]


def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    pattern: re.Pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)


#"images/\\w+\\.png"