
import os
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities
from nltk.corpus import stopwords

os.chdir('/home/amisha/toy_data/')
df=pd.read_csv('output_concat.csv')
x=df['comments'].values.tolist()
corpus= x
job_titles = [nltk.word_tokenize(line.strip().decode('utf-8')) for line in corpus]
filtered_words = [word for word in job_titles if word not in stopwords.words('english')]
print filtered_words
job_titles = [line.decode('utf-8').strip() for line in title_file.readlines()]
print job_titles
tok_corp= [nltk.word_tokenize(sent.decode('utf-8').strip()) for sent in corpus.readlines()]
print tok_corp
model = gensim.models.Word2Vec(job_titles, min_count=10, size = 2000)
model.save('testmodel')
model = gensim.models.Word2Vec.load('testmode',min_count=10, size = 2000)
model.most_similar('good')

