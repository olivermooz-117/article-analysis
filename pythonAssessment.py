import re

def count_specific_word(text, search_word):
    words = re.findall(r"\b\w+\b", text.lower())
    count = 0

    for word in words:
        if word == search_word.lower():
            count += 1

    return count


def identify_most_common_word(text):
    if text.strip() == "":
        return None

    words = re.findall(r"\b\w+\b", text.lower())

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common = None

    for word in word_count:
        if most_common is None:
            most_common = word
        elif word_count[word] > word_count[most_common]:
            most_common = word

    return most_common


def calculate_average_word_length(text):
    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text):
    if text.strip() == "":
        return 1

    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    return len(paragraphs)


def count_sentences(text):
    if text.strip() == "":
        return 1

    sentences = re.split(r"[.!?]+", text)

    count = 0

    for sentence in sentences:
        if sentence.strip():
            count += 1

    return count


file = open("news-article.txt", "r", encoding="utf-8")
article = file.read()
file.close()

print("Count of 'the':", count_specific_word(article, "the"))
print("Most common word:", identify_most_common_word(article))
print("Average word length:", calculate_average_word_length(article))
print("Sentence count:", count_sentences(article))
print("Paragraph count:", count_paragraphs(article))