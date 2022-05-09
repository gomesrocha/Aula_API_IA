from pydantic import BaseModel


class TextBase(BaseModel):
    ''' Schema de entrada e saída de textos na API'''
    textoinfo: str
