from borracho import BorrachoTradicional
from coordenada import Coordenada
from campo import Campo
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(name='Moy')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.agregar_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y,pasos):
    grafica = figure(title='Random Walks',x_axis_label='x axis', y_axis_label='y axis')
    grafica.line(x, y, legend_label='walk', color='yellowgreen',name='juan') #recorrido

    # gráfica la línea inicial de movimiento porque no se puede graficar un punto
    grafica.line(x[0:2],y[0:2],color='black',line_width=10)
    grafica.line(x[-3:-1],y[-3:-1],color='red',line_width=10) #punto final y final-1
    grafica.line(x[0:-1:pasos-1],y[0:-1:pasos-1]) #linea de punto inicial a punto final
    show(grafica)

def main(distancias_caminata, numero_de_intentos, tipo_de_borracho):

    distancias_medias_por_caminatas= []

    for pasos in distancias_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_medias_por_caminatas.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Maximo = {distancia_maxima}')
        print(f'Minimo = {distancia_minima}')

    graficar(distancias_caminata, distancias_medias_por_caminatas,pasos)

if __name__ == '__main__':

    distancias_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_caminata, numero_de_intentos, BorrachoTradicional)