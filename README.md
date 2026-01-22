# 📊 Tratamento de Dados para Dashboard no Power BI

## 📌 Descrição do Projeto

Este projeto tem como objetivo demonstrar o **processo de limpeza, padronização e transformação de dados** utilizando **Python**, simulando um cenário real de preparação de dados para criação de dashboards no **Power BI**.

Os dados originais foram tratados inicialmente no Power BI, e posteriormente foi desenvolvido um **script em Python** para reproduzir o mesmo processo de forma automatizada, seguindo boas práticas de Engenharia e Análise de Dados.

O projeto é voltado para fins de **aprendizado, portfólio profissional e versionamento no GitHub**.

Abaixo está uma visualização do dashboard desenvolvido a partir dos dados tratados em Python:

![Dashboard Power BI](imagens/dashboard_gestao-de-vendas.jpg)

---


## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas** – Manipulação e tratamento de dados
* **RapidFuzz** – Normalização automática de textos (fuzzy matching)
* **Power BI** – Visualização e construção do dashboard

---

## 🗂️ Estrutura do Projeto

```text
📦 dashboard-vendas
 ┣ 📂 dados
 ┃ ┣ dados_brutos.csv
 ┃ ┗ dados_tratados.csv
 ┣ 📂 scripts
 ┃ ┗ tratamento_dados.py
 ┣ 📂 powerbi
 ┃ ┗ power bi vendas.pbix
 ┣ 📂 imagens
 ┃ ┗ dashboard_gestao-de-vendas.png
 ┣ README.md
 ┗ requirements.txt
```

---

## 🔄 Etapas de Tratamento dos Dados

O script em Python executa as seguintes etapas:

### 1️⃣ Carregamento dos dados

* Leitura do arquivo `dados_brutos.csv` utilizando Pandas.

### 2️⃣ Padronização da coluna **Produto**

* Remoção de espaços extras
* Conversão do texto para letras minúsculas
* Padronização para **Primeira letra maiúscula**
* Normalização automática de nomes semelhantes (ex: `Mala` e `Malaa`) usando **fuzzy matching**

### 3️⃣ Tratamento da coluna **Qtde/Preco Unit**

* Separação da coluna em:

  * `quantidade`
  * `preco_unitario`
* Conversão dos valores para formato numérico

### 4️⃣ Criação da coluna **valor_total**

* Cálculo automático:

```text
valor_total = quantidade × preco_unitario
```

### 5️⃣ Exportação dos dados tratados

* Geração do arquivo `dados_tratados.csv`, pronto para uso no Power BI.

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone <url-do-repositorio>
```

### 2️⃣ (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o script de tratamento

```bash
python scripts/tratamento_dados.py
```

Após a execução, o arquivo **dados_tratados.csv** será gerado na pasta `dados`.

---

## 📈 Dashboard

O arquivo gerado é utilizado como base para construção do dashboard no **Power BI**, permitindo análises como:

* Valor total por produto
* Quantidade vendida
* Padronização e confiabilidade dos dados

---

## 🎯 Objetivo Profissional

Este projeto faz parte do meu **portfólio na área de Dados**, demonstrando conhecimentos em:

* Limpeza e preparação de dados
* Automação de processos com Python
* Boas práticas de versionamento
* Integração entre Python e Power BI

---

## 👩‍💻 Autora

**Fabiane Muniz**
Estudante de Análise e Desenvolvimento de Sistemas
Interesse em Análise de Dados e Engenharia de Dados

---

📌 *Sugestões e feedbacks são sempre bem-vindos!*
