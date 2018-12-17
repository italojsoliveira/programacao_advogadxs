# -*- coding: utf-8 -*-

"""
Problema 2

Programar uma função que recebe uma lista de strings (palavras ou expressões
compostas) e devolve um dicionário com o número de ocorrências de cada uma
delas, juntamente com uma tupla (para cada uma das string procuradas) contendo:
 - A identificação da decisão;
 - A data de Julgamento;
 - O nome do relator, se houver;
 - O trecho que contém o termo -- 40 caracteres antes e 40 depois.

A busca será feita dentro de uma coleção de decisões. A função terá que acessar
uma pasta chamada 'decisoes' contendo 1500 decisões do STF em formato .txt, que
estará no mesmo diretório do arquivo .py. 

A entrada da função será uma lista de termos:

 - Exemplo: ['artigo 557 do Código de Processo Civil', 'tentativa de furto']

O retorno da função terá o formato descrito no exemplo:


{
    'artigo 557 do Código de Processo Civil':[
        {
            "decisão": "res12.txt",
            "relator": "MARCO AURÉLIO",
            "julgamento": "04/11/2001",
            "trechos": 
                [
                    " aplicação da multa prevista no § 2º do artigo 557 do Código de Processo Civil, arcando a parte com o ônus decorrente ",
                ]
        },
        {
            "decisão": "res65.txt",
            "relator": "AYRES BRITTO",
            "julgamento": "06/10/2003",
            "trechos": 
                [
                    " aplicação da multa prevista no § 2º do artigo 557 do Código de Processo Civil, arcando a parte com o ônus decorrente ",
                ]
        }
    ],
    'tentativa de furto':[
        {
            "decisão": "res21.txt",
            "relator": "AYRES BRITTO",
            "julgamento": "26/03/2011",
            "trechos": 
                [
                    "".957 / RS necessário saber se a alegada tentativa de furto de algumas bijuterias, avaliadas em R$ "",
                ]
        }
    ]
}

Um arquivo zip contendo a pasta com as decisões está disponível em:
 - https://goo.gl/4cYE2s

o conjunto de stopwords está no arquivo stopwords_pt.txt disponível em:
 - https://goo.gl/17eWNR

* Stopwords são palavras que podem ser consideradas irrelevantes para o conjunto
de resultados a ser exibido em uma busca, como por exemplo: "a", "um", "uma",
"de", "com" e etc.

Critérios de avaliação:

 - A função principal deve se chamar "google_amador" e tanto input quanto
   output devem seguir o formato especificado;
 - Outras quatro funções devem ser implementadas: ler_decisao, busca_na_decisao,
   extrai_relator, extrai_data_julgamento;
 - Devem ser utilizadas pelo menos 2 dessas funções: lambda, map, zip, filter,
   reduce, any e all;
 - É Imprescindível que o código esteja bem organizado e com comentários.
"""


def google_amador(termos):
    resultados = {}

    # ...
    return resultados


# BONUS!
def lista_arquivos(nome_diretorio):
    """ 
    Esta função acessa um diretório (nome_diretorio), coleta o nome de todos
    os arquivos presentes, seleciona apenas aqueles que são .txt e retorna uma
    lista com o caminho para a leitura de todos os arquivos.

    """
    nomes = []  # guarda aquilo que será retornado

    # entrando no diretório
    for raiz, diretorios, arquivos in walk(nome_diretorio):
        # listando arquivos
        for arquivo in arquivos:

            # verificando se o arquivo tem o '.txt' no nome
            if arquivo.endswith(".txt"):
                nomes.append(path.join(raiz, arquivo))

    return nomes


def ler_decisao(nome_arquivo):
    """ Retorna o conteúdo do arquivo de decisão.
    """
    conteudo = ''

    # ...
    return conteudo


def busca_na_decisao(decisao, termos):
    """ Retorna a lista de trechos que contém os termos pesquisados em uma decisão.
    """
    resultado = []
    
    # ...
    return resultado


def extrai_relator(decisao):
    """ Retorna o relator da decisão, quando for possível.
    """
    relator = ''

    # ...
    return relator


def extrai_data_julgamento(decisao):
    """ Retorna a data no formato dd/mm/yyyy, quando for possível.
    """
    data_julgamento = ''

    # ...
    return data_julgamento
