# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:47:01 2020

@author: tiago
"""


import numpy as np  # procesamiento matricial
import pandas as pd
import math

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt  # para mostrar imagenes
plt.rcParams['image.cmap'] = 'gray'
get_ipython().magic('matplotlib inline')
# para leer/guardar videos
import imageio



# Crear un objeto lector de videos
file_name= "4.Video3 Terapia Rami.mp4"
print("Abriendo video...")
vid_reader = imageio.get_reader(file_name)

# ver los metadatos del video
mdata = vid_reader.get_meta_data()
print("La data es:")
print(mdata)

df = pd.DataFrame(mdata, columns = ['plugin', 'Numero de frames', 'Versión del ffmpeg.', 
'Codec', 'Pix_fmt', 'fps', 'source_size', 'size', 'duration (Segundos)'])

df.to_excel('Metadatos.xlsx')