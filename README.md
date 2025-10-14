# Gestão do Agronegócio em Python (Capítulos 3 ao 6)

Este projeto foi desenvolvido como atividade da disciplina de Gestão do Agronegócio em Python, abordando os conteúdos dos capítulos 3 a 6:

- Subalgoritmos: funções e procedimentos com passagem de parâmetros.
- Estruturas de dados: listas, tuplas, dicionários e tabela de memória.
- Manipulação de arquivos: leitura e escrita de arquivos texto e JSON.
- Conexão com banco de dados Oracle.

## Estrutura do projeto

```
Gestao_Agronegocio_Python/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── agronegocio.py
├── db_oracle.py
├── utils.py
├── data/
│   ├── sample_data.json
│   └── sample_data.txt
```

## Como executar

1. Criar ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Executar o programa principal:
   ```bash
   python main.py
   ```

4. (Opcional) Configurar `db_oracle.py` com credenciais para testar conexão com Oracle.

---
