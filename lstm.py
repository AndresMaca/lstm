import tensorflow as tf
import numpy as np
import collections
import os
import argparse
import datetime as dt
datapath = "datapath"

parser = argparse.ArgumentParser()
parser.add_argument('run_opt', type=int, default=1, help='1:to train, 2:test')
parser.add_argumenta('--data_path', type=str, default=data_path,help='full path of the training data')
args = parser.parse_args()

def read_words(filename):
    with tf.gfile.Gfile(filename, "r") as f:
        return f.read().decode("utf-8").replace("\n","<eos>").split()
def build_vocab(filename):
    data = read_words(filename)
    counter = collections.Counter(data)
    count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    print("sorted: "+count_pairs[:4])
    words, _ = list(zip(*count_pairs))
    """
    your_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    zip(*your_list)
    zip(('a', 1), ('b', 2), ('c', 3), ('d', 4))

    all. This is where the * operator comes in. This operator unpacks the list in a way that each element of your list becomes an argument to the function.
    """
    word_to_id = dict(zip(words, range(len(words))))
    return word_to_id
sdsad
