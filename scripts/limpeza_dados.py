import pandas as pd
from rapidfuzz import process, fuzz

# ==============================
# 1. Carregar dados
# ==============================
# Lê o arquivo que está na pasta "dados"
df = pd.read_excel('../dados/dados_brutos.xlsx')

print('Colunas do dataset:')
print(df.columns)
print('\nPrimeiras linhas:')
print(df.head())

# ==============================
# Padronizar coluna Produto
# ==============================

# Remove espaços extras no início e no fim do texto
df['Produto'] = df['Produto'].str.strip()

# Converte todas as letras para minúsculas
df['Produto'] = df['Produto'].str.lower()

# Coloca a primeira letra de cada palavra em maiúscula
df['Produto'] = df['Produto'].str.title()

print('\nProdutos após padronização:')
print(df['Produto'].head())


# ==============================
# Normalização automática da coluna Produto (fuzzy matching)
# ==============================

# Lista de produtos únicos existentes no dataset
produtos_unicos = df['Produto'].dropna().unique()

# Lista que armazenará os produtos já tratados
produtos_padronizados = {}

# Percorre cada produto único
for produto in produtos_unicos:
    # Compara o produto atual com os já padronizados
    if not produtos_padronizados:
        # Primeiro produto vira padrão
        produtos_padronizados[produto] = produto
    else:
        # Busca o produto mais parecido entre os já padronizados
        melhor_match, similaridade, _ = process.extractOne(
            produto,
            produtos_padronizados.keys(),
            scorer=fuzz.ratio
        )

        # Se for suficientemente parecido, considera o mesmo produto
        if similaridade >= 85:
            produtos_padronizados[produto] = melhor_match
        else:
            # Caso contrário, cria um novo padrão
            produtos_padronizados[produto] = produto

# Aplica a padronização automática no DataFrame
df['Produto'] = df['Produto'].map(produtos_padronizados)

print('\nProdutos após normalização automática:')
print(df['Produto'].value_counts())

# ==============================
# 2. Tratar coluna Qtde/Preco Unit
# ==============================
# Quebra a coluna "Qtde/Preco Unit" em duas colunas novas
# O split('/') separa o texto usando a barra como divisor
# expand=True cria duas colunas separadas e df insere os novos nomes das colunas
df[['quantidade', 'preco_unitario']] = df['Qtde/Preco Unit'].str.split('/', expand=True)

# Remove espaços extras
df['quantidade'] = df['quantidade'].str.strip()
df['preco_unitario'] = df['preco_unitario'].str.strip()

# Substitui vírgula por ponto
# Dados no padrão brasileiro usam vírgula como separador decimal
# O Python exige ponto, então fazemos a conversão antes do to_numeric
df['preco_unitario'] = df['preco_unitario'].str.replace(',', '.', regex=False)

# Converte para número
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce')
df['preco_unitario'] = pd.to_numeric(df['preco_unitario'], errors='coerce')

df = df.drop(columns=['Qtde/Preco Unit'])

print('\nColunas após tratamento:')
print(df[['quantidade', 'preco_unitario']].head())

# ==============================
# Criar coluna Valor Total
# ==============================

# Multiplica a quantidade pelo preço unitário
# O pandas faz essa operação linha a linha automaticamente
df['valor_total'] = df['quantidade'] * df['preco_unitario']
df['valor_total'] = df['valor_total'].round(2)

print(df[['quantidade', 'preco_unitario', 'valor_total']].head())

# ==============================
# 4. Salvar dados tratados
# ==============================
df.to_csv(
    '../dados/dados_tratados.csv',
    index=False,
    sep=';',
    encoding='utf-8-sig'
)
print('\nScript executado com sucesso!')
