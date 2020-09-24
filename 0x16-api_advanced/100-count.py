#!/usr/bin/python3
""" Recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """count_words"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, params={'after': after},
                     allow_redirects=False,
                     headers={'user-agent': 'myUser'})

    if r.status_code == 200:
        data = r.json()

        for hotTopic in (data['data']['children']):
            for word in hotTopic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is not None:
            count_words(subreddit, word_list, after, count)
        else:
            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if count[j] > count[i] or
                    (word_list[i] > word_list[j] and
                     count[j] == count[i]):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0):
                    print("{}: {}".format(word_list[i].lower(), count[i]))
