#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: ??
@author: li
@file: configure.py
@time: 2018/10/31 1:52 PM
配置文件
"""

import os


class Configure(object):

    project_path = "/Users/li/PycharmProjects/event_parser/src"
    # project_path = os.getcwd()

    # singlepass_run 和history_event 使用同一个时间段前的新闻，动态更新使用该时间之后的新闻
    data_time = '1545235200'

    # 词典目录
    dic_path = project_path + '/corpus'
    stock_new_path = dic_path + "/stock.csv"

    # 停用词目录
    stop_words_path = project_path + '/corpus/stop_words_CN'

    # tf-idf 训练语料文件位置，标题和正文合并在一起
    corpus_train_path = project_path + "/data/text_full_index.txt"

    # 新闻标题的保存路径
    corpus_news_title = project_path + "/data/text_title_index.txt"

    # singlePass聚类结果保存目录文件
    clustering_save_path = project_path + '/model/clustering_new_10.pkl'
    # clustering_save_path = project_path + '/model/clustering_new_20.pkl'
    # clustering_save_path = project_path + '/model/clustering_new_30.pkl'
    # clustering_save_path = project_path + '/model/clustering_new_40.pkl'

    corpus_news = corpus_train_path

    event_unit_path = project_path + '/model/event_units_new_10.pkl'
    # event_unit_path = project_path + '/model/event_units_new_20.pkl'
    # event_unit_path = project_path + '/model/event_units_new_30.pkl'
    # event_unit_path = project_path + '/model/event_units_new_40.pkl'

    event_save_path = project_path + '/model/event_model/'

    # TF-IDF计算相关文件
    tfidf_feature_path = project_path + '/model/tfidf_model/feature_full.pkl'
    tfidftransformer_path = project_path + '/model/tfidf_model/tfidftransformer_full.pkl'
    word_dict_path = project_path + '/model/tfidf_model/word_dict_full.pkl'


conf = Configure()
