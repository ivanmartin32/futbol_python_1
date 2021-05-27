#!/usr/bin/env python
'''
Archivos [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.4"

import csv
import re
from statistics import mean

def cantidad_partidos_local(partidos,seleccion):     
    
    cantidad_partidos = 0

    for i in range(len(partidos)):
        datos = partidos[i]
        for k, v in datos.items():
            if k == 'home_team':
                if v == seleccion:
                    cantidad_partidos += 1
    return cantidad_partidos

def cantidad_partidos_visitante(partidos,seleccion):     
    
    cantidad_partidos = 0

    for i in range(len(partidos)):
        datos = partidos[i]
        for k, v in datos.items():
            if k == 'away_team':
                if v == seleccion:
                    cantidad_partidos += 1
    return cantidad_partidos
                                                                                                                                                                                                     
def partidos_ganados_local(partidos,seleccion):     
    
    cantidad_ganados_local = 0
    
    for i in range(len(partidos)):
        datos = partidos[i]
        for k, l in datos.items():
            if k == 'home_score':
                for k, v in datos.items():
                    if k == 'away_score':
                        if l > v:
                            for k,s in datos.items():
                                if k == 'home_team':
                                    if s == seleccion:
                                        cantidad_ganados_local += 1
    return cantidad_ganados_local                                            
                                    
def partidos_ganados_visitante(partidos,seleccion):     
    
    cantidad_ganados_visitante = 0
    
    for i in range(len(partidos)):
        datos = partidos[i]
        for k, l in datos.items():
            if k == 'home_score':
                for k, v in datos.items():
                    if k == 'away_score':
                        if l < v:
                            for k,s in datos.items():
                                if k == 'away_team':
                                    if s == seleccion:
                                        cantidad_ganados_visitante += 1

    return cantidad_ganados_visitante

def partidos_perdidos_local(partidos,seleccion):     
    
    cantidad_perdidos_local = 0
    
    for i in range(len(partidos)):
        datos = partidos[i]
        for k, l in datos.items():
            if k == 'home_score':
                for k, v in datos.items():
                    if k == 'away_score':
                        if l < v:
                            for k,s in datos.items():
                                if k == 'home_team':
                                    if s == seleccion:
                                        cantidad_perdidos_local += 1
    return cantidad_perdidos_local  

def partidos_perdidos_visitante(partidos,seleccion):     
    
    cantidad_perdidos_visitante = 0
    
    for i in range(len(partidos)):
        datos = partidos[i]
        for k, l in datos.items():
            if k == 'home_score':
                for k, v in datos.items():
                    if k == 'away_score':
                        if l > v:
                            for k,s in datos.items():
                                if k == 'away_team':
                                    if s == seleccion:
                                        cantidad_perdidos_visitante += 1
    return cantidad_perdidos_visitante

def empate_local(partidos,seleccion):

    cantidad_empates_local = 0

    for i in range(len(partidos)):
        datos = partidos[i]
        for k, l in datos.items():
            if k == 'home_score':
                for k, v in datos.items():
                    if k == 'away_score':
                        if l == v:
                            for k,s in datos.items():
                                if k == 'home_team':
                                    if s == seleccion:
                                        cantidad_empates_local += 1
    return cantidad_empates_local

def empate_visitante(partidos,seleccion):

    cantidad_empates_visitante = 0

    for i in range(len(partidos)):
        datos = partidos[i]
        for k, l in datos.items():
            if k == 'home_score':
                for k, v in datos.items():
                    if k == 'away_score':
                        if l == v:
                            for k,s in datos.items():
                                if k == 'away_team':
                                    if s == seleccion:
                                        cantidad_empates_visitante += 1
    return cantidad_empates_visitante
                              

def goles_local_marcados(partidos,seleccion):

    cantidad_goles_local = 0

    for i in range(len(partidos)):
        datos = partidos[i]
        for k,s in datos.items():
            if k == 'home_score':
                for k,t in datos.items():
                    if k == 'home_team':
                        if t == seleccion:
                            cantidad_goles_local += int(str(s))
    return cantidad_goles_local 

def goles_visitante_marcados(partidos,seleccion):

    cantidad_goles_visitante = 0

    for i in range(len(partidos)):
        datos = partidos[i]
        for k,s in datos.items():
            if k == 'away_score':
                for k,t in datos.items():
                    if k == 'away_team':
                        if t == seleccion:
                            cantidad_goles_visitante += int(str(s))
    return cantidad_goles_visitante  

def goles_local_marcaron(partidos,seleccion):

    cantidad_goles_local = 0

    for i in range(len(partidos)):
        datos = partidos[i]
        for k,s in datos.items():
            if k == 'away_score':
                for k,t in datos.items():
                    if k == 'home_team':
                        if t == seleccion:
                            cantidad_goles_local += int(str(s))
    return cantidad_goles_local 

def goles_visitante_marcaron(partidos,seleccion):

    cantidad_goles_local = 0

    for i in range(len(partidos)):
        datos = partidos[i]
        for k,s in datos.items():
            if k == 'home_score':
                for k,t in datos.items():
                    if k == 'away_team':
                        if t == seleccion:
                            cantidad_goles_local += int(str(s))
    return cantidad_goles_local 

def ultimos_partidos(partidos,seleccion):

    ultimos_10_partidos = []

    for i in range(len(partidos)):
        datos = partidos[i]
        for k,l in datos.items():
            if k == 'home_team':
                if l == seleccion:
                    ultimos_10_partidos.append(l)
                    for o,e in datos.items():
                        if o == 'away_team':
                            if e != seleccion:
                                ultimos_10_partidos.append(e)
            if k == 'away_team':
                if l == seleccion:
                    for o,e in datos.items():
                        if o == 'home_team':
                            if e != seleccion:
                                ultimos_10_partidos.append(e)
                                ultimos_10_partidos.append(l)

    return ultimos_10_partidos

def hostorial_partidos(partidos,seleccion,seleccion_contraria):

    historial_ganados = 0
    historial_empatados = 0
    historial_perdidos = 0
    goles_favor = 0
    goles_contra = 0
    ultimos_resultados = []

    for i in range(len(partidos)):
        datos = partidos[i]
        for k,s in datos.items():
            if k == 'home_score':
                for h,t in datos.items():
                    if h == 'home_team':
                        if t == seleccion:
                            for a,g in datos.items():
                                if a == 'away_score':
                                    for v,b in datos.items():
                                        if v == 'away_team':
                                            if b == seleccion_contraria:
                                                goles_favor += int(str(s))
                                                goles_contra += int(str(g))
                                                if s == g:
                                                    historial_empatados += 1
                                                if s > g:
                                                    historial_ganados += 1
                                                if s < g:
                                                    historial_perdidos += 1
                                                ultimos_resultados.append(t)
                                                ultimos_resultados.append(s) 
                                                ultimos_resultados.append(g)
                                                ultimos_resultados.append(b)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            if k == 'away_score':
                for h,t in datos.items():
                    if h == 'away_team':
                        if t == seleccion:
                            for a,g in datos.items():
                                if a == 'home_score':
                                    for v,b in datos.items():
                                        if v == 'home_team':
                                            if b == seleccion_contraria:
                                                goles_favor += int(str(s))
                                                goles_contra += int(str(g))
                                                if s == g:
                                                    historial_empatados += 1
                                                if s > g:
                                                    historial_ganados += 1
                                                if s < g:
                                                    historial_perdidos += 1
                                                ultimos_resultados.append(b)
                                                ultimos_resultados.append(g) 
                                                ultimos_resultados.append(s)
                                                ultimos_resultados.append(t) 
                                                
    return (historial_ganados,historial_empatados,
            historial_perdidos,goles_favor,goles_contra,
            ultimos_resultados)
    




def menu():

    csvfile = open('partidos.csv')
    
    partidos = list(csv.DictReader(csvfile))

    print('Datos a marcar, los nombres de selecciones son en ingles')

    seleccion = str.capitalize(input(
        'Ingrese la seleccion que desea evaluar\n'))

    print('Elija una de las siguientes opciones que desea saber:')

    opciones_numeros = int(input('1- Para saber cantidad de partidos jugados \n'
                        '2- Para saber cantidad de partidos ganados \n'
                        '3- Para saber cantidad de partidos perdidos \n'
                        '4- Para saber cantidad de partidos empatados \n'
                        '5- Para saber cantidad de goles que marco \n'
                        '6- Para saber la cantidad de goles que le marcaron \n'
                        '7- Mostrar contra quienes jugo los ultimos 10 partidos \n'
                        '8- Para saber el historial de partidos contra otro equipo \n'))
                        
                                                                                                                                                                    
    
    if opciones_numeros == 1:
        opciones_letras = str.capitalize(input('A- Partidos totales jugados \n'
                            'B- Partidos de Local jugados \n'
                            'C- Partidos de Visitante jugados \n'))
                            
        if opciones_letras == 'A':
            partidos_jugados_local = cantidad_partidos_local(partidos,seleccion)
            partidos_jugados_visitante = cantidad_partidos_visitante(partidos,seleccion)
            partidos_jugados_total = partidos_jugados_local + partidos_jugados_visitante
            print(partidos_jugados_total)
        if opciones_letras == 'B':
            partidos_jugados_local = cantidad_partidos_local(partidos,seleccion)
            print(partidos_jugados_local)
        if opciones_letras == 'C':
            partidos_jugados_visitante = cantidad_partidos_visitante(partidos,seleccion)
            print(partidos_jugados_visitante)
        #else:
        #    print('ERROR, la letra ingresada no coincide con el menu, vuelva a intentarlo')

    if opciones_numeros == 2:
        opciones_letras = str.capitalize(input('A- Partidos totales ganados \n'
                        'B- Partidos de Local ganados \n'
                        'C- Partidos de Visitante ganados \n'))
        if opciones_letras == 'A':
            partidos_local_ganados = partidos_ganados_local(partidos,seleccion)
            partidos_visitante_ganados = partidos_ganados_visitante(partidos,seleccion)
            partidos_total_ganados = partidos_local_ganados + partidos_visitante_ganados
            print(partidos_total_ganados)
        if opciones_letras == 'B':
            partidos_local_ganados = partidos_ganados_local(partidos,seleccion)
            print(partidos_local_ganados)
        if opciones_letras == 'C':
            partidos_visitante_ganados = partidos_ganados_visitante(partidos,seleccion)
            print(partidos_visitante_ganados)
        #else:
        #    print('ERROR, la letra ingresada no coincide con el menu, vuelva a intentarlo')

    if opciones_numeros == 3:
        opciones_letras = str.capitalize(input('A- Partidos totales perdidos \n'
                        'B- Partidos de Local perdidos \n'
                        'C- Partidos de Visitante perdidos \n'))
        if opciones_letras == 'A':
            partidos_local_perdidos = partidos_perdidos_local(partidos,seleccion)
            partidos_visitante_perdidos = partidos_perdidos_visitante(partidos,seleccion)
            partidos_total_perdidos = partidos_local_perdidos + partidos_visitante_perdidos
            print(partidos_total_perdidos)
        if opciones_letras == 'B':
            partidos_local_perdidos = partidos_perdidos_local(partidos,seleccion)
            print(partidos_local_perdidos)
        if opciones_letras == 'C':
            partidos_visitante_perdidos = partidos_perdidos_visitante(partidos,seleccion)
            print(partidos_visitante_perdidos)
        #else:
        #    print('ERROR, la letra ingresada no coincide con el menu, vuelva a intentarlo')
    if opciones_numeros == 4:
        opciones_letras = str.capitalize(input('A- Total de partidos empatados \n'
                'B- Total de partidos empatados de local \n'
                'C- Total de partidos empatados de visitante \n'))
        if opciones_letras == 'A':
            empatados_local = empate_local(partidos,seleccion)
            empatados_visitante = empate_visitante(partidos,seleccion)
            total_empatados = empatados_local + empatados_visitante
            print(total_empatados)
        if opciones_letras == 'B':
            empatados_local = empate_local(partidos,seleccion)
            print(empatados_local)
        if opciones_letras == 'C':
            empatados_visitante = empate_visitante(partidos,seleccion)
            print(empatados_visitante)

    if opciones_numeros == 5:
        opciones_letras = str.capitalize(input('A- Total de goles marcados \n'
                'B- Total goles marcados de local \n'
                'C- Total goles marcados de visitante \n'))

        if opciones_letras == 'A':
            goles_local = goles_local_marcados(partidos,seleccion)
            goles_visitante = goles_visitante_marcados(partidos,seleccion)
            goles_total = goles_local + goles_visitante
            print(goles_total)
        if opciones_letras == 'B':
            goles_local = goles_local_marcados(partidos,seleccion)
            print(goles_local)
        if opciones_letras == 'C':
            goles_visitante = goles_visitante_marcados(partidos,seleccion)
            print(goles_visitante)
    
    if opciones_numeros == 6:
        opciones_letras = str.capitalize(input('A- Total de goles que le marcados \n'
                'B- Total goles que le marcaron de local \n'
                'C- Total goles que le marcaron de visitante \n'))
        if opciones_letras == 'A':
            goles_local = goles_local_marcaron(partidos,seleccion)
            goles_visitante = goles_visitante_marcaron(partidos,seleccion)
            goles_total = goles_local + goles_visitante
            print(goles_total)
        if opciones_letras == 'B':
            goles_local = goles_local_marcaron(partidos,seleccion)
            print(goles_local)
        if opciones_letras == 'C':
            goles_visitante = goles_visitante_marcaron(partidos,seleccion)
            print(goles_visitante)

    if opciones_numeros == 7:
        ultimos_10_partidos = ultimos_partidos(partidos,seleccion)
        
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-20:-19]))), 'vs', 
            '\n'.join(list(map(''.join, ultimos_10_partidos[-19:-18]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-18:-17]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-17:-16]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-16:-15]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-15:-14]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-14:-13]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-13:-12]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-12:-11]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-11:-10]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-10:-9]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-9:-8]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-8:-7]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-7:-6]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-6:-5]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-5:-4]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-4:-3]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-3:-2]))))
        print('\n'.join(list(map(''.join, ultimos_10_partidos[-2:-1]))), 'vs',
            '\n'.join(list(map(''.join, ultimos_10_partidos[-1:]))))

    if opciones_numeros == 8:

        seleccion_contraria = str.capitalize(input(
            'Ingrese la seleccion que desea evaluar el historial \n'))
        
        historial = hostorial_partidos(partidos,seleccion,seleccion_contraria)
        print(seleccion, 'le gano',historial[0],'veces a {}'.format(seleccion_contraria))
        print(seleccion, 'empato',historial[1],'veces con {}'.format(seleccion_contraria))
        print(seleccion, 'perdio',historial[2],'veces con {}'.format(seleccion_contraria))
        print(seleccion, 'le marco',historial[3],'goles a {}'.format(seleccion_contraria))
        print(seleccion_contraria, 'le marco',historial[4],'goles a {}'.format(seleccion))
        print('Los ultimos 5 resultados de {} contra {} son:'.format(seleccion,seleccion_contraria))
        ultimos_5_resultados = historial[5]
        print('\n'.join(list(map(''.join, ultimos_5_resultados[-20:-19]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-19:-18]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-18:-17]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-17:-16]))), '',)
        print('\n'.join(list(map(''.join, ultimos_5_resultados[-16:-15]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-15:-14]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-14:-13]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-13:-12]))), '',)
        print('\n'.join(list(map(''.join, ultimos_5_resultados[-12:-11]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-11:-10]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-10:-9]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-9:-8]))), '',)
        print('\n'.join(list(map(''.join, ultimos_5_resultados[-8:-7]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-7:-6]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-6:-5]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-5:-4]))), '',)
        print('\n'.join(list(map(''.join, ultimos_5_resultados[-4:-3]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-3:-2]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-2:-1]))), '',
                '\n'.join(list(map(''.join, ultimos_5_resultados[-1:]))))
    
    csvfile.close()
    
    
        #else:
        #    print('ERROR, la letra ingresada no coincide con el menu, vuelva a intentarlo')
        

        
                                                          
    #else:
    #    print('ERROR, el numero ingresado no coincide con el menu, vuelva a intentarlo')

if __name__ == '__main__':
    print("Bienvenidos a consultas de estaditicas de selecciones de futbol 1872-2020")
    menu()
    
    