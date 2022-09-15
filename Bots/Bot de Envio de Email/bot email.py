import pyautogui
import pyperclip
import time
import pandas as pd

#entrando no site para baixar o arquivo
pyautogui.PAUSE = 0.2
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

#posição do mouse ja detectada por pyautogui.position()

pyautogui.click(321,253, clicks=2)
time.sleep(2)

#download base de dados
pyautogui.click(317,325) #posição arquivo
time.sleep(2)
pyautogui.click(1728,156) #posição dos 3 pontos
time.sleep(2)
pyautogui.click(1490,487) #posição do download
time.sleep(7)

#ler o arquivo
tabela = pd.read_excel(r"C:\Users\Italo\Downloads\Vendas - Dez.xlsx")
quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()


#entrar no email
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://outlook.live.com/mail/0/')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(231, 135)  # clicar no botão de novo
time.sleep(2)

pyautogui.write('teste@hotmail.com')  # escreve o destinatario
time.sleep(2)

pyautogui.press('tab')  # selecionar o email
time.sleep(2)

pyautogui.press('tab')  # passar para o canto de assunto
time.sleep(2)

pyautogui.write('relatório de vendas teste')  # escrever assunto
time.sleep(2)

pyautogui.press('tab')  # passar ao corpo do email
time.sleep(2)

texto = f"""Queridos, boa tarde!

Faturamento de ontem foi de: R$ {faturamento: ,.2f}
A quantidade de produtos foi: {quantidade:,}

Atenciosamente, Italo.
"""""
pyperclip.copy(texto) #escrever email
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

pyautogui.click(705.328) #enviar o email
