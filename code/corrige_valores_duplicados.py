#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:57:00 2019

@author: vitor
"""

from pandas import DataFrame as df, read_csv
import pandas as pd
import numpy as np

arquivo = input ("Arquivo a ser modificado ( + .csv):\n") #recebe arquivo
coluna = input("Nome da coluna a ser transformada em linha:\n")#recebe nome da coluna

data = read_csv(arquivo, sep = ',')

for i in data['nid'].unique(): #percorre todos os nids
    
    aux = data[data['nid']==i][['nid','title',coluna]] #seleciona apenas os nids que são iguais a i

    c = aux[coluna].tolist()#transforma a coluna em lista
    c = df(c)
    title = df(aux['title'].unique()) #pega o primeiro valor de 'title' sem repetição
    nid = df(aux['nid'].unique()).astype(object) #pega o primeiro valor de 'nid' sem repetiçãow
    dat = pd.concat([nid,title,c]).T # concatena os novos dataframes e pega o transposto.



    dat.to_csv('tratado_'+ arquivo, mode = 'a', header = False, index = False) #salva novo .csv   
print('\\\*** Arquivo Pronto ***///')

#fim de programa