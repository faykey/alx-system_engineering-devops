#!/usr/bin/python3
"""
This is a Module for count_words function
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, new_after='', words_dict=None):
    """
    Queries the Reddit API, then parses the title
    of all hot articles, and prints a
    sorted count of given keywords.
    """

    if words_dict is None:
        words_dict = Counter()

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={'User-Agent': 'Custom'},
                       params={'after': new_after},
                       allow_redirects=False)

    if res.status_code != 200:
        return

    try:
        response = res.json().get('data', None)
        if response is None:
            return
    except ValueError:
        return

    children = response.get('children', [])

    for post in children:
        title = post.get('data', {}).get('title', '')
        for key_word in word_list:
            for word in title.lower().split():
                if key_word == word:
                    words_dict[key_word] += 1

    new_after = response.get('after', None)

    if new_after is None:
        sorted_dict = sorted(words_dict.items(),
                             key=lambda x: x[1],
                             reverse=True)

        for word, count in sorted_dict:
            if count != 0:
                print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, new_after, words_dict)
