import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


## base de dados

tabela = pd.read_csv(r'D:\Intensivão Python\Aula 04\advertising.csv')

#criar grafico
sns.heatmap(tabela.corr(), cmap = 'Wistia', annot=True)

#exibir grafico
plt.show()

#separando treinos e teste

from sklearn.model_selection import train_test_split
y = tabela["Vendas"]
x = tabela[["TV", "Radio", "Jornal"]]

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

#teste modelo

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor ()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

#avaliar melhor modelo

from sklearn.metrics import r2_score

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

print (r2_score(y_teste, previsao_regressaolinear))
print (r2_score(y_teste, previsao_arvoredecisao))

#visualização dos testes de previsão

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

#fazendo nova previsão

novos = pd.read_csv(r'D:\Intensivão Python\Aula 04\novos.csv')

print(modelo_arvoredecisao.predict(novos))

sns.barplot(x=x_treino.columns, y=modelo_arvoredecisao.feature_importances_)
plt.show()

##fim