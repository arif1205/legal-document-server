import re
from typing import List
from models.schemas import Match


def keywords(q: str) -> List[str]:
    """
    Extract each word as a keyword from a query string.
    """
    words = re.findall(r"\w+", q.lower()) 
    keywords = []
    for t in words:
        if len(t) > 2:
            keywords.append(t)
    return keywords


def score(text: str, keywords: List[str]) -> int:
    """
    Score a text based on how many keywords i can find in it.
    """
    tl = text.lower()
    total_score = 0
    for t in keywords:
        count = tl.count(t)
        total_score += count
    return total_score


def make_summary(all_matches: List[Match]) -> str:
    return all_matches[0].text

