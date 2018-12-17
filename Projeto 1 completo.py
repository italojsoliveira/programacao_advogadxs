import csv

def ler_clientes(nome_do_arquivo):
    with open(nome_do_arquivo, 'r',encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        lista = list(reader)
        return lista
        

#print(ler_clientes("clientes.csv"))

lista = ler_clientes("clientes.csv")


# cabeçalho / não varia, a não ser na qualificação
cabecalho = '''EXCELENTÍSSIMO SENHOR DESEMBARGADOR PRESIDENTE DO EGRÉGIO TRIBUNAL DE JUSTIÇA DO ESTADO DO RIO DE JANEIRO

{0} (doravante chamado 'paciente'), {2} anos, de nacionalidade brasileira, casado/solteiro, RG nº xxx, CPF yyyy, residente no endereço Rua XYZ, da cidade de {1}, vem respeitosamente à presença de Vossa Excelência, com fundamento no artigo 5º, LXVIII, da Constituição Federal, e com
artigo 647 e seguintes do Código de Processo Penal, impetrar a presente ordem de

“HABEAS CORPUS”, com PEDIDO DE LIMINAR

contra ato da MM. Juíza da (endereçamento DDD), em favor de si mesmo, pelas razões de fato e de direito a seguir expostas:'''

# HC preventivo homicidio
tipo_hc_hom = '''DOS FATOS

O paciente foi acusado de ter praticado crime de homicídio, tipificado no artigo 121 do Código Penal, ocorre que na data de xx/xx/xx, ocasião dos fatos, o paciente estava fora do país em viagem de negócios, conforme faz prova os documentos em anexo (Doc.).

A imprensa local desfavorece o paciente imputando-lhe o fato criminoso, em contradição o que diz o artigo 5º, inciso LVII da Constituição Federal.

A autoridade policial titular do __º distrito policial, inclina-se a idéia da prisão temporária do paciente.

Desse modo, fica caracterizada a grave ameaça do paciente vir sofrer limitação em seu direito de liberdade.'''


# HC preventivo homicidio culposo de trânsito
tipo_hc_trans = '''DOS FATOS

O paciente foi acusado de ter praticado crime de homicídio culposo de trânsito, tipificado no artigo 302 do Código de Trânsito Brasileiro, ocorre que na data de xx/xx/xx, ocasião dos fatos, o paciente estava fora do país em viagem de negócios, conforme faz prova os documentos em anexo (Doc.).

A imprensa local desfavorece o paciente imputando-lhe o fato criminoso, em contradição o que diz o artigo 5º, inciso LVII da Constituição Federal.

A autoridade policial titular do __º distrito policial, inclina-se a idéia da prisão temporária do paciente.

Desse modo, fica caracterizada a grave ameaça do paciente vir sofrer limitação em seu direito de liberdade.'''

# HC preventivo falta de pagamento pensão alimentícia / falta adequar o texto à fundamentação
tipo_hc_pensao = '''DOS FATOS

O paciente foi acusado de ter faltado com o pagamento de pensão alimentícia, correndo o risco de ter prisão civil deferida, pelo art. 528, CPC.
Ocorre que na data de xx/xx/xx, ocasião dos fatos, o paciente estava fora do país em viagem de negócios, conforme faz prova os documentos em anexo (Doc.).
E tem feito os pagamentos corretamente por depósito automático.

A imprensa local desfavorece o paciente imputando-lhe o fato criminoso, em contradição o que diz o artigo 5º, inciso LVII da Constituição Federal.

A autoridade policial titular do __º distrito policial, inclina-se a idéia da prisão temporária do paciente.

Desse modo, fica caracterizada a grave ameaça do paciente vir sofrer limitação em seu direito de liberdade.'''


# parte do direito / não varia
hc_direito = """DO DIREITO

A Constituição Federal, ampara o pleito do paciente em seus artigos 5º, inciso LXVIII, quando diz que:

"Art.5º. Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança, e a propriedade, nos termos seguintes:

LVII - Ninguem será considerado culpado até o trânsito em julgado de sentença penal condenatória;

LXVIII - conceder-se-á habeas corpus sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder;"

O Código de Processo Penal nos seus dispositivos, fala que:

"Art. 654. O habeas corpus poderá ser impetrado por qualquer pessoa, em seu favor ou de outrem, bem como pelo Ministério Público.

§ 1º - A petição de habeas corpus conterá:

b) a declaração da espécie de constrangimento ou, em caso de simples ameaça de coação, as razões em que funda o seu temor;"

"Art.660. Efetuadas as diligências, e interrogado o paciente, o juiz decidirá, fundamentadamente, dentro de 24 (vinte e quatro) horas.

§ 4º - Se a ordem de habeas corpus for concedida para evitar ameaça de violência ou coação ilegal, dar-se-á ao paciente salvo-conduto assinado pelo juiz."

Informo a Vossa Excelência, que o paciente é casado, tem filhos, trabalho fixo e residência fixa, fazendo prova pelos documentos anexados (docs.).

Assim fica demonstrado que o paciente idôneo, possuindo excelente conduta social, nunca tendo sido processado anteriormente.

"""

# PEDIDO preventivo

hc_pedido_prev = '''PEDIDO

Por todo o exposto, tendo provado a procedência de seu justo receio, requer à Vossa Excelência, a expedição de salvo conduto, preservando o direito fundamental da liberdade física do paciente, nos termos do artigo 660, §4°, do Código de Processo Penal, sendo feitas as comunicações necessárias à ilustre autoridade coatora e à a autoridade judiciária de plantão, tudo por ser de JUSTIÇA.

Nestes termos

Pede deferimento

{1}, data, 2018

{0}'''


# HC liberatório homicídio ou culposo trânsito ou pensão

hc_lib = """O paciente encontra-se preso desde o dia (data ), por força da prisão temporária sob a acusação de {4}, por 30 dias, decretada pela Excelentíssima Juíza da (xxª) Vara Criminal do Juízo Regional de (xxxxx), sendo, posteriormente, renovada a prisão preventiva em (data) pelo Excelentíssimo Juiz da (xxª) Vara Criminal do Juízo Regional de (Estado).

Ocorre que, da data da prisão do paciente, até a presente, transcorreram mais de 106 dias, tendo a autoridade coatora, por essa razão, excedido o prazo da instrução criminal, há muito deveria ter sido findado."""



hc_pedido_lib = """Ante ao acima exposto, espera a impetrante, que se faça cessar imediatamente o constrangimento ilegal, pelo qual está passando o paciente, concedendo-lhe a ordem de "HABEAS CORPUS" com a restituição da sua liberdade, através da expedição urgente do competente alvará de soltura.

Tudo por ser de merecida e salutar justiça.

Nestes termos

Pede deferimento

{1}, data, 2018

{0}"""


# def habeas_corpus(nome, cidade, idade, tipo, crime): recebe o nome, cidade , idade, tipo, crime e retorna o texto do HC
   
#for nome, cidade, idade, tipo, crime in lista:   

def habeas_corpus(nome, cidade, idade, tipo, crime):    
    
    texto_hc = cabecalho.format(nome, cidade, idade, tipo, crime)
    
    if tipo == 'preventivo':
        
        if crime == 'homicídio':
            
            texto_hc = texto_hc + tipo_hc_hom
        
        elif tipo == 'homicídio culposo de trânsito':
            
            texto_hc = texto_hc + tipo_hc_trans
        
        elif tipo == 'falta de pagamento de pensão alimnentícia':
            
            texto_hc = texto_hc + tipo_hc_pensao                                       
        
        texto_hc = texto_hc + hc_direito
        
        texto_hc = texto_hc+ hc_pedido_prev.format(nome, cidade, idade, tipo, crime)
        
    else:
        
        texto_hc = texto_hc + hc_lib.format(nome, cidade, idade, tipo, crime)
        texto_hc = texto_hc + hc_direito
        texto_hc = texto_hc + hc_pedido_lib.format(nome, cidade, idade, tipo, crime)
    
    
    
    return texto_hc
  
#print(texto_hc)


def salva_habeas_corpus(nome, idade, tipo, texto_hc):
       
    f = open('{} - {} - {}.txt'.format(tipo, nome, idade), 'w+',encoding="utf-8-sig")
    
    texto = f.write(texto_hc)
    
    f.close()
    
    
for nome, cidade, idade, tipo, crime in lista:
    
    texto_hc = habeas_corpus(nome, cidade, idade, tipo, crime)
    
    
    
    #print(texto_hc)
    
    salva_habeas_corpus(nome, idade, tipo, texto_hc)