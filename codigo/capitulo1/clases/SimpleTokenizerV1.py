import re
from codigo.capitulo1.clases.sourcetextv1 import SourceText

class SimpleTokenizerV1:
    def __init__(self, vocab) -> None:
        self.str_to_int = vocab
        self.int_to_str = {i:s for s, i in vocab.items()}

    def encode(self,text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    
    def decode(self,ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
if __name__ == "__main__":
    """
    Bloque de ejecución directa:
    - Pruebas rápidas de desarrollo
    - Demostración de uso de la clase
    - No se ejecuta al importar el módulo
    """
    url = (
        "https://raw.githubusercontent.com/rasbt/" 
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/" 
        "the-verdict.txt") 

    vocab = SourceText().get(url)

    tokenizer = SimpleTokenizerV1(vocab) 
    text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride.""" 
    ids = tokenizer.encode(text) 
    print(ids)