# -*- coding: utf-8 -*-
from unicodedata import normalize
"""
Var Globais
"""
entrada = ">>: "
"""
Funcoes Globais
"""
def normalizar_frase(txt):
  return remover_acentos(txt).lower()
pass
"""
"""
def remover_acentos(txt):
  return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
pass
"""
"""
def readString(frase = None):
  if frase is not None:
    return input(frase)
  else:
    return input(entrada)
pass
