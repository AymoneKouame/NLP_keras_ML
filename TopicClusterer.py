import csv

# First, tokenize text by sentence to obtain a list of sentences
raw_sentences = nltk.sent_tokenize(raw_text)

# Second, clean each sentence in the list (recall CleanSentences())and append all sentences as corpus
corpus = []
for sent in list(raw_sentences):
    clean_sentence = CleanSentences(sent)
    corpus.append(clean_sentence)
    
# Third, tokenize words in each sentence, creating a bag-of-words per sentence
Corpus = [c.split() for c in corpus]

# Prepare data for modeling
import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(Corpus)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(d) for d in Corpus]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Train an LDA model on the document term matrix (we will set topic number at 10).
ntopics = 10
ldamodel = Lda(doc_term_matrix, num_topics=ntopics, id2word = dictionary, passes=50)
