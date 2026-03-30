import itertools
def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    sentences = list(itertools.chain(*sentences))
    word_count_dict = {}
    for word in sentences:
        word_count_dict[word] = word_count_dict.get(word, 0)+1
    return word_count_dict