listaAluno = []
qntdAprovada, qntdReprovada, qntdRecuperacao = 0, 0, 0

#Excepts
class IdadeInvalidaError(Exception):
    pass
class NotaInvalidaError(Exception):
    pass

print("=-=-" * 15)
print("NSA 2.0.0")
print("=-=-" * 15 + "\n")

#Funcoes
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
    return round(media)

while True:
    while True:
        c = 0
        try:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade de " + nome + ": "))
            if idade<0:
                raise IdadeInvalidaError()
            nota = float(input("Digite a nota de " + nome + ": "))
            if nota>=0 and nota<=10:
                break
            else:
                raise NotaInvalidaError()
        except ValueError:
            print("\n[Error] Insira apenas números. Tente novamente!\n")
        except IdadeInvalidaError:
            print("\n[Error] Idade Inválida! Tente novamente. \n")
        except NotaInvalidaError:
            print("\n[Error] Nota Inválida! Tente novamente.\n")

    Aluno = {
        "nomeAluno": nome,
        "idadeAluno": idade,
        "notaAluno": nota,
        "statusAluno": "Analisando"
    }
    listaAluno.append(Aluno)

    resposta = input("Digite 'N' para parar de cadastrar. Caso contrário aperte enter: ")
    if resposta.lower() == "n":
        break
    else:
        print("\nCadastrando novo aluno:")
j = 0
while j<len(listaAluno):
    calcularNota(j)
    j += 1

menorNota, maiorNota = 0, 0
melhoresAlunos, pioresAlunos = [], []

i = 1
maiorNota = listaAluno[0]["notaAluno"]
menorNota = listaAluno[0]["notaAluno"]
melhoresAlunos = [listaAluno[0]["nomeAluno"]]
pioresAlunos = [listaAluno[0]["nomeAluno"]]

while i<len(listaAluno):
    nota = listaAluno[i]["notaAluno"]
    if nota>maiorNota:
        maiorNota = nota
        melhoresAlunos=[listaAluno[i]["nomeAluno"]]
    elif nota==maiorNota:
        melhoresAlunos.append(listaAluno[i]["nomeAluno"])
    if nota<menorNota:
        menorNota = nota
        pioresAlunos=[listaAluno[i]["nomeAluno"]]
    elif nota == menorNota:
        pioresAlunos.append(listaAluno[i]["nomeAluno"])
    i = i + 1

#Mostrando o resultado

print("\n" + ("=-=-" * 10))
print("RESULTADOS")
print("=-=-" * 10)
i = 0
while i<len(listaAluno):
    print("\nNome: " + listaAluno[i]["nomeAluno"])
    print("Idade: ", listaAluno[i]["idadeAluno"])
    print("Nota: ", listaAluno[i]["notaAluno"])
    print("Situação:  " + listaAluno[i]["statusAluno"])
    i += 1

print("\nmedia da turma foi: ", calcularMedia())
print("Aprovados: ", qntdAprovada)
print("Reprovados: ", qntdReprovada)
print("Recuperação: ", qntdRecuperacao)
print("\nA menor nota da turma: ", menorNota, "do aluno: ")

i = 0
while i<len(pioresAlunos):
    print(pioresAlunos[i])
    i = i + 1
print("\nE a maior nota foi: ", maiorNota, "do aluno: ")
i = 0
while i<len(melhoresAlunos):
    print(melhoresAlunos[i])
    i = i + 1
