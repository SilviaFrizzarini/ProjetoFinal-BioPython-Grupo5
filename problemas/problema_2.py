# Problema 2: Tradução de Sequências de Nucleotídeos para Sequências de Proteínas
# Objetivo: Traduzir sequências de nucleotídeos para sequências de proteínas.
# Tarefa: Escreva um script em Python para:
# Fazer o parse do arquivo multiFASTA.
# Traduzir cada sequência de nucleotídeos para sua sequência de proteína correspondente.
# Imprimir as sequências de proteínas.
# Dica: Use sua classe Sequencia e sua função de traduzir
from sequencia import Sequencia 
from organismo_fasta import OrganismoFasta
from ler_fasta import ler_fasta
leitura=ler_fasta("arquivos/Flaviviridae-genomes.fasta")
for i in leitura:
    print (i.id)
    print (f"A sequencia de aminoácidos é:  {i.sequencia.traduzir()}")
    