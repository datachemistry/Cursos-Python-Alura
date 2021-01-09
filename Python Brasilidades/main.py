from acesso_cep import BuscaEndereco
import requests

cep = 13473300
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acesso_viacep()
print(bairro, cidade, uf )


