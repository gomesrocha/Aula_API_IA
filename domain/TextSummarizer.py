from schema.TextBase import TextBase
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

def resumir(texto: TextBase):
    parser = PlaintextParser.from_string(texto.textoinfo,
                                         Tokenizer('portuguese'))
    sumarizador = LuhnSummarizer()
    resumo = sumarizador(parser.document, 1)

    for i in resumo:
        texto = f"Resumo: {i}"
    return TextBase(textoinfo=texto)
