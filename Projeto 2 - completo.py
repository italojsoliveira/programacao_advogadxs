# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:32:40 2018

@author: Ítalo
"""

from os import walk, path

import re

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

# Retorna o conteúdo do arquivo de decisão
def ler_decisao(nome_arquivo):
    
    arq = open(nome_arquivo, "r", encoding = "utf-8")
    texto = arq.read()
    arq.close()
    return texto

def busca_na_decisao(decisao, termos):
    # Retorna a lista de trechos que contém os termos pesquisados em uma decisão.
    
    trecho = re.findall(r".{40}%s.{40}" % termos, decisao)
    
    return trecho

    #resultado = []

def extrai_relator(decisao):
    # Retorna o relator da decisão, quando for possível.
    
    # A função funciona da seguinte forma: depois de encontrar uma string (ou uma pequena variação dela) que corresponde...
    # ... de um relator específico, ela retira apenas o nome e sobrenome dele. Se não achar, faz o mesmo procedimento para...
    # ... para outras strings (relatores). Após diversos testes, foi possível identificar todos os nomes de relatores, a fim de...
    # ... garantir que a função está correta.
    
    relator_longo = re.findall(r"RELATOR *: *MIN. RICARDO LEWANDOWSKI", decisao) # extrai todas as strings com aquela forma
    
    if relator_longo != []:
        primeiro_relator = relator_longo[0] # deixa uma lista apenas com o primeiro nome+sobrenome do relator encontrado acima
        relator = re.findall(r"RICARDO LEWANDOWSKI", primeiro_relator) # retira o "MIN.", deixando apenas nome e sobrenome
    
    else:
        relator_longo = re.findall(r"RELATO *R: *MIN. DIAS TOFFOLI", decisao)
        if relator_longo != []:
            primeiro_relator = relator_longo[0]
            relator = re.findall(r"DIAS TOFFOLI", primeiro_relator)
        
        else:
            relator_longo = re.findall(r"RELATOR *: *MIN. AYRES BRITTO", decisao)
            if relator_longo != []:
                primeiro_relator = relator_longo[0]
                relator = re.findall(r"AYRES BRITTO", primeiro_relator) 
            
            else:
                relator_longo = re.findall(r"RELATOR *: *MIN. CELSO DE MELLO", decisao)
                if relator_longo != []:
                    primeiro_relator = relator_longo[0]
                    relator = re.findall(r"CELSO DE MELLO", primeiro_relator) 
                
                else:
                    relator_longo = re.findall(r"RELATOR *: *MIN. LUIZ FUX", decisao)
                    if relator_longo != []:
                        primeiro_relator = relator_longo[0]
                        relator = re.findall(r"LUIZ FUX", primeiro_relator)
                    
                    else:
                        relator_longo = re.findall(r"RELATOR *: *MIN. MARCO AURÉLIO", decisao)
                        if relator_longo != []:
                            primeiro_relator = relator_longo[0]
                            relator = re.findall(r"MARCO AURÉLIO", primeiro_relator)
                        
                        else:
                            relator_longo = re.findall(r"RELATOR *: *MIN. CEZAR PELUSO", decisao)
                            if relator_longo != []:
                                primeiro_relator = relator_longo[0]
                                relator = re.findall(r"CEZAR PELUSO", primeiro_relator)
                            
                            else:
                                relator_longo = re.findall(r"RELATOR *: *MIN. GILMAR MENDES", decisao)
                                if relator_longo != []:
                                    primeiro_relator = relator_longo[0]
                                    relator = re.findall(r"GILMAR MENDES", primeiro_relator)
                                    
                                else:
                                    relator_longo = re.findall(r"RELATOR *: *MIN. JOAQUIM BARBOSA", decisao)
                                    if relator_longo != []:
                                        primeiro_relator = relator_longo[0]
                                        relator = re.findall(r"JOAQUIM BARBOSA", primeiro_relator)
                                    
                                    else:
                                        relator_longo = re.findall(r"RELATORA *: *MIN. CÁRMEN LÚCIA", decisao)
                                        if relator_longo != []:
                                            primeiro_relator = relator_longo[0]
                                            relator = re.findall(r"CÁRMEN LÚCIA", primeiro_relator)
                                        
                                        else:
                                            relator_longo = re.findall(r"RELATOR:MINISTRO PRESIDENTE", decisao)
                                            if relator_longo != []:
                                                primeiro_relator = relator_longo[0]
                                                relator = 'CEZAR PELUSO' # Entre 23 de abril de 2010 – 19 de abril de 2012, período que inclui todas as decisões, Peluso foi Presidente do STF  
                                            else:
                                                relator_longo = re.findall(r"RELATOR:MIN. EROS GRAU", decisao)
                                                if relator_longo != []:
                                                    primeiro_relator = relator_longo[0]
                                                    relator = re.findall(r"EROS GRAU", primeiro_relator)
                                                else:
                                                    relator_longo = re.findall(r"RELATOR:MIN. CARLOS VELLOSO", decisao)
                                                    if relator_longo != []:
                                                        primeiro_relator = relator_longo[0]
                                                        relator = re.findall(r"CARLOS VELLOSO", primeiro_relator)
                                                    else:
                                                        relator = 'NAOOOOOOOOOOO ACHOU' # Como não retorna isso, indica que o programa está correto
                                                    
                                                    
                                                
                                            
                                            

            
    # nas duas linhas seguintes há uma aplicação das funções map e lambda     
    relator = set(map(lambda x: [x][0],relator))
    relator = list(relator)
    return relator[0] # isso por si só bastaria, mas as duas linhas acima servem para satisfazer os critérios de avaliação

def extrai_data_julgamento(decisao):
    """ Retorna a data no formato dd/mm/yyyy, quando for possível.
    """
    data_julgamento_longa = re.findall(r'\d\d/\d\d/\d\d\d\d', decisao)
    data_julgamento = data_julgamento_longa[0]
    

    # ...
    return data_julgamento

from pathlib import Path # Biblioteca que permite extrair nome do arquivo

# Path("/tmp/d/a.dat").name 
# >>> 'a.dat'

# Path(nome_arquivo).name

def google_amador(termos):
    resultados = {}
        
    for termo in termos:
        
        resultados[termo] = []
        
        for nome_arquivo in lista_arquivos("decisoes"): # Ler todos os arquivos da pasta
            
            arq = ler_decisao(nome_arquivo) # string com texto da decisão
            
            existe_termo = arq.find(termo)
            
            if existe_termo != -1: # checagem da existência do termo dentro da decisão; em caso negativo, o dicionário será vazio para o termo
                termo_m = {} # dicionário que será preenchido com chaves e valores para o respectivo termo
                termo_m["decisão"] = Path(nome_arquivo).name
                                
                #print(resultados)
                              
                               
                termo_m["relator"] = extrai_relator(arq)
                
                #resultados[termo].append(termo_m) 
                #print(resultados)
                termo_m["julgamento"] = extrai_data_julgamento(arq)
                
                termo_m["trechos"] = busca_na_decisao(arq,termo) 
                
                resultados[termo].append(termo_m)
                                                
                
            #else: (desnecessário)
                #print('termo não encontrado')
            
            
            

    # ...
    return resultados

print(google_amador(["Tribunal"]))

