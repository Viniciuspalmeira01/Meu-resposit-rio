tabela = {'*Bahia':20.5 , '*Acre':19 , '*Amazonas':20 ,'*Alagoas':19 ,'*Amapá':18 ,'*Ceará':20 ,'*Rio Grande do Norte':18,
    '*DF':20 ,'*Espírito Santo':17 , '*Goiás ':19, '8Maranhão ':22 , '*Mato Grosso':17 ,'*Mato Grosso do Sul':17,
    '*Minas Gerais':18, '*Pará ':19 ,'*Paraíba ':20,'*Paraná ':19.5, '*Pernambuco':20.5, '*Piauí ':21, '*Rio de Janeiro':22,
    '*Rio Grande do Sul':17 ,'*Rondônia ':19.5 ,'*Roraima ':20 ,'Santa Catarina ':17, 'São Paulo ':18, 'Sergipe':19 ,'Tocantins':20}
class Cont():
     def __init__(self) -> None:
         self.index =0
         pass
     def CSLL(self, receita, percentual_presunção , aliquota):
         info = 'Fórmula: CSLL = Receita Bruta * Percentual de Presunção * Alíquota CSLL'
         
         return receita * percentual_presunção * aliquota
     
     def analise(self, lucro,tempo):
          media = float(lucro/tempo)
          if media >10.0 :
               print(f'você tem uma {media} por mês')
          else: 
               print('Você está abaixo da média')
     def Lucro (self,x , y):
          int(x)
          int(y)
          return x - y    

class Tax():
    def __init__(self) -> None:
        self.index = 0
        self.info = 'Tabela ICMS transporte interestadual e intermunicipal: dados de 2024'
        self.salario = float(1.320)
    def aliquotas (self, value):
        for valor in tabela.items():
            print(valor)
            
    def Icms(self,values , origem):

        if origem == tabela['Bahia']:
            values = values * 20.5 /100
        elif origem == tabela['Acre']:
             values = values * 19 /100
        elif origem == tabela ['Rio de Janeiro']:
              values = values * 22 /100
        elif origem == tabela['Alagoas']:
             values = values * 19 /100
        elif origem == tabela['Amapá']:
             values = values * 18 /100
        elif origem == tabela['Amazonas']:
            values = values * 20 /100 
        elif origem == tabela['Ceará']:
             values = values * 20 /100
        elif origem == tabela['Rio Grande do Norte']:
             values = values * 18 /100
        elif origem == tabela['Rio Grande do Sul']:
             values = values * 17 /100   
        elif origem == tabela['Rondônia ']:
             values = values * 19.5 /100   
        elif origem == tabela['Roraima ']:
             values = values * 20 /100
        elif origem == tabela['Pernambuco']:
             values = values * 20.5 /100 
        elif origem == tabela['Pará ']:
             values = values * 19 /100
        elif origem == tabela['DF']:
             values = values * 20 /100
        elif origem == tabela['Espírito Santo']:
             values = values * 17 /100
        elif origem == tabela['Goiás ']:
             values = values * 19 /100
        elif origem == tabela['Maranhão ']:
             values = values * 22 /100
        elif origem == tabela['Mato Grosso do Sul']:
             values = values * 17 /100
        elif origem == tabela['Mato Grosso']:
             values = values * 17 /100
        elif origem == tabela['Minas Gerais']:
             values = values * 18 /100
        elif origem == tabela['Paraíba ']:
             values = values * 20 /100
        elif origem == tabela['Piauí ']:
             values = values * 21 /100
        elif origem == tabela['Paraná ']:
             values = values * 19.5 /100
        elif origem == tabela['Santa Catarina ']:
            values = values * 17 /100
        elif origem == tabela['São Paulo ']:
             values = values * 18 /100
        elif origem == tabela['Sergipe']:
             values = values * 19 /100
        elif origem == tabela['Tocantins']:
             values = values * 20 /100
        else:
             print('erro')    

        return values
    
    def Pis(self, values):
        result = values * 1.65 / 100
        return result
    def Cofins(self, values):
         result = values * 7.6 /100
         return result
    def pasep(self, value):
        result = value /0.12
        return result
    def Importation(self,value):
         result = value * 60 / 100
         return result
    def IPI(self, values):
         values = values * 25 / 100
         return values
    def IPTU(self, size_house, size_value, aliquota):
         metro_quadrado = float(size_house * size_value)
         result = metro_quadrado * aliquota
         return result
    def ISS(self, values, aliquota):
         result = values * aliquota /1.0
         return result