from cpf_cnpj import Documento
#cpf = "39636169896"
#objeto_cpf = Cpf(cpf)
#print(objeto_cpf)

# este dá Erro
#cpf_novo = "11111111111111"
#objeto_cpf = Cpf(cpf_novo)
#print(objeto_cpf)


exemplo_cnpj = "03265765000141"
exemplo_cpf = "39636169896"

documento1 = Documento.cria_documento(exemplo_cnpj)
documento2 = Documento.cria_documento(exemplo_cpf)

print(documento1)
print(documento2)
