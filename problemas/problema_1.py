# Problema 1: Análise de Composição de Nucleotídeos
# Tarefa: Escreva um script que:
# 1) Faça o parse do arquivo multiFASTA, usando a função ler_fasta.
# 2) Imprima o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo GC (percentual de C + G) para cada sequência.  
# Dica: Use sua classe Sequencia e sua função .calcular_percentual(bases)
#from bio.constantes import DNA_PARA_AMINOACIDO
from sequencia import Sequencia 
from organismo_fasta import OrganismoFasta
from ler_fasta import ler_fasta
leitura=ler_fasta("arquivos/Flaviviridae-genomes.fasta")
for i in leitura:
    print (i.id)
    print (f"O percentual da base A é:  {i.sequencia.calcular_percentual(["A"])}")
    print (f"O percentual da base T é:  {i.sequencia.calcular_percentual(["T"])}")
    print (f"O percentual da base C é:  {i.sequencia.calcular_percentual(["C"])}")
    print (f"O percentual da base G é:  {i.sequencia.calcular_percentual(["G"])}")
    print (f"O percentual das bases GC é: {i.sequencia.calcular_percentual(["G", "C"])}")



