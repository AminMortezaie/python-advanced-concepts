import inspect
from dataclasses import dataclass
from pprint import pprint

@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: int

def main():
    comment = Comment(1, "this is a comment!")
    print(inspect.getmembers(Comment, inspect.isfunction))