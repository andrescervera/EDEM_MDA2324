#!/bin/bash

import requests
from requests.models import Response


URL: str = "https://api.chucknorris.io/jokes/random"


def num_chistes ():
 
    for i in range(1, 11):
        respuesta: requests.Response = requests.get(url = URL)
        estado: int = respuesta.status_code
        datos = respuesta.json()
        if estado == 200:
            frase_chuck: str = datos['value']
            print(f'{frase_chuck}')
            f = open('fichero_chuck.txt','a')
            f.write(f'{frase_chuck}' + '\n')
num_chistes()