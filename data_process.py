# -*- coding: UTF-8 -*-

import os 
import pandas as pd

def train_sample_generate(train_query_path, train_reply_path):
    train_query_dict = {}
    train_samples = []

    with open(train_query_path, 'r') as f:
        for line in f.readlines(): 
            line = line.strip()
            session_idx,query = line.split('\t')
            train_query_dict[session_idx] = [query]
    
    with open(train_reply_path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            session_idx, reply_idx, answer, label = line.split('\t')
            train_query_dict[session_idx].append((answer,label))

    for k,v in train_query_dict.items():
        query = v[0]
        for _ in v[1:]:
            train_samples.append(
                {
                    'query':query,
                    'answer': _[0],
                    'label': _[1]
                }
            )

    return train_samples


def test_sample_generate(test_query_path, test_reply_path):
    test_query_dict = {}
    test_samples = []

    with open(test_query_path, 'r', encoding='gbk') as f:
        for line in f.readlines():
            line = line.strip()
            session_idx, query = line.split('\t')
            test_query_dict[session_idx] = [query]
        
    with open(test_reply_path, 'r', encoding='gbk') as f:
        for line in f.readlines():
            line = line.strip()
            session_idx, reply_idx, answer = line.split('\t')
            test_query_dict[session_idx].append(answer)   

    for k,v in test_query_dict.items():
        query = v[0]
        for answer in v[1:]:
            test_samples.append({
                'query':query,
                'answer':answer
            })
    
    return test_samples

if __name__ == "__main__":
    train_path = 'data/train/'
    test_path = 'data/test/'
    train_query_path = os.path.join(train_path, 'train.query.tsv')
    train_reply_path = os.path.join(train_path, 'train.reply.tsv')
    test_query_path = os.path.join(test_path, 'test.query.tsv')
    test_reply_path = os.path.join(test_path, 'test.reply.tsv')
    
    train_samples = train_sample_generate(train_query_path, train_reply_path)
    test_samples = test_sample_generate(test_query_path, test_reply_path)
    pd.DataFrame(train_samples).to_excel('data/train_samples.xlsx')
    pd.DataFrame(test_samples).to_excel('data/test_samples.xlsx')


    
    

