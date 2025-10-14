import json
from typing import List, Dict

def cadastrar_producao(tipo: str, area_ha: float, produtividade_t_ha: float, perda_percentual: float) -> Dict:
    if area_ha < 0 or produtividade_t_ha < 0 or perda_percentual < 0:
        raise ValueError('Valores não podem ser negativos')
    producao = {
        'tipo': tipo,
        'area_ha': float(area_ha),
        'produtividade_t_ha': float(produtividade_t_ha),
        'perda_percentual': float(perda_percentual),
    }
    return producao

def listar_producoes(producoes: List[Dict]):
    if not producoes:
        print('Nenhuma produção registrada.')
        return
    for i, p in enumerate(producoes):
        print(f"[{i}] Tipo: {p['tipo']}, Área: {p['area_ha']} ha, Produtividade: {p['produtividade_t_ha']} t/ha, Perda: {p['perda_percentual']} %")

def calcular_perda_colheita(producao: Dict) -> float:
    area = producao['area_ha']
    produtividade = producao['produtividade_t_ha']
    perda_perc = producao['perda_percentual']
    perda = area * produtividade * (perda_perc / 100.0)
    return perda

def salvar_producoes_para_json(producoes: List[Dict], caminho: str):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(producoes, f, ensure_ascii=False, indent=2)

def carregar_producoes_de_json(caminho: str) -> List[Dict]:
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for p in data:
                p['area_ha'] = float(p['area_ha'])
                p['produtividade_t_ha'] = float(p['produtividade_t_ha'])
                p['perda_percentual'] = float(p['perda_percentual'])
            return data
    except FileNotFoundError:
        return []
