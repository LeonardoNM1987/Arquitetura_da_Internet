# AUTOR DO CÓDIGO - LEONARDO MENDONCA


filename = 'sydney20100814.0400.txt' 

with open(filename)as leitor:    


    # CAPTURA APENAS AS TODAS DE CADA LINHA DO ARQUIVO TXT
    for line in leitor:
        currentLine = line.split("|")
        result = str(currentLine[2])+ "\n"
        print(result)







    





