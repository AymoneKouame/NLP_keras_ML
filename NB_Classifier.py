from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ('Great company and office environment!', 'pos'),
    ('the opportunity is here', 'pos'),
    ('Great place to work!', 'pos'),
    ('Not just a job, we are a family', 'pos'),
    ("great teamwork environment and plenty of opportunity to grow!", 'pos'),
    ('Weak management support', 'neg'),
    ('Lack of communication between management and employees is not the best', 'neg'),
    ("Not much room to advance", 'neg'),
    ('Very strict late policy no matter the weather conditions', 'neg'),
    ('My boss is horrible.', 'neg')
]
test = [
    ('Personally I like the job itself', 'pos'),
    ('Too large and slow to keep up with modern tech advancements', 'neg'),
    ("Zero work life balance", 'neg'),
    ("Excellent opportunities for people who want to move up, quickly", 'pos'),
    ('Great pay package', 'pos'),
    ("Bureaucracy too long to make decisions", 'neg')
]
cl = NaiveBayesClassifier(train)
file=open("all_reviews.txt")
t=file.read()
t = t.decode("utf8")
blob = TextBlob(t, classifier=cl)
print(blob.classify())
for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())
print("Accuracy: {0}".format(cl.accuracy(test)))
cl.show_informative_features(5)
