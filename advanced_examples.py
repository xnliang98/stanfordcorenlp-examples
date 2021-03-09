# encoding: utf-8
# author: Geoff Liang
# time: 2021/3/9

# import class
from stanfordcorenlp import StanfordCoreNLP


text = 'Guangdong University of Foreign Studies is located in Guangzhou. ' \
       'GDUFS is active in a full range of international cooperation and exchanges in education. '



# load jar from stanford corenlp path
# memory default is '4g', we set it as '8g'
nlp = StanfordCoreNLP(r'stanford-corenlp-4.2.0', 
                    memory='8g',
                    lang='en',
                    quiet=True) # if you want to debug, you need to set quiet=False
# Details of annotators: https://stanfordnlp.github.io/CoreNLP/annotators.html
props={
    'annotators': 'tokenize,ssplit,pos', # tokenize, split sentence, part of speech
    'pipelineLanguage': 'en', # english
    'outputFormat': 'json' # xml
    }
print(nlp.annotate(text, properties=props))

nlp.close()