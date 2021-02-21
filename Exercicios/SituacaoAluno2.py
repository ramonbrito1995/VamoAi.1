'''Uma professora deseja desenvolver um sistema para automatizar
seu trabalho. Ela precisa criar uma solução onde seus alunos
consigam inserir suas notas (seja a média geral de todas as
matérias ou a média de uma única disciplina), receber a média, e
saber sua situação (aprovação, reprovação ou recuperação)'''

print("******************************")
print("Situação do Aluno".center(30))
print("******************************")


def media():
    materia = list()
    disciplinas = list()
    x = int(input("\nQuantas matérias você quer calcular a media das notas? "))
    for c in range(0,x):
        materia.append(str(input(f"\nDiga o nome da {c+1}° matéria? ")))
        materia.append(float(input("\nQual é a média da matéria? ")))
        disciplinas.append(materia[:])
        materia.clear()
    soma = sum( [x[1] for x in disciplinas])
    print("\n\nA média de suas matérias é: ",round((soma/x),2))
    print("\n\nAs matérias que você informou são:")
    for x in disciplinas:
        print(x[0],":",x[1])
      
media() 

