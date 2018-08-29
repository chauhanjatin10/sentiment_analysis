from nltk import tokenize
from nltk import pos_tag, word_tokenize, ne_chunk
from nltk.tree import Tree
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class NER:
	def __init__(self):
		self.text = text

	def extract_named_entities(self):
		named_entiites = []
		for chunk in ne_chunk(pos_tag(word_tokenize(self.text))):
			if type(chunk) == Tree:
				named_entiites.append(' '.join(c[0] for c in chunk))
		return named_entiites


class Sentiment:
	def __init__(self, text):
		self.text = text
		self.analyser = SentimentIntensityAnalyzer()

	def sentiment_polarity(self):
		with open('sentiment.txt', 'w') as f:
			for paragraph in self.text:
				for line in paragraph[:-1]:
					f.write(line + ' -> analysis - ')
					ss = self.analyser.polarity_scores(line)
					for k in sorted(ss):
						f.write('{0}: {1} , '.format(k, ss[k]))
					f.write('\n')
				f.write('\n')
				






