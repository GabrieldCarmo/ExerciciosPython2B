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

def calcularClassificacao():
    global maiorNota, menorNota, melhoresAlunos, pioresAlunos
    i = 1
    maiorNota = listaAluno[0]["notaAluno"]
    menorNota = listaAluno[0]["notaAluno"]
    melhoresAlunos = [listaAluno[0]["nomeAluno"]]
    pioresAlunos = [listaAluno[0]["nomeAluno"]]
    while i<len(listaAluno):
        nota = listaAluno[i]["notaAluno"]
        if nota>maiorNota:
            maiorNota = nota
            melhoresAlunos.clear()
            melhoresAlunos.append(listaAluno[i]["nomeAluno"])
        elif nota==maiorNota:
            melhoresAlunos.append(listaAluno[i]["nomeAluno"])
        if nota<menorNota:
            menorNota = nota
            pioresAlunos.clear()
            pioresAlunos.append(listaAluno[i]["nomeAluno"])
        elif nota == menorNota:
            pioresAlunos.append(listaAluno[i]["nomeAluno"])
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

calcularClassificacao()
print("A menor nota da turma foi: ", menorNota, " com esse(s) aluno(s) que tem essa nota: ")
i = 0
while i<len(pioresAlunos):
    print(pioresAlunos[i])
    i = i + 1
print("E a maior nota foi: ", maiorNota, "com esse(s) aluno(s) que tem essa nota: ")
i = 0
while i<len(melhoresAlunos):
    print(melhoresAlunos[i])
    i = i + 1

