# AUTOR DO CÓDIGO - LEONARDO MENDONCA

filename = 'sydney20100814.0400.txt' 

with open(filename)as leitor:    



    #EXIBE QTDE DE LINHAS DO ARQUIVO UTILIZADO
     for line in leitor:
        linhas = len(leitor.readlines())
        print("Arquivo: ", filename)
        print("Total de Linhas: ",linhas)






    





