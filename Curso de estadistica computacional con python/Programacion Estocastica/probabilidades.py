import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    suma_de_tiros = []
    secuencia_de_tiros_1=0
    secuencia_de_tiros_2=1
    for _ in range(numero_de_intentos):
        secuencia_de_tiros_1 = tirar_dado(numero_de_tiros)
        print(secuencia_de_tiros_1)

        secuencia_de_tiros_2 = tirar_dado(numero_de_tiros)
        print(secuencia_de_tiros_2)
        
        for i in range(len(secuencia_de_tiros_1)):
            suma_tmp = 0
            suma_tmp = secuencia_de_tiros_1[i] + secuencia_de_tiros_2[i]
            print(suma_tmp)
            
            suma_de_tiros.append(suma_tmp)
        
    tiros.append(suma_de_tiros)
        
    print(tiros)          
                
            
            
    tiros_con_12 = 0
    for tiro in tiros:
        if 12 in tiro:
            tiros_con_12 += 1

    print(tiros_con_12)

    probabilidad_tiros_con_1 = tiros_con_12 / numero_de_intentos
    print(f'Probabilidad de obtener 12 como suma de ambos dados en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')



if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)