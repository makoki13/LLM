import re
import urllib.request 

class SourceText:
    def get(self,url):
        file_path = "temp.txt" 
        urllib.request.urlretrieve(url, file_path)

        with open("temp.txt", "r", encoding="utf-8") as f: 
            raw_text = f.read() 
        #pendiente: Borrar fichero temp.txt

        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text) 
        preprocessed = [item.strip() for item in preprocessed if item.strip()] 

        all_tokens = sorted(list(set(preprocessed))) 
        all_tokens.extend(["<|endoftext|>", "<|unk|>"])

        vocab = {token:integer for integer,token in enumerate(all_tokens)} 

        return vocab

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
    for i, item in enumerate(vocab.items()): 
        print(item) 
        if i >= 50: 
            break