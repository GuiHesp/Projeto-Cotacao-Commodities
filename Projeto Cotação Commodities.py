#!/usr/bin/env python
# coding: utf-8

# ## Desafio:
# Trabalhamos em uma importadora e compramos e vendemos commodities:
# - soja,milho,trigo,petróleo,etc
# 
# Precisamos pegar na internet a cotação de todas elas e ver se está abaixo do nosso preço ideal de compra.
# 
# Usaremos selenium, webdriver.

# In[6]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")


# In[8]:


import pandas as pd

tabela = pd.read_excel(r"TabelaProdutos.xlsx")
display(tabela)


# In[10]:


for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    produto = produto.replace("ó", "o").replace("ã", "a").replace("á", "a").replace("é", "e").replace("ç", "c").replace("ú", "u")
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    navegador.get(link)
    
    preco = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
    preco = preco.replace(".", "").replace(",", ".")
    tabela.loc[linha, "Preço Atual"] = float(preco)

display(tabela)
print(tabela.info())


           
        


# In[4]:


tabela["Comprar"] = tabela["Preço Atual"] <= tabela["Preço Ideal"]
display(tabela)

