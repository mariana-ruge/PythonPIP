import matplotlib.pyplot as plt

#Función que genera un chart
def generar_pychart():
    etiquetas = ['A', 'B', 'C']
    valores = [200, 100, 300]

    fig, ax = plt.subplots()
    ax.pie(valores, labels=etiquetas)
    plt.savefig('pie.png')
    plt.close()
    