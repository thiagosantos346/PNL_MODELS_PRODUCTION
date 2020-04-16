from . import word2vec_predict

def test_word2vec_predict():
    assert word2vec_predict.apply("Jane") == "hello Jane"
