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
    counter = collections.Counter(data)#numero de palabras
    print("first counter items: "+counter.items()[0])
    count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    """
    key is a function that will be called to transform the collection's items before they are compared. The parameter passed to key must be something that is callable.
    """
    print("sorted: "+count_pairs[:4])
    words, _ = list(zip(*count_pairs))
    """
    your_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    zip(*your_list)
    zip(('a', 1), ('b', 2), ('c', 3), ('d', 4))

    all. This is where the * operator comes in. This operator unpacks the list in a way that each element of your list becomes an argument to the function.
    """
    word_to_id = dict(zip(words, range(len(words))))
    return word_to_id #word_to_id: ordena de mayor a menor segun el numero de apariciones, asigna un numero segun la posicion, ie: (a,0),(x,1),(car,2) so, a is the word with most appearances, x is the second one, so on..

def file_to_word_ids(filename, word_to_id):
    data = read_words(filename)
    return [word_to_id[word] for word in data if word in word_to_id]

def load_data():
    train_path = os.path.join(data_path, "ptb.train.txt")
    valid_path = os.path.join(data_path, "ptb.valid.txt")
    test_path = os.path.join(data_path, "ptb.test.txt")

    word_to_id = build_vocab(train_path) #word_to_id: ordena de mayor a menor segun el numero de apariciones, asigna un numero segun la posicion, ie: (a,0),(x,1),(car,2) so, a is the word with most appearances, x is the second one, so on..
    train_data = file_to_word_ids(train_path, word_to_id) # interchange the word for the id.
    valid_data = file_to_word_ids(valid_path, word_to_id)
    test_data = file_to_word_ids(test_path, word_to_id)
    vocabulary = len(word_to_id)
    reversed_dictionary = dict(zip(word_to_id.values(), word_to_id.keys()))
    """
    x = (1,2,3)
    y = (a,b,c)
    zip(x,y)
    >>(1,a),(2,b),(3,c)
    """
    print(train_data[:5])
    print(word_to_id)
    print(vocabulary)
    print(" ".join([reversed_dictionary[x] for x in train_data[:10]]))
    return train_data, valid_data, test_data, vocabulary, reversed_dictionary
