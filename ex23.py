listaAluno = []
qntdAprovada = 0
qntdReprovada = 0
qntdRecuperacao = 0
def calcularNota(indice):
    global qntdAprovada, qntdReprovada, qntdRecuperacao
    nota = listaAluno[indice]["notaAluno"]
    if nota>= 7:
        qntdAprovada = qntdAprovada + 1
        listaAluno[indice]["statusAluno"] = "Aprovado"
    elif nota >= 5:
        qntdRecuperacao = qntdRecuperacao+ 1
        listaAluno[indice]["statusAluno"] = "Recuperação"
    else:
        qntdReprovada = qntdReprovada + 1
        listaAluno[indice]["statusAluno"] = "Reprovado"
def calcularMedia():
    i = 0
    totalNotas = 0
    while i<len(listaAluno):
        totalNotas = totalNotas + listaAluno[i]["notaAluno"]
        i = i + 1
    media = totalNotas/len(listaAluno)
    return (media)
while True:
    while True:
        try:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            nota = float(input("Digite a nota do aluno: "))
            if idade>0 and nota>=0 and nota<=10:
                break
            else:
                print("Idade ou nota invalida, tente novamente")
        except ValueError:
            print("Valor invalido, insira novamente")
    Aluno = {
        "nomeAluno": nome,
        "idadeAluno": idade,
        "notaAluno": nota,
        "statusAluno": "Analisando"
    }
    listaAluno.append(Aluno)

    resposta = input("Digite 'N' se você deseja para de cadastrar")
    if resposta.lower() == "n":
        break
    else:
        print("Cadastrando novo aluno:")
j = 0
while j<len(listaAluno):
    calcularNota(j)
    j += 1

#Mostrando o resultado
i = 0
while i<len(listaAluno):
    print("Nome: " + listaAluno[i]["nomeAluno"])
    print("Idade: ", listaAluno[i]["idadeAluno"])
    print("Nota: ", listaAluno[i]["notaAluno"])
    print("Este aluno está atualmente " + listaAluno[i]["statusAluno"])
    i += 1
print("A media da turma foi: ", calcularMedia())
print("A quantidade de aprovados foi: ", qntdAprovada)
print("A quantidade de reprovados foi: ", qntdReprovada)
print("A quantidade de pessoas em recuperação foi: ", qntdRecuperacao)
