import requests
from fastapi import FastAPI
from schema.TextBase import TextBase
from domain.TextSummarizer import resumir
app = FastAPI()

cep = 'https://viacep.com.br/ws/{}/json/'
urltempo = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang=pt_br&appid=b77e07f479efe92156376a8b07640ced'

@app.get("/")
async def root():
    return {"message": "ResumoAPI"}


@app.get("/tempo/{ceptxt}")
async def tempo(ceptxt: str) :
    resposta = requests.get(cep.format(ceptxt))
    cidade = resposta.json()['localidade']
    respostatempo = requests.get(urltempo.format(cidade))
    return respostatempo.json()


@app.get("/resumo/{texto}", response_model=TextBase)
async def resumo(texto: str) -> TextBase:
    ''' API de resumo de textos'''
    texto = TextBase(textoinfo=texto)
    return resumir(texto)
