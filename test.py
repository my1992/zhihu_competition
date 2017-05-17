from gensim.models import Word2Vec

word_vectors = Word2Vec.load_word2vec_format('data/word_embedding.txt', binary=False)  # C text format
print(list(word_vectors.vocab)[0:10])
