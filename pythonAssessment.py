#!/usr/bin/env python3
import re
import sys
from typing import List, Dict, Optional


def _tokenize(text: str) -> List[str]:
    words = re.findall(r"\b[\w']+\b", text.lower())
    return words


def identify_most_common_word(text: str) -> Optional[str]:
    if not text.strip():
        return None

    words = _tokenize(text)
    if not words:
        return None

    word_count: Dict[str, int] = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return max(word_count, key=word_count.get)


def calculate_average_word_length(text: str) -> float:
    words = _tokenize(text)
    if not words:
        return 0.0

    total_length = 0
    for word in words:
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text: str) -> int:
    if not text.strip():
        return 1  # Empty text should count as 1 paragraph
    
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs) if paragraphs else 1

def count_sentences(text: str) -> int:
    if not text.strip():
        return 0

    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


def count_paragraphs(text: str) -> int:
    if not text.strip():
        return 1  # Fixed: empty text = 1 paragraph
    
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs) if paragraphs else 1


def count_specific_word(text: str, target: str) -> int:
    if not text.strip() or not target.strip():
        return 0

    words = _tokenize(text)
    target_lower = target.lower()
    count = 0
    i = 0
    while i < len(words):  # Added while loop
        if words[i] == target_lower:
            count += 1
        i += 1
    return count

def main() -> None:
    filename = sys.argv[1] if len(sys.argv) > 1 else "news-article.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            article = file.read()
    except FileNotFoundError:
        print(f"Error: input file '{filename}' does not exist.")
        sys.exit(1)

    print(count_specific_word(article, "the"))
    print(identify_most_common_word(article))
    print(calculate_average_word_length(article))
    print(count_sentences(article))
    print(count_paragraphs(article))


if __name__ == "__main__":
    main()
