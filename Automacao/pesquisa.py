# Biblioteca Selenium, Webdriver
# Baixar Chrome driver

#01 - Baixar chrone driver e coloca-lo na mesma pasta do python 
   # https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/win32/chromedriver-win32.zip

#02 - Instalar biblioteca Selenium; pip install selenium

#03 - Instalar Web Driver Manager; pip install webdriver_manager

# Importar bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Importando serviço de utilização do navegador
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By


# Criando um serviço do Chrome
servico = Service(ChromeDriverManager().install())

# Criar uma variável para usar o navegador
# navegarGoogle = webdriver.Chrome(service=servico)
# navegarSenai = webdriver.Chrome(service=servico)
navegarMercadoLivre = webdriver.Chrome(service=servico)


# Abrindo o site do Gooogle
#navegarGoogle.get("https://www.google.com")

# Abrindo o site do Senai
#navegarSenai.get("https://www.sp.senai.br/cursos")


# Abrindo o site do Mercado Livre
navegarMercadoLivre.maximize_window() # Maximizando a janela
navegarMercadoLivre.get("https://www.mercadolivre.com.br/")

pesquisa = 'notebook' # Texto para inserir na barra de pesquisa

navegarMercadoLivre.find_element('xpath', '//*[@id="cb1-edit"]').send_keys(pesquisa) # Inserindo texto atraves da barra de pesquisa pelo elemento Xpath

navegarMercadoLivre.find_element('xpath', '/html/body/header/div/div[2]/form/button').click() # Comando para clickar no item selecionado; botão pesquisar

navegarMercadoLivre.find_element('xpath', '//*[@id=":R2m55e6:-display-values"]').click() # Elemento da ordenagem dos itens; selecionando menor valor

navegarMercadoLivre.find_element('xpath', '//*[@id=":R2m55e6:-menu-list-option-price_asc"]').click() # Selecionando para ordenar por menor valor

# Pausar programa
input('Aperte enter para pausar\n')