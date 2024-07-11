# Classe Sequencia
# Esta classe vai ser a principal do projeto e vai conter as funcionalida de sequencia.
# Ela deve ter pelo menos um atributo que é a própria Sequencia.
# Essa classe deve ter os seguintes métodos:
# .complementar() - Inspirado no método Seq().complement()
# Retorna outro objeto sequencia, com a sequencia complementar.
# .complementar_reversa() - Inspirado no método Seq.reverse_complement()
# Retorna outro objeto sequencia, com a sequencia complementar reversa.
# .transcrever - Inspirado no método Seq.transcribe()
# Retorna outro objeto sequencia, com a sequencia resultado da transcricao daquela sequencia.
from constantes import DNA_PARA_AMINOACIDO
class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(index)

    def mostrar_complementar (self):
      sequencia_complementar=""
      base_complementar={"A":"T", "T":"A", "C":"G", "G":"C"}
      for base in self.sequencia:
        sequencia_complementar=sequencia_complementar+base_complementar[base]
      return sequencia_complementar

    def mostrar_complementarreversa (self):
      sequencia_complementar=""
      base_complementar={"A":"T", "T":"A", "C":"G", "G":"C"}
      for base in self.sequencia:
        sequencia_complementar=sequencia_complementar+base_complementar[base]
      return sequencia_complementar [::-1]

    def transcrever (self):
      sequencia_complementar=""
      base_complementar={"A":"T", "T":"U", "C":"G", "G":"C"}
      for base in self.sequencia:
        sequencia_complementar=sequencia_complementar+base_complementar[base]
      return sequencia_complementar

# .traduzir(parar=False) - Inspirado no método Seq().translate()
# Retorna uma string com a tradução da sequencia para uma proteína.
# Exemplo: "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG" -> "MAIVMGRKGAR"
# Essa função receberá um argumento parar. Se ele for true, sua tradução deve parar no stop codon. 
# Se parar=False, deve continuar e marcar os stop códons como * e varrer até o final.
# Para fazer essa função, está disponibilizado um dicionário no arquivo constantes.py DNA_PARA_AMINOACIDO que você pode importar.
# Caso a trinca de codon não esteja nesse dicionário, é porque a sequencia tem uma base indefinida. Nessa caso, marque a proteína como X, indicando que não tem como sabe-la.

    def traduzir (self, parar=False):
          stop_codons = ["TAA", "TAG", "TGA"]
          if parar: #significa que parar=True
            sequence_length = len(self.sequencia)
            start_index = self.sequencia.find("ATG")
            for i in range(start_index, sequence_length, 3):
              codon = self.sequencia[i:i+3] #mesmo que 1a base[i]+2a base[i+1]+3a base [i+2], vai até i+3 porque exclui o 3
              if codon in stop_codons:
                traducao=""  
                for j in range(start_index, i, 3):
                  codon = self.sequencia[j:j+3]
                  if codon in DNA_PARA_AMINOACIDO.keys(): 
                    traducao=traducao+DNA_PARA_AMINOACIDO[codon]
                  else:
                    traducao=traducao+"X"
                return traducao
          else: #ou seja, se parar=False
            for codon in stop_codons:
              nova_sequencia = self.sequencia.replace(codon,"***")
            sequence_length = len(nova_sequencia)
            start_index = nova_sequencia.find("ATG")
            traducao=""
            for i in range(start_index, sequence_length, 3):
              codon = nova_sequencia[i:i+3] 
              if codon in DNA_PARA_AMINOACIDO.keys(): 
                traducao=traducao+DNA_PARA_AMINOACIDO[codon]
              elif codon=="***":
                traducao=traducao+"*"    
              else:
                traducao=traducao+"X"
            return traducao
              
# .calcular_percentual(bases)
# Ex: Sequencia("ATCGAAA").calcular_percentual(bases=["A"]) = 0.5 (pois há 4 As num total de 8 bases)
# Esse método foi inventado. Ele vai receber uma lista de bases e calcular o percentual daquelas bases na composição da Sequencia.
# Ex: Sequencia("ATCGAAA").calcular_percentual(bases=["A"]) = 0.5 (pois há 4 As num total de 8 bases)
# Ex: Sequencia("ATCGCC").calcular_percentual(bases=["C", "G"]) = 0.66 (pois há 4 Cs e Gs num total de 8 bases)

    def calcular_percentual(self,bases):
       base_A=0
       base_G=0
       base_T=0
       base_C=0
       for i in self.sequencia:
          if i=="A":
             base_A=base_A+1
          elif i=="G":
             base_G=base_G+1
          elif i=="T":
             base_T=base_T+1
          elif i=="C":
             base_C==base_C+1
       percentual_A=base_A/len(self.sequencia)
       percentual_G=base_G/len(self.sequencia)
       percentual_T=base_T/len(self.sequencia)
       percentual_C=base_C/len(self.sequencia)
       soma_bases=0
       for j in bases:
          if j=="A":
            soma_bases=soma_bases + percentual_A
          elif j=="T":
             soma_bases=soma_bases + percentual_T
          elif j=="C":
             soma_bases=soma_bases+percentual_C
          elif j=="G":
             soma_bases=soma_bases+percentual_G
       return soma_bases
    
# sequencia="ACGTAGCATAGCAGAT"
# S1=Sequencia(sequencia)
# print (S1.calcular_percentual(bases=["G", "C"]))


