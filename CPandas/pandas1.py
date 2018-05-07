
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


datos_archivo = 'data/nyc_data.csv'
# datos recopilados por taxis en Manhattan


# In[4]:


datos = pd.read_csv(datos_archivo,parse_dates=['pickup_datetime',
                                              'dropoff_datetime'])
# datos es un objeto DataFrame
# DataFrame es una tabla que contiene:
# filas -> observaciones o muestras
# columnas -> atributos o variables

# Los DataFrame pueden contener texto, numeros, fechas y otros tipos


# In[5]:


datos.head(3) #Las primeras tres filas de nuestra tabla


# In[6]:


datos.tail(3) #Las últimas cuatro filas de nuestra tabla


# In[8]:


datos.describe() # datos básicos de todas las columnas


# In[9]:


datos.columns # lista de columnas


# In[16]:


p_lng = datos.pickup_longitude
p_lat = datos.pickup_latitude
d_lng = datos.dropoff_longitude
d_lat = datos.dropoff_latitude
# datos.nombre de columna -> nos da solo esa columna
# tambien puede ser datos['nombre de columna']


# In[17]:


p_lat


# In[18]:


# Debemos crear una función para pasar los datos de latitud y longitud
# a coordenadas

def lat_lng_a_pixeles(lat,lng):
    lat_rad = lat * np.pi / 180
    lat_rad = np.log(np.tan((lat_rad + np.pi / 2.0)/2.0))
    x = 100 * (lng + 180) / 360
    y = 100 * (lat_rad - np.pi) / (2 * np.pi)
    return x,y


# In[19]:


px, py = lat_lng_a_pixeles(p_lat,p_lng)


# In[20]:


px


# In[21]:


plt.scatter(px,py)


# In[25]:


plt.figure(figsize=(8,6)) # podemos especificar tamaño de figura
plt.scatter(px, py, s=.1, alpha=.03)
# s = tamaño de puntos, alpha = opacidad
plt.axis('equal')
plt.xlim(29.40,29.55)
plt.ylim(-37.63,-37.54)
plt.axis('off')


# In[29]:


px.count(),px.min(),px.max()
# cantidad, minimo, maximo


# In[30]:


px.mean(), px.median(), px.std()
# media, mediana, desv estandar


# In[34]:


datos.trip_distance


# In[35]:


datos.trip_distance.hist(bins=np.linspace(0,10,100))
# Pandas también nos permite realizar gráficas


# In[36]:


# Para seleccionar una o unas filas en específico
# data.loc[numero de fila]
datos.loc[3]


# In[37]:


datos.loc[3:5] # incluye al 5


# In[38]:


datos.loc[[0,10]] # fila 0 y 10


# In[48]:


datos.loc[10:30,['trip_distance','trip_time_in_secs']]


# In[49]:


# indexar con booleanos
datos.loc[datos.trip_distance > 50]

