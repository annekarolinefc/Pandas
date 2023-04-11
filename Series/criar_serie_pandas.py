# importar a biblioteca
import numpy as np
import pandas as pd 

#Você pode...
# - passar um array como um objeto
# - passar um dicionário python
# - passar um valor escalar

# Criar uma series pandas contendo 8 numeros randomicos de -10 a 10
serie1 = pd.Series(np.random.randint(-10, 11, size=8))
print(serie1)

# Criar uma series pandas contendo 8 numeros randomicos de -10 a 10 passando index
serie2 = pd.Series(np.random.randint(-10, 11, size=8), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(serie2)