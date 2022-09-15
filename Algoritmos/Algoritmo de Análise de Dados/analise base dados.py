import pandas as pd
import numpy
import openpyxl
import plotly.express as px

#ler a tabela
tabela = pd.read_csv(r'D:\Intensivão Python\Aula 02\telecom_users.csv')

#visualização da tabela
print(tabela)

#remoção de informações que só atrapalham
tabela = tabela.drop('Unnamed: 0', axis=1)

    #tratamento de dados

#ajudar tipo do "TotalGasto" de "objetct" para "float64"
tabela["TotalGasto"] = pd.to_numeric(tabela['TotalGasto'], errors= 'coerce')

#informações vazias - colunas (remoção)
tabela = tabela.dropna(how = 'all', axis = 1)

#informações vazias - linhas com algum dado vazio (remoção)
tabela = tabela.dropna(how ='any', axis = 0)

print(tabela.info())

#com valores corretos e dados vazios removidos, agora a analise de dados
#churn de 26%


print(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format)) #contar o valor de churns em porcentagem


#tabela com as colunas

print(tabela.columns)

#gráfico com motivações de cancelamentos (churns)
for coluna in tabela.columns:
    #criar grafico
    grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True)
    #mostrar graifoc
    grafico.show()


# Motivações de cancelamento (analise final)

## Clientes com contrato mensal tem maior chance de cancelamento

## Familias maiores cancelam menos

## Quanto mais serviços o cliente possui, menor a chance de ele

## Clientes que pagam via boleto tem chance maior de cancelamento##