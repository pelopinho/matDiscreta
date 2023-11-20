def probabilidade(evento, espaco_amostral):
  
  # Calcula o número de elementos do espaço amostral.
  n_espaco_amostral = len(espaco_amostral)

  # Calcula o número de elementos do evento.
  n_evento = len(evento)

  # Retorna a probabilidade do evento.
  return n_evento / n_espaco_amostral


if __name__ == "__main__":
  # Exemplo de cálculo da probabilidade de lançar um dado e obter um número par.
  espaço_amostral = [1, 2, 3, 4, 5, 6]
  evento = [2, 4, 6]

  probabilidade = probabilidade(evento, espaço_amostral)

  print("Probabilidade de obter um número par:", probabilidade)
