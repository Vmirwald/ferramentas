#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:36:09 2019

@author: vitor
"""

import pandas as pd
from pandas import DataFrame as df


arquivo = input('Entre com o nome do arquvivo sem .csv \n')
campo = input('Entre com o nome da coluna \n')

horas = input("horas a corrigir\n")
horas = int(horas)

data = pd.read_csv(arquivo)

df = df(data) #df é um DataFrame onde o conteúdo são os dados da tabela Data


df[campo] = pd.to_datetime(df[campo])
df[campo] = pd.to_datetime(df[campo], format = '%Y-%m-%d %H:%M:s') #função que reconhece formato de hora e data
df[campo] = pd.to_datetime(df[campo].astype(str)) + pd.DateOffset(hours= horas, minutes=00) #Adiciona 3horas 
df.to_csv(arquivo + "_data_time_tratado.csv", index = False) #faz novo arquivo .csv

#Alterando campo ' ' para T novamente.
data = open(arquivo + "_data_time_tratado.csv",'r')

horas1 = str(horas)
dataout = open(arquivo +"_data_time_tratado_"+ horas1 + ".csv", "w")

for line in data:
	dataout.write(line.replace(' ', 'T'))
data = dataout
data.close()
dataout.close()


#Fim de Programa
