import re
import os
import numpy as np
import pandas as pd


def question_topic_train_set():
    question_topic_dict = {}
    with open('data/question_topic_train_set.txt', 'r', encoding='utf8') as fr:
        for line in fr:
            q, ts = line.split()
            ts = ts.split(',')
            question_topic_dict[q] = ts[0]

    return question_topic_dict


def question_train_set():
    char_title = []
    word_title = []
    char_description = []
    word_description = []
    question_id = []

    count = 0

    max_len = 0
    with open('data/question_train_set.txt', 'r', encoding='utf8') as fr:
        for f in fr:
            count += 1
            if count % 5000 == 0:
                print('processed data', count, 'in question_train_set.txt')
            f = f.split()
            if len(f) == 3:
                question_id.append(f[0])
                char_title.append(f[1].split(','))
                if len(f[1].split(',')) > max_len:
                    max_len = len(f[1].split(','))
                word_title.append(f[2].split(','))
                char_description.append([])
                word_description.append([])
            elif len(f) == 5:
                question_id.append(f[0])
                char_title.append(f[1].split(','))
                if len(f[1].split(',')) > max_len:
                    max_len = len(f[1].split(','))
                word_title.append(f[2].split(','))
                char_description.append(f[3].split(','))
                word_description.append(f[4].split(','))
    print('max_len:', max_len)
    question_train_set_dict = {'char_title': char_title, 'word_title': word_title, 'char_description': char_description,
                               'word_description': word_description}

    return question_train_set_dict


def question_eval_set():
    char_title = []
    word_title = []
    char_description = []
    word_description = []
    question_id = []

    count = 0
    with open('data/question_eval_set.txt', 'r', encoding='utf8') as fr:
        for f in fr:
            count += 1
            if count % 5000 == 0:
                print('processed data', count, 'in question_eval_set.txt')
            f = f.split()
            if len(f) == 3:
                question_id.append(f[0])
                char_title.append(f[1].split(','))
                word_title.append(f[2].split(','))
                char_description.append([])
                word_description.append([])
            elif len(f) == 5:
                question_id.append(f[0])
                char_title.append(f[1].split(','))
                word_title.append(f[2].split(','))
                char_description.append(f[3].split(','))
                word_description.append(f[4].split(','))
    question_eval_set_dict = {'char_title': char_title, 'word_title': word_title, 'char_description': char_description,
                              'word_description': word_description}

    return question_eval_set_dict


def topic_info():
    char_name = []
    word_name = []
    char_description = []
    word_description = []
    topics = []
    topic2parent = {}

    count = 0
    with open('data/topic_info.txt', 'r', encoding='utf8') as fr:
        for f in fr:
            count += 1
            if count % 1000 == 0:
                print('processed %s lines.' % count)

            f = f.split()
            if len(f) == 4:
                topics.append(f[0])
                topic2parent[f[0]] = f[1].split(',')
                char_name.append(f[2].split(','))
                word_name.append(f[3].split(','))
                char_description.append([])
                word_description.append([])
            elif len(f) == 6:
                topics.append(f[0])
                topic2parent[f[0]] = f[1].split(',')
                char_name.append(f[2].split(','))
                word_name.append(f[3].split(','))
                char_description.append(f[4].split(','))
                word_description.append(f[5].split(','))

    _topic_info_dict = {'char_name': char_name, 'word_name': word_name, 'char_description': char_description,
                        'word_description': word_description, 'topics': topics, 'topic2parent': topic2parent}
    return _topic_info_dict


if __name__ == '__main__':
    topic_info_dict = topic_info()
    print(len(topic_info_dict.get('topics')))
    # for p in topic_info_dict.get('topic2parent').keys():
    #     print(p, ':', topic_info_dict.get('topic2parent').get(p))
    # question_train_set()