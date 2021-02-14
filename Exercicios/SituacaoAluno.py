'''Uma professora deseja desenvolver um sistema para automatizar
seu trabalho. Ela precisa criar uma solução onde seus alunos
consigam inserir suas notas (seja a média geral de todas as
matérias ou a média de uma única disciplina), receber a média, e
saber sua situação (aprovação, reprovação ou recuperação)'''

print("******************************")
print("Situação do Aluno".center(30))
print("******************************")

#Programa para calcular a média diretamente e informar a situação do aluno.

def situacao(media):
    if media >= 7:
        return "\nAprovado na matéria!\n"
    elif  media < 7 and media >=4:
       print("\nDe recuperação! Para ser aprovado na final, você precisa tirar no mínimo: ", 10 - media,"pontos.")
    else:
        return "\nReprovado!\n"
    

media = float(input("\nDigite a média da matéria: \n"))

print(situacao(media))
