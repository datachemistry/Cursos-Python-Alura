import re
from TelefBr import TelefBr

# padrao = "[0-9][a-z]{1,2}[0-9]"
# texto = "123 1ac2 lcc aal"
# resposta = re.search(padrao, texto)
# print(resposta.group())


#padrao_email = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
#email = "aaaaaabbb   thiagoyuki@gmail.com.br fsfsdfsdfsdfsdf"
#resposta = re.search(padrao_email, email)
#print(resposta.group())

#padrao_email = "\w{5,50}@[a-z]{3,10}.com.br"
#email = "aaaaaabbb   datachemistry@gmail.com.br fsfsdfsdfsdfsdf"
#resposta = re.search(padrao_email, email)
#print(resposta.group())

#padrao_molde = "(xx)aaa-aaaa"
#padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
#texto = "Meu numero é 19991273092 mas também 1921083056"
#resposta = re.findall(padrao, texto)
#print(resposta)

#telefone = "1921083056"
#objeto_telefone = TelefBr(telefone)

#telefone = "5519991273092"
#padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.findall(padrao, telefone)
#resposta2 = re.search(padrao, telefone)
#print(resposta)
#print(resposta2)
#print(resposta2.group())
#print(resposta2.group(1))
#print(resposta2.group(2))
#print(resposta2.group(3))

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#telefone2 = "19991273092"
#resposta = re.findall(padrao, telefone2)
#resposta2 = re.search(padrao, telefone2)
#print(resposta)
#print(resposta2)
#print(resposta2.group())
#print(resposta2.group(1))
#print(resposta2.group(2))
#print(resposta2.group(3))

telefone = "551921083056"
telefone_objeto = TelefBr(telefone)
print(telefone_objeto)

telefone = "5519991273092"
telefone_objeto = TelefBr(telefone)
print(telefone_objeto)
