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
