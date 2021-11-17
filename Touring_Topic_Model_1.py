import gensim
from gensim import corpora
from pprint import pprint
from gensim.utils import simple_preprocess
from smart_open import smart_open
import os
import argparse
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models import Phrases
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk.corpus import stopwords
import re
from gensim.test.utils import datapath
import logging
from pprint import pprint
import json 

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", dest="input_file", help="input file")
parser.add_argument("--output_file", dest="output_file", help="output file")
parser.add_argument("--output_path", dest="output_path", help="output path")
args = parser.parse_args()
input_file = args.input_file
output_file = args.output_file

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
                                            
tokenizer = RegexpTokenizer('\w+')


with open(input_file, 'r') as text_file:
    dictionary_list = json.load(text_file)

    print(len(dictionary_list))
    document_list = []
    for dict in dictionary_list:
        document = dict["artist"] 
        document_list.append(document)
       
    print(len(document_list))
                                                                                                                                                                                                                                                                                                                                                                                                                              
    dictionary = corpora.Dictionary(document_list)
    #dictionary.filter_extremes(no_below = 20, no_above= 0.5)
    corpus = [dictionary.doc2bow(doc) for doc in document_list]
    print('Number of unique tokens: %d' % len(dictionary))
    print('Number of documents: %d' % len(corpus))

    num_topics = 10
    chunksize = 2000
    passes = 40
    iterations = 400
    eval_every = 1
    temp = dictionary[0]
    id2word = dictionary.id2token
    print('about to model')
    model = LdaModel( corpus=corpus, id2word=id2word,
    chunksize=chunksize,
    alpha='auto',
    eta='auto',
    iterations=iterations,
    num_topics=num_topics,
    passes=passes,
    eval_every=eval_every)

    top_topics = model.top_topics(corpus)
    pprint(top_topics)



    # print(model.print_topics())                                                                                                                                                                                                                                             
   # print('\nPerplexity: ', model.log_perplexity(corpus))                                                                                                                                                                                                                    
   # coherence_model_lda = CoherenceModel(model = model, texts=lem_docs, dictionary=id2word, coherence='c_v')                                                                                                                                                                 
    #coherence_lda = coherence_model_lda.get_coherence()                                                                                                                                                                                                                      
   # print('\nCoherence Score: ', coherence_lda)                                                                                                                                                                                                                              
   #add the if not to check and cut a new file                                                                                                                                                                                                                                
model.save(output_file)

