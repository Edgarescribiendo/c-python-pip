import read_csv
import utils
import charts

def population_by(data, dato, buscar):
  result = list(filter(lambda item: item[dato] == buscar, data))
  return result
  
def column_by(data,dato):
  column = list(map(lambda i: i[dato] , data))
  return column
                     
  
def run():  
  data = read_csv.read_csv('data.csv')
  dato = ((input('¿Que desea encontrar? ')).lower()).title()
  if dato == 'Country':
    dato = 'Country/Territory'
  buscar = ((input('Nombre: ')).lower()).title()
  
  if buscar == 'Todos':
    print('A elegido todos los paises')
  elif buscar != 'Todos':
    busqueda = population_by(data, dato, buscar)
    print(busqueda)
  question = (input('¿Desea un grafico en barra o de torta? ')).lower() 
  
  if question == 'barra':
    result = population_by(data, dato,buscar)
    if len(result) > 0:
      result = result [0]   
      labels, values = utils.get_population(result)
      charts.generate_bar_chart(buscar, labels, values)
    
  if question == 'torta' and buscar == 'Todos': 
    labels = column_by(data,dato)
    values = column_by(data,dato=input(''))
    charts.generate_pie_chart(labels, values)
    
  if question == 'torta' and not buscar == 'Todos':
    labels = column_by(busqueda,'Country/Territory')
    values = column_by(busqueda,'World Population Percentage')
    charts.generate_pie_chart(labels, values)
    
if __name__=='__main__':
  run()

