import gensim


def average_word2vec(word):
    model_file_name = "idwiki_word2vec_200.model"
    model = gensim.models.Word2Vec.load(model_file_name)
    sum = 0
    vals = []
    # ini jangan lupa di cek. ada kata yang gak ada di word2_vec
    if word in model.wv.vocab:
        vals = model.wv.__getitem__(word)

    for val in vals:
        sum += val

    sum /= max(1, len(vals))
    return sum
