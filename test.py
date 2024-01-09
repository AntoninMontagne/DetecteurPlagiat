from src.algo.classification.bayes.Bayes import *
from src.corpus.DBInterface import ScrapDatabase


db = ScrapDatabase()
test, train = db.getTestTrainCorpus()

bayes = Bayes(test, test[0].text_article)

author = bayes.chooseClass(option=1)
print(bayes.mostUsedWords(author, option=1))