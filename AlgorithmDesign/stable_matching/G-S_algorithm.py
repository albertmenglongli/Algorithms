# -*- coding:utf-8 -*-
from AlgorithmDesign.stable_matching import Man, Woman
from operator import attrgetter
from random import shuffle
from funcy import walk, first

men = [Man('Albert', age=20, height=170, preferences_key=lambda x: -len(x.name)),  # 喜欢名字长的
       Man('Bob', age=18, height=175, preferences_key=attrgetter('age')),  # 喜欢年龄小的
       Man('Cyrus', age=20, height=180, preferences_key=attrgetter('age'))  # 喜欢年龄小的
       ]

women = [Woman('Alice', age=18, height=165, preferences_key=attrgetter('age')),  # 喜欢年龄小的
         Woman('Brenda', age=20, height=165, preferences_key=lambda x: -x.height),  # 喜欢个子高的
         Woman('Claire_CC', age=19, height=165, preferences_key=attrgetter('name')),  # 喜欢名字字母顺序靠前的
         ]

shuffle(men)
shuffle(women)

# while there is a man m who is free and hasn't proposed to every woman
while filter(lambda x: x.proposal is None, men):
    m = first(filter(lambda _m: _m.proposal is None, men))
    w = first(filter(lambda _w: not m.has_proposed(_w), m.get_ranks(women)))
    m.append_to_proposed(w)
    if w.proposal is None:
        m.proposal = w
        w.proposal = m
    else:
        w_ranks = w.get_ranks(men)
        cur_m = w.proposal
        if w_ranks.index(cur_m) < w_ranks.index(m):
            continue
        else:
            cur_m.proposal = None
            w.proposal = m
            m.proposal = w

for m in sorted(men, key=attrgetter('name')):
    print m, '<-->', m.proposal

walk(lambda x: x.reset(), men)
walk(lambda x: x.reset(), women)
