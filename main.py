from bio.constantes import DNA_PARA_AMINOACIDO
from bio.sequencia import Sequencia
from bio.organismo_fasta import OrganismoFasta
from bio.ler_fasta import ler_fasta

sequencia="ACGTAGCATAGCAGAT"
S1=Sequencia(sequencia)
print (S1.calcular_percentual(bases=["G", "C"]))


organismo = OrganismoFasta(id="NM00", nome="fulano",sequencia=sequencia)
organismo.mostrar_atributos()

leitura=ler_fasta("arquivos/Flaviviridae-genomes.fasta")
print(len(leitura))

leitura[158].mostrar_atributos()


