#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:57:00 2019

@author: vitor
"""

from pandas import DataFrame as df, read_csv

arquivo = input ("Arquivo a ser modificado ( + .csv):\n") #recebe arquivo
coluna = input("Nome da coluna a ser transformada em linha:\n")#recebe nome da coluna

data = read_csv(arquivo, sep = ',')

for i in data['nid'].unique(): #percorre todos os nids
    
    aux = data[data['nid']==i][['nid','title',coluna]] #seleciona apenas os nids que são iguais a i
    
    ramo = aux[coluna].to_list() #transforma a coluna 'ramno' em lista
    
    title = aux['title'].unique() #pega o primeiro valor de 'title' sem repetição
    nid = aux['nid'].unique() #pega o primeiro valor de 'nid' sem repetição
    
    new = df([ramo],[nid,[title[0]]]) #adiciona nova linha a um dataframe novo
    
    new.to_csv('arquivo_tratado.csv', mode = 'a', header = False) #salva novo .csv
    
print('\\\*** Arquivo Pronto ***///')

#fim de programa