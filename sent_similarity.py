sources = ('law-corpus.en')
documents = gensim.models.doc2vec.TaggedLineDocument(sources)
model = gensim.models.doc2vec.Doc2Vec(dm=0, # DBOW
				size=400, 
				window=8, 
				min_count=5,  
				dbow_words = 1) # DBOW, simultaneously train word vectors with doc vectors

# build model
model.build_vocab(documents)
# train model
model.train(documents)
# save
model.save('model-law-corpus-en')

And to compare:

model = gensim.models.doc2vec.Doc2Vec.load('model-law-corpus-en')

st = 'criminal'

new_doc_vec = model.infer_vector(st)

print model.docvecs.most_similar([new_doc_vec])