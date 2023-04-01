import matplotlib.pyplot as plt # usamos el as como un alias para usarla mas facil

def generate_bar_chart(name,labels,values):
    fig,ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels,values):
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig("./imgs/pie.png")
    plt.close()

labels = ['a','b','c']
values = [100,200,300]
if __name__ =='__main__':
    generate_pie_chart(labels,values)