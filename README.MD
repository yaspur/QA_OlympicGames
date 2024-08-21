# 📚🗨️  QA Olympic Games: Pregunta lo que quieras saber sobre los juegos olimpicos

¿Sabías que chatGPT puede tener informacion actualizada a la fecha? esto se logra creando un Agente de IA y añadiendole herramientas de busqueda en internet.

## Introduccion
📄🧠 Con QA Olympic Games, podras ver como realizar la creacion y como es el funcionamiento de un agente de IA con herramientas que le permiten conectarse a internet
y hacer que ChatGPT sea mas poderoso. 
Para desarrollar esta aplicación en menos de 50 líneas de código necesitaremos:
* ChatGPT API
* Streamlit

## ¿Cómo funciona?
1. Se valida primero si la pregunta tiene que ver con los juegos olimpicos
2. Crea las herramientas de busqueda en internet para el agente (tools), en este caso Wikipedia y GuckDuckSearchGo
3. El agente se encargara de realizar busquedas y una cadena de pensamiento hasta dar con la respuesta indicada a la pregunta
4. Una vez se tiene la respuesta el agente finaliza la ejecucion.

## Instalar preguntaDOC
¡Usar QA Olympic Games es fácil! Aquí están los pasos:
1. Clone o descargue el repositorio en su máquina local.
2. Instale las bibliotecas requeridas ejecutando el siguiente comando en su terminal:
```console
pip install -r requirements.txt
```
3. Ejecute la aplicación con el siguiente comando:
```console
streamlit run app.py
```
4. Obtenga una clave API de OpenAI para usar su API ChatGPT.
5. Escriba su pregunta y disfrute de la magia.