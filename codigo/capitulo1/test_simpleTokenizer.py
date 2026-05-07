from clases.SimpleTokenizerV1 import SimpleTokenizerV1
from clases.SourceText import SourceText

url = (
    "https://raw.githubusercontent.com/rasbt/" 
    "LLMs-from-scratch/main/ch02/01_main-chapter-code/" 
    "the-verdict.txt") 

vocab = SourceText().get(url)

tokenizer = SimpleTokenizerV1(vocab) 
#Correcto
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride.""" 
ids = tokenizer.encode(text) 
print(ids)

'''
#Con error
text = """Hello. Do you like tea?""" 
ids = tokenizer.encode(text) 
print(ids)
'''