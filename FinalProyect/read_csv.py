import csv
def read_(path):
    with open(path,'r') as csvfile:
      reader = csv.reader(csvfile,delimiter=(','))
      header = next(reader)
      lista = []
      for row in reader:
        iterable = zip(header,row)
        dict_ = {key:value for key,value in iterable}
        lista.append(dict_)
      return lista
      
      
        

if __name__=='__main__':
   read_('./FinalProyect/data.csv')
  
