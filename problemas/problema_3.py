# ## Problema 3: Identificação de Mutação em Genomas Virais
# #### Contexto
# Você está colaborando com uma equipe de virologistas que está estudando mutações específicas em genomas de vírus da família 
# Flaviviridae. Eles identificaram uma mutação de interesse que ocorre na posição 1000 das sequências, onde o nucleotídeo 'A' 
# é substituído por 'G'. Seu trabalho é identificar se essa mutação está presente nas sequências fornecidas e gerar um relatório. 
# Esta análise é crucial para entender a evolução dos vírus e suas possíveis implicações na virulência e resistência a tratamentos.
# #### Objetivo
# Aprender a usar Python para procurar mutações específicas em sequências de DNA e gerar relatórios detalhados.
# ### Tarefa - Fazer script que:
# 1. Faça o parse do arquivo multiFASTA contendo os genomas virais.
# 2. Verifique se a mutação específica (substituição de nucleotídeo) na posição 1000 está presente em cada sequência.
# 3. Gerar um relatório que indique quais sequências possuem a mutação e quais não possuem.
from sequencia import Sequencia 
from organismo_fasta import OrganismoFasta
from ler_fasta import ler_fasta
leitura=ler_fasta("arquivos/Flaviviridae-genomes.fasta")
lista_de_ID_A=[]
lista_de_ID_G=[]
for i in leitura:
    if i.sequencia.sequencia[1000] == "A":
        lista_de_ID_A.append(i.id)
    elif i.sequencia.sequencia[1000] == "G":
        lista_de_ID_G.append(i.id)
print (f"Os organismos com a base A na posição 1000 são: {lista_de_ID_A}")
print (f"Os organismos com a base G na posição 1000 são: {lista_de_ID_G}")


