#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser

rss_url = 'https://aws.amazon.com/jp/blogs/aws/feed/'

rss_dic = feedparser.parse(rss_url)

entries = rss_dic.entries

for i in (reversed(entries)):
    date = i.published
    title = i.title
    url = i.link
    s = '更新日時\n' + date + '\n\n' + '更新内容\n' + title + '\n\n' + '詳細\n' + url 
    print('-'*50)
    print(s)
    print('-'*50)