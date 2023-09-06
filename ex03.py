nome = str(input("Digite seu nome:")) #Nome com mais de 3 caracteres
while len(nome)<4:
    nome = str(input("[ERRO] Digite novamente seu nome:"))

idade = int(input("Digite sua idade:")) #Idade precisa estar entre 0 e 150 anos
while idade<0 or idade>150:
    idade = int(input("[ERRO] Digite novamente sua idade:"))

salario = float(input("Digite seu salário:")) #Salário precisa ser maior que 0
while salario<0:
    salario = float(input("[ERRO] Digite novamente seu salário:"))

sexo = str(input("Digite seu sexo (f ou m):")) #Sexo feminino ou masculino
while sexo !="f" and sexo!="m" :
    sexo = str(input("[ERRO] Digite novamente seu sexo (f ou m):"))

est_civil = str(input("Digite seu Estado Civil (s, c, v ou d):")) #Estado civil solteiro casado viúvo ou divorcidado
while est_civil !='s' and est_civil !='c' and est_civil !='v' and est_civil !='d':
    est_civil = str(input("[ERRO] Digite novamente seu Estado Civil (s, c, v ou d):"))
    
print(f"Nome:{nome}; Idade:{idade}; Salário:R${salario}; Sexo:{sexo}; Estado Civil:{est_civil}.")
