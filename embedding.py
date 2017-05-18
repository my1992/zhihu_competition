import numpy as np
from gensim.models import Word2Vec

word_vectors = Word2Vec.load_word2vec_format('data/word_embedding.txt', binary=False)  # C text format
char_vectors = Word2Vec.load_word2vec_format('data/char_embedding.txt', binary=False)  # C text format


class Vector(object):
    def __init__(self, chars, words):
        self.chars = chars
        self.words = words

    def chars2vectors(self):
        _vectors = []
        for _c in self.chars:
            if _c in char_vectors.vocab:
                _vectors.append(char_vectors.wv[_c])
            else:
                _vectors.append(np.zeros(256))
        return _vectors

    def words2vectors(self):
        _vectors = []
        for _w in self.words:
            if _w in word_vectors.vocab:
                _vectors.append(word_vectors.wv[_w])
            else:
                _vectors.append(np.zeros(256))
        return _vectors

    def vectors2mat(self, _vectors):
        return np.mat(_vectors)


class Topic2Vector(object):
    def __init__(self, topic_id=None, char_name=None, word_name=None, char_description=None, word_description=None):
        self.topic_id = topic_id
        self.char_name = char_name
        self.word_name = word_name
        self.char_description = char_description
        self.word_description = word_description

    def char_name_vec(self):
        _char_name_vec = np.zeros(256)
        if self.char_name:
            count = 0
            for _c in self.char_name:
                if _c in char_vectors.vocab:
                    count += 1
                    _char_name_vec += char_vectors.wv[_c]
            if count > 0:
                _char_name_vec /= count
        return _char_name_vec

    def word_name_vec(self):
        _word_name_vec = np.zeros(256)
        if self.word_name:
            count = 0
            for _w in self.word_name:
                if _w in word_vectors.vocab:
                    count += 1
                    _word_name_vec += word_vectors.wv[_w]
            if count > 0:
                _word_name_vec /= count
        return _word_name_vec

    def char_description_vec(self):
        _char_description_vec = np.zeros(256)
        if self.char_description:
            count = 0
            for _c in self.char_description:
                if _c in char_vectors.vocab:
                    count += 1
                    _char_description_vec += char_vectors.wv[_c]
            if count > 0:
                _char_description_vec /= count
        return _char_description_vec

    def word_description_vec(self):
        _word_description_vec = np.zeros(256)
        if self.word_description:
            count = 0
            for _w in self.word_description:
                if _w in word_vectors.vocab:
                    count += 1
                    _word_description_vec += word_vectors.wv[_w]
            if count > 0:
                _word_description_vec /= count
        return _word_description_vec

    def topic_vector(self, _char_name_vec=None, _word_name_vec=None, _char_description_vec=None,
                     _word_description_vec=None):
        _vec = np.zeros(256)
        count = 0
        if _char_name_vec:
            count += 1
            _vec += _char_name_vec
        if _word_name_vec:
            count += 1
            _vec += _word_name_vec
        if _char_description_vec:
            count += 1
            _vec += _char_description_vec
        if _word_description_vec:
            count += 1
            _vec += _word_description_vec

        _vec /= count
        return _vec
