ListaIdade = [10,25,23,45,56]
ListaNome = ["Ana", "Joao", "Bia", "Bruno", "Eliza"]
for n in ListaNome:
    print("Nome: "+ n)
for n in ListaIdade:
    print(f"Idade: {n}")
ListaNome.sort() #Ordena Por ordem de maior para o menor
print(ListaNome)
ListaIdade.insert(0, 15) #Primeiro é a posição segundo é oque sera inserido
print(ListaIdade)
ListaNome.append("Luan") #Coloca por ultimo
print(ListaNome)
#Estas Listas podem possuir elementos de diferentes tipos juntos Mas não é o ideal
