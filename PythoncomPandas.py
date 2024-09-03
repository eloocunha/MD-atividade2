import pandas as pd
import ast

import pandas as pd
import ast


filmes_df = pd.read_csv('tmdb_5000_movies.csv')
creditos_df = pd.read_csv('tmdb_5000_credits.csv')


print(filmes_df.head())
print(creditos_df.head())


creditos_elenco = creditos_df[['title', 'cast']]
print(creditos_elenco.head())

def obter_primeiro_ator(elenco):
    try:
        
        lista_elenco = ast.literal_eval(elenco)
        if lista_elenco:
            return lista_elenco[0]['name']
        else:
            return None
    except:
        return None

creditos_elenco['primeiro_ator'] = creditos_elenco['cast'].apply(obter_primeiro_ator)

resultado = creditos_elenco[['title', 'primeiro_ator']]
print(resultado.head(10))
