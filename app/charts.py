import matplotlib.pyplot as plt
import read_csv
#Con import as, podemos ponerle un alias a las librerias o modules que importemos y asi hacer uso de ellas en codigo mucho mas facil, ya que el alias es mucho mas corto y simple. 

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./countries/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

def choose_country():
  country = input('que pais quieres graficar:')
  return country


def country_population_chart():
  data= read_csv.read_csv('data_ppl.csv')
  #generate_bar_chart(labels, values)

  chosen = choose_country()
  country = list(filter(lambda item: item['Country/Territory'] == chosen, data))
  print(country)
  filt = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
  country_dicc = {key: int(value) for key, value in country[0].items() if key in filt}
  print(country_dicc)
  years = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']

  population = list(country_dicc.values())

  if chosen != None:
      generate_bar_chart(chosen, years, population)
