'''
A researcher has gathered thousands of news articles. But she wants to focus
her attention on articles including a specific word. Complete the function
below to help her filter her list of articles.

Your function should meet the following criteria:

Do not include documents where the keyword string shows up only as a part of a
larger word. For example, if she were looking for the keyword “closed”, you
would not include the string “enclosed.”
She does not want you to distinguish upper case from lower case letters. So
the phrase “Closed the case.” would be included when the keyword is “closed”
Do not let periods or commas affect what is matched. “It is closed.” would be
included when the keyword is “closed”. But you can assume there are no other
types of punctuation.
'''

doc_list=[
'The Learn Python Challenge Casino',
'They bought a car, and a horse',
'Casinoville?']

signos_puntuacion = ['.', ',', ':']

def word_search(doc_list, keyword):
   
    ind = -1
    respuestas = []
    #-- Itero sobre cada uno de los documentos
    for doc in doc_list:
        ind += 1
        doc_spl = doc.split(' ')
        
        #-- Ahora reviso una por una las palabras en el documento
        for key in doc_spl:
            key1 = ''
            for char in key:
                if char not in signos_puntuacion:
                    key1 += char
            #-- Si contiene exactamente la palabra buscada entonces la guarda en las respuestas
            if keyword.lower() == key1.lower():
                respuestas.append(ind)
                break
    return respuestas
    
print(word_search(doc_list, 'car'))
