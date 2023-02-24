import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
#Delimiter se refiere a con que estan separados cada uno de los valores del archivo
    header= next(reader)
    #Como es un iterable, con este next() hacemos que header obtenga la primera fila del csv, la cual son las categorias de cada uno de los datos.
    data = []
    for row in reader:
      iterable = zip(header, row)
      #aqui estamos uniendo los valores de dos listas, para generar tulas de cada uno de los pares
      '''print(list(iterable))#final mente imprimimos las tuplas generadas dentro de una gran lista. Asi tendremos cada uno de los valores junto a su respectiva categoria.'''
      country_dicc = {key : value for key, value in iterable}
      data.append(country_dicc)
    #ahora para administrar bien los datos, con el iterable creado con zip, lo recorreremos como clave:valor para crear un diccionario de cada uno de los paises y luego agregar el diccionario a una lista que contendra todos los diccionarios creados por pais
  return data

    
if __name__ == '__main__':
  data_list = read_csv('data_ppl.csv')
  print(data_list)