#coding: utf-8

class Usuario:
	def __init__(self, uid, nome, cpf, email, listaDeAvaliacao=[]):
		self.uid = uid
		self.nome = nome
		self.cpf = cpf
		self.email = email
		self.listaDeAvaliacao = listaDeAvaliacao
