import os,sys
import getter

if __name__=='__main__':
    if not os.path.isfile('size_of_kit.txt'): getter.main()
    grupo = []
    with open('size_of_kit.txt','r') as file: 
        size = int(file.readline())
        for i in range(size):
            texto = []
            for _ in range(8): 
                texto.append(file.readline().strip('\n'))
            nome = texto[0]
            tamanho = int(texto[6].split()[1])
            tupla = (tamanho,nome)
            grupo.append(tupla)
    grupo.sort()
    smallest = grupo[0][0]
    with open('ordered_kit_size.txt','w') as file:
        for i in grupo:
            file.write(f'{i[1]} {i[0]} {i[0]/smallest : .3}\n')