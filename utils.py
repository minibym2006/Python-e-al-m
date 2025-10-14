def validar_float(valor: str) -> float:
    while True:
        try:
            v = float(valor)
            return v
        except Exception:
            valor = input('Valor inválido. Digite um número: ')

def validar_int(valor: str) -> int:
    while True:
        try:
            v = int(valor)
            return v
        except Exception:
            valor = input('Valor inválido. Digite um inteiro: ')

def ler_texto_exemplo(caminho: str) -> str:
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()
