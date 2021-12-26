
#%%
from collections import Counter

with open('biblia-em-txt.txt', 'r', encoding = "utf8") as f:
    texto = f.read()
#print(texto)

ocorrencia = Counter([palavra.lower() for palavra in texto.split(' ')])
ocorrencia.most_common(1000)


#%%

ocorrencia['senhor']