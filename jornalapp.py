#coding: utf-8

class Usuario:
	def __init__(self, uid, nome, cpf, email, listaDeAvaliacao=[]):
		self.uid = uid
		self.nome = nome
		self.cpf = cpf
		self.email = email
		self.listaDeAvaliacao = listaDeAvaliacao

class Empresa:
	def __init__(self, uid, cnpj, diretorresponsavel, razaosocial, nomefantasia, telefonesede, listadeestabelecimento=[]):

		self.uid = uid
		self.cnpj = cnpj
		self.diretorresponsavel = diretorresponsavel
		self.razaosocial = razaosocial
		self.nomefantasia = nomefantasia
		self.telefonesede = telefonesede
		self.listadeestabelecimento = listadeestabelecimento
		
class Critico:
	def __init__(self, uid, nome, cargo, email, listaderesenha=[]):
		self.uid = uid
		self.nome = nome
		self.cargo = cargo
		self.email = email
		self.listaderesenha = listaderesenha

class Estabelecimento:
	def __init__(self, uid, endereco, gerenteresponsavel, ramo, telefone, empresa, listadeinformacaodevisita=[], listaderesenha=[]):
		self.uid = uid
		self.endereco = endereco
		self.gerenteresponsavel = gerenteresponsavel
		self.ramo = ramo
		self.telefone = telefone
		self.empresa = empresa
		self.listadeinformacaodevisita = listadeinformacaodevisita
		self.listaderesenha = listaderesenha

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

