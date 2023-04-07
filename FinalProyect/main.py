import utils
import read_csv
import charts
import pandas

def run():
    
    data = read_csv.read_('./data.csv')
    country = input('Type Country: ').capitalize()
    result = utils.population_by_country(data,country)

    if len(result)> 0:
        country = result[0]
        labels,values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'],labels,values)
if __name__ == '__main__':
    run()

def run2():
    dato = read_csv.read_('./data.csv')
    keys,values = utils.get_percentage(dato)
    charts.generate_pie_chart(keys,values)
if __name__=='__main__':
    run2()





