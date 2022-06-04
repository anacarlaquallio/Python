#!/usr/bin/env python
# coding: utf-8

# # Exercícios NumPy  
# 
# Agora que aprendemos sobre NumPy, vamos testar seu conhecimento. Começaremos com algumas tarefas simples, para depois entrarmos nas perguntas mais complicadas.

# #### Importe NumPy como np

# In[2]:


import numpy as np


# #### Crie uma matriz de 10 zeros

# In[2]:


np.zeros(10)


# #### Crie uma matriz de 10 ones

# In[3]:


np.ones(10)


# #### Crie uma matriz de 10 cincos

# In[4]:


np.ones(10) * 5


# #### Crie um array de inteiros de 10 até 50

# In[5]:


np.arange(10,51)


# #### Crie um array dos numeros pares de 10 até 50

# In[6]:


np.arange(10,51,2)


# #### Criei uma matriz 3x3 com valores variando de 0 até 8

# In[7]:


np.arange(9).reshape(3,3)


# #### Crie uma matriz identidade 3x3

# In[8]:


np.eye(3)


# #### Use NumPy para gerar números aleatórios entre 0 e 1

# In[15]:


np.random.rand(1)


# #### Use Numpy para gerar um array de 25 números aleatórios tirados de uma distribuição normal.

# In[33]:


np.random.randn(25)


# #### Crie a seguinte matriz:

# In[35]:


np.arange(1,101).reshape(10,10) / 100


# #### Crie um array de tamanho 20 igualmente espaçado entre 0 e 1.

# In[36]:


np.linspace(0,1,20)


# ## Indexação Numpy e Seleção
# 
# Agora você receberá algumas matrizes e será solicitado a replicar as saídas resultantes da matriz:

# In[4]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[39]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO RODAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A MATRIZ DESEJADA


# In[40]:


mat[2:,1:]


# In[29]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[41]:


mat[3,4]


# In[30]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[42]:


mat[:3,1:2]


# In[31]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[46]:


mat[4,:]


# In[32]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[49]:


mat[3:5,:]


# ### Agora faça o seguinte

# #### Obter a soma de todos os valores no "mat"

# In[50]:


mat.sum()


# #### Obter o desvio padrão dos valores em mat

# In[51]:


mat.std()


# #### Obter a soma de todas as colunas em mat

# In[53]:


mat.sum(axis=0)

