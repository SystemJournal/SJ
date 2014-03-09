#coding: utf-8

class Usuario:
    def __init__(self, uid, nome, cpf, email, listaDeAvaliacao=[]):
		self.uid = uid
		self.nome = nome
		self.cpf = cpf
		self.email = email
		self.listaDeAvaliacao = listaDeAvaliacao
    
    def inserirAvaliacao(self, avaliacao):
        self.listaDeAvaliacao.append(avaliacao)
	
    def verificarAvaliacao(self, avaliacao):
        return avaliacao in self.listaDeAvaliacao
    #verifica a media geral do usuario, quanto ele gasta em media quando sai a noite?

    def verificarMediaDeConsumo(self):
        total = 0.0
        divisor = 0.0
        for x in xrange(len(self.listaDeAvaliacao)):
            total += self.listaDeAvaliacao[x].precoTotal
            print total
            divisor += 1.0
            media = total / divisor
        return media

class Critico:
    def __init__(self, uid, nome, cargo, email, listaderesenha=[]):
        self.uid = uid
        self.nome = nome
        self.cargo = cargo
        self.email = email
        self.listaderesenha = listaderesenha

    def inserirResenha(self, resenha):
	    self.listaderesenha.append(resenha)

    def verificarResenha(self, resenha):
	    return resenha in self.listaderesenha
    #contar total de resenhas feita por um critito até hoje
    def totalResenhas(self):
        return (len(self.listaderesenha))


class Empresa:
    def __init__(self, uid, cnpj, diretorresponsavel, razaosocial, nomefantasia, telefonesede, listadeestabelecimento=[]):

        self.uid = uid
        self.cnpj = cnpj
        self.diretorresponsavel = diretorresponsavel
        self.razaosocial = razaosocial
        self.nomefantasia = nomefantasia
        self.telefonesede = telefonesede
        self.listadeestabelecimento = listadeestabelecimento

    def inserirEstabelecimento(self, estabelecimento):
        self.listadeestabelecimento.append(estabelecimento)

    def verificarEstabelecimento(self, estabelecimento):
        return estabelecimento in self.listadeestabelecimento

       #verificar media total da empresa ou seja, é a média da média de cada estabelecimento cadastrado gerando uma media geral da empresa

    def mediaDaEmpresa(self):
        total = 0
        divisor = 0
        for x in xrange(len(self.listadeestabelecimento)):
            for y in xrange(len(self.listadeestabelecimento[x].listaDeAvaliacao)):
                total += self.listadeestabelecimento[x].listaDeAvaliacao[y].nota
                divisor +=1    
        return total / divisor

    #verificar empresa acima da média
    def estabelecimentoAcimadaMedia(self):
        listaAcimadaMedia=[]
        media = 0
        total = 0
        divisor = 0
        media = self.mediaDaEmpresa()
        for x in xrange(len(self.listadeestabelecimento)):
            for y in xrange(len(self.listadeestabelecimento[x].listaDeAvaliacao)):
                total += self.listadeestabelecimento[x].listaDeAvaliacao[y].nota
                divisor +=1
            if (total/divisor > media):
                listaAcimadaMedia.append(self.listadeestabelecimento[x])
                print(self.listadeestabelecimento[x])
            total = 0
            divisor = 0
        return listaAcimadaMedia
 

class Estabelecimento:
	def __init__(self, uid, endereco, gerenteresponsavel, ramo, telefone, empresa, listaDeAvaliacao=[], listaderesenha=[]):
		self.uid = uid
		self.endereco = endereco
		self.gerenteresponsavel = gerenteresponsavel
		self.ramo = ramo
		self.telefone = telefone
		self.empresa = empresa
		self.listaDeAvaliacao = listaDeAvaliacao
		self.listaderesenha = listaderesenha

	def inserirResenha(self, resenha):
		self.listaderesenha.append(resenha)

	def verificarResenha(self, resenha):
		return resenha in self.listaderesenha

	def inserirAvaliacao(self, avaliacao):
		self.listaDeAvaliacao.append(avaliacao)

	def verificarAvaliacao(self, avaliacao):
		return avaliacao in self.listaDeAvaliacao
class Avaliacao:
    def __init__(self, uid, alimentosConsumidos, nota, precoTotal, usuario, estabelecimento):
		self.uid = uid
		self.alimentosConsumidos = alimentosConsumidos 
		self.nota = nota
		self.precoTotal = precoTotal
		self.usuario = usuario
		self.estabelecimento = estabelecimento
		
class Resenha:
	def __init__(self, uid, resenha, critico, estabelecimento):
		self.uid = uid
		self.resenha = resenha
		self.critico = critico
		self.estabelecimento = estabelecimento

