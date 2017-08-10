# Esse arquivo serve unicamente para salvar
# e carregar informações em diferentes sessões
###############################################

import pickle

def Salvar(c, e):
	infoEstabelecimento = open("infoe.ar", 'wb')
	infoCartao = open("infoc.ar", 'wb')
	pickle.dump(c, infoCartao)
	pickle.dump(e, infoEstabelecimento)
	infoEstabelecimento.close()
	infoCartao.close()
	return "Informações salvas corretamente"

def Load():
	infoEstabelecimento = open("infoe.ar", 'rb')
	infoCartao = open("infoc.ar", 'rb')
	return (pickle.load(infoCartao), pickle.load(infoEstabelecimento))