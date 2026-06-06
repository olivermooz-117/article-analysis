#!/usr/bin/env python3
"""Analyze a text article and report word and sentence statistics."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from typing import List, Optional, Sequence

DEFAULT_ARTICLE_FILENAME = "news-article.txt"
DEFAULT_TARGET_WORD = "the"


def _tokenize(text: str) -> List[str]:
    """Convert text to lowercase words, excluding punctuation."""
    return re.findall(r"\b[\w']+\b", text.lower())


def identify_most_common_word(text: str) -> Optional[str]:
    """Return the most common word in the text, or None when no words exist."""
    words = _tokenize(text)
    if not words:
        return None

    counts = Counter(words)
    return counts.most_common(1)[0][0]


def calculate_average_word_length(text: str) -> float:
    """Return the average length of words in the text."""
    words = _tokenize(text)
    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def count_paragraphs(text: str) -> int:
    """Count paragraphs separated by one or more blank lines."""
    stripped_text = text.strip()
    if not stripped_text:
        return 0

    paragraphs = [paragraph for paragraph in re.split(r"\n\s*\n", stripped_text) if paragraph.strip()]
    return len(paragraphs)


def count_sentences(text: str) -> int:
    """Count sentences using punctuation delimiters."""
    stripped_text = text.strip()
    if not stripped_text:
        return 0

    sentences = [sentence for sentence in re.split(r"[.!?]+", stripped_text) if sentence.strip()]
    return len(sentences)


def count_specific_word(text: str, target: str) -> int:
    """Count occurrences of the exact target word, case-insensitive."""
    if not target.strip():
        return 0

    target_lower = target.lower()
    return sum(1 for word in _tokenize(text) if word == target_lower)


def read_text_file(path: Path) -> str:
    """Read and return the contents of the specified file."""
    return path.read_text(encoding="utf-8")


def parse_arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Analyze a text article for basic metrics.")
    parser.add_argument(
        "-f",
        "--file",
        default=DEFAULT_ARTICLE_FILENAME,
        help=f"Path to the article text file (default: {DEFAULT_ARTICLE_FILENAME})",
    )
    parser.add_argument(
        "-t",
        "--target",
        default=DEFAULT_TARGET_WORD,
        help="Specific word to count in the text",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_arguments(argv)
    article_path = Path(args.file)

    if not article_path.exists():
        print(f"Error: input file '{article_path}' does not exist.")
        return 1

    article = read_text_file(article_path)

    print(count_specific_word(article, args.target))
    print(identify_most_common_word(article))
    print(calculate_average_word_length(article))
    print(count_sentences(article))
    print(count_paragraphs(article))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
