listaAluno[]

def cadastroAluno ():
    while True:
        try:
            nome = input("Digite o nome do aluno")
            idade = input("Digite a idade do aluno")
            nota = int(input("Digite a nota do aluno"))
            break
        except ValueError:
            print("Valor invalido, insira novamente")
    Aluno = {
        "nomeAluno": nome,
        "idadeAluno": idade,
        "notaAluno": nota,
        "statusAluno": "Analisando"
    }
    listaAluno.append(Aluno)
def calcularNota:
    i = 0
    while i<len(listaAluno):
        nota = listaAluno[i]["notaAluno"]
        if nota>= 7:
            listaAluno[i]["statusAluno"] = "Aprovado"

while True:
    cadastroAluno()
    resposta = input("Digite 'N' se você deseja para de cadastrar")
    if resposta.toLower() == "n":
        break
    else:
        print("Cadastrando novo aluno:")
