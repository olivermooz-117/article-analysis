import re

def identify_most_common_word(text):
    if text.strip() == "":
        return None
    
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        clean_word = word.strip('.,!?";:()')
        if clean_word in word_count:
            word_count[clean_word] += 1
        else:
            word_count[clean_word] = 1
            
    most_common = ""
    for word in word_count:
        if most_common == "":
            most_common = word
        elif word_count[word] > word_count[most_common]:
            most_common = word
    return most_common

def calculate_average_word_length(text):
    words = text.split()
    if len(words) == 0:
        return 0
    
    total_length = 0
    for word in words:
        clean_word = word.strip('.,!?";()')
        total_length += len(clean_word)

    return total_length / len(words)

def count_paragraphs(text):
    if text.strip() == "":
        return 1

    count = 1
    i = 0

    while i < len(text) - 1:
        if text[i] == "\n" and text[i + 1] == "\n":
            count += 1
        i += 1

    return count

def count_sentences(text):
    if text.strip() == "":
        return 1
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


def count_specific_word(text, word):
    """Count occurrences of word in text (case-insensitive, whole words)."""
    if text is None or word is None:
        return 0
    pattern = r"\b" + re.escape(word) + r"\b"
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


file = open("news-article.txt", "r", encoding="utf-8")
article = file.read()
file.close()

print(count_specific_word(article, "the"))
print(identify_most_common_word(article))
print(calculate_average_word_length(article))
print(count_sentences(article))
print(count_paragraphs(article))