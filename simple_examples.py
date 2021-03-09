# encoding: utf-8
# author: Geoff Liang
# time: 2021/3/9

# import class
from stanfordcorenlp import StanfordCoreNLP

sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'

# load jar from stanford corenlp path
# memory default is '4g', we set it as '8g'
nlp = StanfordCoreNLP(r'stanford-corenlp-4.2.0', 
                    memory='8g',
                    lang='en',
                    quiet=True)

print("Sentence:", sentence)
# word tokenizer
print("Tokenize:", nlp.word_tokenize(sentence))

print("Part of Speech:", nlp.pos_tag(sentence))

print("Name Entities:", nlp.ner(sentence))

print("Constituency Parsing:", nlp.parse(sentence))

print('Dependency Parsing:', nlp.dependency_parse(sentence))
# server should be closed 
nlp.close()