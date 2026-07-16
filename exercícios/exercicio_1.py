nome, sobrenome  = input().split()
idade = int(input())
ano_nascimento = int(input())
maior_de_idade = idade >=18
altura_em_metros = float(input())

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura em metros:", altura_em_metros)