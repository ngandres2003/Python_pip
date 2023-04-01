def get_population(country_dict):
    population_dict ={
          2022 :int(country_dict['2022 Population']),
          2020:int(country_dict['2020 Population']),
          2015:int(country_dict['2015 Population']),
          2010:int(country_dict['2010 Population']),
          2000:int(country_dict['2000 Population']),
          1990:int(country_dict['1990 Population']),
          1980:int(country_dict['1980 Population']),
          1970:int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels,values

def population_by_country(data,country):
    return list(filter(lambda item : item['Country/Territory'] == country,data))

def get_percentage(dato):
    keys = list(map(lambda item : item['Country/Territory'],dato))
    values = list(map(lambda item:float(item['World Population Percentage']),dato))
    dict_ = dict(zip(keys,values))
    keys2 =[]
    for  x,y in dict_.items():
        if y > 0.7:
            keys2.append(x)
        else:
            keys2.append('')
    return keys2,values
    
