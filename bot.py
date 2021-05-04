#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import random
import sys

sys.path.insert(0, "/Users/Andres/Google Drive/Cursos de Programacion/Python/bot_queen/bot_queen/credenciales.py")
sys.path.insert(0, "/Users/Andres/Google Drive/Programación/Python/bot_queen/bot_queen/listado_canciones.txt")
from credenciales import *
#from listado import *

twitter_API = tweepy.API(auth)

listado_canciones = open ("/Users/Andres/Google Drive/Programación/Python/bot_queen/bot_queen/listado_canciones.txt", "r")
leer_canciones = listado_canciones.readlines ()

#for i in canciones:
#    lyric = random.choice (canciones)
#    twitter_API.update_status (lyric)
#    time.sleep (43200)

for i in leer_canciones:
    seleccion = random.choice (leer_canciones)
    twitter_API.update_status (seleccion)
    time.sleep (43200)

print ('Bot en funcionamiento')

listado_canciones.close()