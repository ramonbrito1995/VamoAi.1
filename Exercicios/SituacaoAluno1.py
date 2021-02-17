'''Uma professora deseja desenvolver um sistema para automatizar
seu trabalho. Ela precisa criar uma solução onde seus alunos
consigam inserir suas notas (seja a média geral de todas as
matérias ou a média de uma única disciplina), receber a média, e
saber sua situação (aprovação, reprovação ou recuperação)'''

print("******************************")
print("Situação do Aluno".center(30))
print("******************************")

def notas(nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    print(f"\nSua média é {round(media,2)} !")
    if media >= 7:
        print("Você está aprovado.")
    elif  media >=4  and media <=7 :
        print("\nVocê está de recuperação. "
              "Você precisa tirar", round(10 - media,2),"na prova final.")
    else:
        print("Você está reprovado!")

math = float(input("\nQual é a sua nota de matematica?  "))
port = float(input("\nQual é a sua nota de Português?  "))
bio = float(input("\nQual é a sua nota de Biologia?  "))

notas(8,7,9)