#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:36:09 2019

@author: vitor
"""

import pandas as pd
from pandas import DataFrame as df

data = pd.read_csv('eventos1.csv')

df = df(data) #df é um DataFrame onde o conteúdo são os dados da tabela Data


df['field_eventdate'] = pd.to_datetime(df['field_eventdate'])
df['field_eventdate'] = pd.to_datetime(df['field_eventdate'], format = '%Y-%b-%d%H:%M') #função que reconhece formato de hora e data
df['field_eventdate'] = pd.to_datetime(df['field_eventdate'].astype(str)) + pd.DateOffset(hours=3, minutes=00) #Adiciona 3horas 
df.to_csv('eventos_tratado.csv', index = False) #faz novo arquivo .csv

#Alterando campo ' ' para T novamente.
data = open("eventos_tratado.csv",'r')
dataout = open("eventos_+3.csv", "w")

for line in data:
	dataout.write(line.replace(' ', 'T'))
	
data.close()
dataout.close()


#Fim de Programa
