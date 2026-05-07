import re 
text = "Hello, world. This, is a test." 

#separa con espacios
result = re.split(r'(\s)', text) 
print(result)

#separa con espacios, comas y puntos
result = re.split(r'([,.]|\s)', text) 
print(result)

#elimina espacios en blanco
result = [item for item in result if item.strip()] 
print(result)

#incluye otros caracteres como :;?_!()
text = "Hello, world. Is this-- a test?" 
result = re.split(r'([,.:;?_!"()\']|--|\s)', text) 
result = [item.strip() for item in result if item.strip()] 
print(result)