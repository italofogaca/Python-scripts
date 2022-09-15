from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()

#dolar
navegador.get('https://www.google.com/')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao dolar')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

#euro

navegador.get('https://www.google.com/')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao euro')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)

#ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')

cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',','.')

print(cotacao_ouro)


navegador.quit()

#atualizacao base de dados


tabela = pd.read_excel(r'D:\Intensivão Python\Aula 03\Produtos.xlsx')

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)

tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)

tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

#preço de compra = preço original * cotação
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela ['Cotação']

#preço de venda = preço de compra * margem
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela ['Margem']

print(tabela)

#exportando tabela atualizada

tabela.to_excel(r'D:\Intensivão Python\Aula 03\Produtos v2.xlsx', index=False)