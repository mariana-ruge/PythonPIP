import utils_a
import leer_datos
import pandas as pd

def run():
    dataFrame = pd.read_csv('lego.csv')
    dF1 = dataFrame[dataFrame['Theme']=='LEGOLAND']
    dF2 = dataFrame[dataFrame['Theme']=='Trains']

    anios = dF1['Year'].values
    grupo = dF2['Name'].values
    print(anios)
    print(grupo)

if __name__ == "__main__":
    run()

