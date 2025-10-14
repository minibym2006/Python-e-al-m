from agronegocio import (
    cadastrar_producao,
    listar_producoes,
    salvar_producoes_para_json,
    carregar_producoes_de_json,
    calcular_perda_colheita,
)
from db_oracle import OracleConnector
from utils import ler_texto_exemplo, validar_float, validar_int
import os

DATA_JSON = os.path.join('data', 'sample_data.json')

def menu():
    print("\n=== Gestão do Agronegócio — Capítulos 3-6 (Demo) ===")
    print("1. Cadastrar produção")
    print("2. Listar produções")
    print("3. Calcular perda na colheita (ex: cana)")
    print("4. Salvar em JSON")
    print("5. Carregar de JSON")
    print("6. Ler arquivo de texto exemplo")
    print("7. Testar conexão Oracle (opcional)")
    print("0. Sair")

def main():
    producoes = []

    while True:
        menu()
        escolha = input('Escolha uma opção: ').strip()
        if escolha == '1':
            tipo = input('Tipo (ex: cana, soja): ').strip()
            area = validar_float(input('Área (ha): '))
            produtividade = validar_float(input('Produtividade (t/ha): '))
            perda_perc = validar_float(input('Perda estimada (%) — ex 5 para 5%: '))
            prod = cadastrar_producao(tipo, area, produtividade, perda_perc)
            producoes.append(prod)
            print('Produção cadastrada com sucesso!')
        elif escolha == '2':
            listar_producoes(producoes)
        elif escolha == '3':
            if not producoes:
                print('Nenhuma produção cadastrada.')
                continue
            idx = validar_int(input('Índice da produção (começa em 0): '))
            try:
                prod = producoes[idx]
            except Exception:
                print('Índice inválido.')
                continue
            perda = calcular_perda_colheita(prod)
            print(f"Perda estimada: {perda:.2f} toneladas")
        elif escolha == '4':
            salvar_producoes_para_json(producoes, DATA_JSON)
            print('Salvo em', DATA_JSON)
        elif escolha == '5':
            producoes = carregar_producoes_de_json(DATA_JSON)
            print('Produções carregadas:', len(producoes))
        elif escolha == '6':
            conteudo = ler_texto_exemplo(os.path.join('data', 'sample_data.txt'))
            print('\n--- Conteúdo do arquivo de texto ---\n')
            print(conteudo)
        elif escolha == '7':
            print('Tentando conectar ao Oracle...')
            conn = OracleConnector()
            try:
                conn.connect()
                print('Conectado com sucesso!')
            except Exception as e:
                print('Erro na conexão:', e)
            finally:
                conn.close()
        elif escolha == '0':
            print('Encerrando...')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()
