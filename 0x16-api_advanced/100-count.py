#!/usr/bin/python3
"""Queries the Reddit API and
returns a list containing the
titles of all hot articles for
a given subreddit.

If no results are found for the
given subreddit, the function
should return Invalid.
"""
import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    if count_dict is None:
        count_dict = {}

    reddit = requests.Reddit(client_id='your_client_id_here',
                         client_secret='your_client_secret_here',
                         user_agent='your_user_agent_here')
    
    try:
        sub = reddit.subreddit(subreddit)
        hot_posts = sub.hot(limit=100, params={'after': after})

        for post in hot_posts:
            title = post.title.lower()
            for word in word_list:
                if word.lower() in title:
                    if word in count_dict:
                        count_dict[word] += 1
                    elif word.lower() in count_dict:
                        count_dict[word.lower()] += 1
                    else:
                        count_dict[word] = 1

        if hot_posts:
            count_words(subreddit, word_list, count_dict, after=hot_posts[-1].name)
        else:
            sorted_words = sorted(count_dict.items(), key=lambda x: x[0].lower())
            for word, count in sorted_words:
                print(f'{word}: {count}')
    except:
        print('Invalid subreddit.')
