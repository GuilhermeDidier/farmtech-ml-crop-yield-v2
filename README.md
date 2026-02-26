# 🌾 FarmTech Solutions - Análise de Rendimento de Safras

**Instituição:** FIAP
**Fase:** 5
**Disciplinas:** Machine Learning e Computação em Nuvem

---

## 👥 Equipe

| Nome | RM |
|---|---|
| Davis Roberto | RM567941 |
| Guilherme Chan | RM567722 |
| Deivid Paula da Silva Oliveira | RM566752 |
| Guilherme Paes Barreto Didier Garcia | RM568457 |

---

## 📋 Sobre o Projeto

Projeto desenvolvido para a **FarmTech Solutions**, empresa de IA prestando serviços para uma fazenda de médio porte de **200 hectares** (aproximadamente 210 campos de futebol). O objetivo é analisar dados de condições de solo e temperatura para **prever o rendimento de safras** e **explorar tendências de produtividade** por meio de Machine Learning supervisionado e não supervisionado.

---

## 🎯 Objetivos

1. **Análise Exploratória de Dados (EDA):** Compreender padrões, distribuições e qualidade dos dados
2. **Clusterização:** Identificar tendências de produtividade e detectar cenários discrepantes (outliers)
3. **Modelagem Preditiva:** Desenvolver 5 modelos de regressão para prever o rendimento de safras
4. **Computação em Nuvem:** Estimar e comparar custos de hospedagem da API + ML na AWS

---

## 📊 Dataset

O dataset `crop_yield.csv` contém **156 registros** de 4 culturas agrícolas com as seguintes variáveis:

| Variável | Descrição |
|---|---|
| **Cultura** | Nome da safra medida |
| **Precipitação (mm dia 1)** | Quantidade de chuva em mm/dia |
| **Umidade específica a 2 metros (g/kg)** | Vapor de água no ar por kg de ar seco |
| **Umidade relativa a 2 metros (%)** | Percentual de vapor de água no ar |
| **Temperatura a 2 metros (ºC)** | Temperatura em graus Celsius |
| **Rendimento** | Quantidade produzida em toneladas/hectare (variável alvo) |

---

## 📁 Estrutura do Projeto

```
farmtech-ml-crop-yield/
│
├── 📓 notebooks/
│   ├── GuilhermeDidierGarcia_rm568457_pbl_fase4_eda.ipynb       # Parte 1: EDA
│   ├── GuilhermeDidierGarcia_rm568457_pbl_fase4_cluster.ipynb   # Parte 2: Clusterização
│   └── GuilhermeDidierGarcia_rm568457_pbl_fase4_modelos.ipynb   # Parte 3: Modelos Preditivos
│
├── 📁 data/
│   └── crop_yield.csv          # Dataset original
│
├── 🔧 scripts/
│   └── executar_analise.py     # Script auxiliar de execução
│
├── 📋 requirements.txt         # Dependências Python
├── .gitignore
└── README.md                   # Este arquivo
```

---

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar os Notebooks (na ordem)

```bash
# Abrir Jupyter
jupyter notebook

# Executar na seguinte ordem:
# 1. GuilhermeDidierGarcia_rm568457_pbl_fase4_eda.ipynb
# 2. GuilhermeDidierGarcia_rm568457_pbl_fase4_cluster.ipynb
# 3. GuilhermeDidierGarcia_rm568457_pbl_fase4_modelos.ipynb
```

> 💡 **Recomendação:** Use o [Google Colab](https://colab.research.google.com) para rodar sem precisar instalar nada localmente. Faça upload do `crop_yield.csv` quando solicitado.

---

## 📓 Notebooks Jupyter

Acesse os notebooks completos diretamente no repositório:

1. **[Parte 1: Análise Exploratória de Dados (EDA)](notebooks/GuilhermeDidierGarcia_rm568457_pbl_fase4_eda.ipynb)**
   - Carregamento e inspeção dos dados
   - Análise de distribuições e correlações
   - Detecção de outliers

2. **[Parte 2: Clusterização](notebooks/GuilhermeDidierGarcia_rm568457_pbl_fase4_cluster.ipynb)**
   - K-Means, DBSCAN e Hierarchical Clustering
   - Análise de padrões de produtividade
   - Comparação de métodos

3. **[Parte 3: Modelos Preditivos](notebooks/GuilhermeDidierGarcia_rm568457_pbl_fase4_modelos.ipynb)**
   - 5 modelos de regressão implementados
   - Comparação de métricas (R², RMSE, MAE, MAPE)
   - Validação cruzada e análise de resíduos

---

## 🔍 Análises Realizadas

### 📊 Parte 1 — Análise Exploratória de Dados (EDA)

- Carregamento e inspeção inicial: 156 registros, 6 colunas, zero valores nulos
- Análise de distribuições, histogramas e boxplots
- Matriz de correlação e pairplot por cultura
- Detecção de outliers com IQR, Z-Score e Isolation Forest
- **Principal achado:** O tipo de cultura é o fator dominante no rendimento, com Oil palm fruit produzindo em média ~175.804 kg/ha contra ~8.883 kg/ha do Cacau

### 🎯 Parte 2 — Clusterização

- **K-Means** com Elbow Method → K=8 (Silhouette Score: 0.391)
- **DBSCAN** (Density-Based) → identificou baixa densidade, não adequado para este dataset
- **Hierarchical Clustering** → Silhouette Score: 0.354
- **Principal achado:** K-Means foi o melhor método; os clusters se organizam principalmente pelo tipo de cultura

### 🤖 Parte 3 — Modelos Preditivos

| Modelo | R² (Teste) | RMSE | MAE | MAPE (%) |
|---|---|---|---|---|
| **🏆 Random Forest** | **0.9944** | **4.640** | **2.748** | **7.99%** |
| Gradient Boosting | 0.9902 | 6.176 | 3.186 | 8.58% |
| Regressão Linear | -0.1015 | 65.365 | 53.724 | 361.73% |
| SVR | -0.3082 | 71.235 | 38.837 | 63.97% |
| MLP (Rede Neural) | -0.1728 | 67.447 | 41.393 | 155.85% |

**Melhor modelo:** Random Forest com R² = 0.9944 e MAPE de apenas 7.99%

---

## 🎥 Vídeos Demonstrativos

| Entrega | Link |
|---|---|
| Entrega 1 — Machine Learning | *(link a ser adicionado)* |
| Entrega 2 — Computação em Nuvem | *(link a ser adicionado)* |

---

---

# ☁️ Entrega 2 — Computação em Nuvem (AWS)

## 📌 Contexto

O modelo de Machine Learning desenvolvido na Entrega 1 precisa ser hospedado em uma infraestrutura de nuvem para funcionar como uma **API em produção**, recebendo dados dos sensores agrícolas em tempo real e retornando previsões de rendimento de safra.

Para isso, realizamos uma estimativa de custos utilizando a **AWS Pricing Calculator**, comparando duas regiões: **São Paulo (Brasil)** e **N. Virgínia (EUA)**.

---

## ⚙️ Especificações da Máquina

A instância selecionada foi a **Amazon EC2 t3.micro**, que atende exatamente às especificações solicitadas:

| Especificação | Requisito | t3.micro |
|---|---|---|
| vCPUs | 2 CPUs | ✅ 2 vCPUs |
| Memória RAM | 1 GiB | ✅ 1 GiB |
| Rede | Até 5 Gigabit | ✅ Up to 5 Gigabit |
| Armazenamento | 50 GB | ✅ 50 GB EBS (gp3) |
| Sistema Operacional | Linux | ✅ Linux |
| Modelo de pagamento | On-Demand 100% | ✅ On-Demand |
| Uso mensal | 100% | ✅ 730 horas/mês |

---

## 💰 Comparação de Custos

### 🇧🇷 Região: South America (São Paulo) — sa-east-1

| Item | Custo |
|---|---|
| Instância t3.micro (On-Demand, 730h) | $12,26 USD/mês |
| Armazenamento EBS 50 GB (gp3) | $7,60 USD/mês |
| **Total Mensal** | **$19,86 USD/mês** |
| **Total Anual** | **$238,32 USD/ano** |

### 🇺🇸 Região: US East (N. Virginia) — us-east-1

| Item | Custo |
|---|---|
| Instância t3.micro (On-Demand, 730h) | $7,59 USD/mês |
| Armazenamento EBS 50 GB (gp3) | $4,00 USD/mês |
| **Total Mensal** | **$11,59 USD/mês** |
| **Total Anual** | **$139,08 USD/ano** |

---

## 📊 Resumo Comparativo

| Região | Custo Mensal | Custo Anual | Diferença |
|---|---|---|---|
| 🇧🇷 São Paulo (BR) | $19,86 USD | $238,32 USD | +71% mais caro |
| 🇺🇸 N. Virgínia (EUA) | $11,59 USD | $139,08 USD | — (referência) |

> **N. Virgínia é aproximadamente 41% mais barata que São Paulo.**
> A economia anual seria de aproximadamente **$99,24 USD**.

---

## 🏆 Qual Região Escolher?

### Análise 1 — Apenas pelo Custo

Se o critério fosse somente o custo, a escolha seria **N. Virgínia (EUA)**, pois é significativamente mais barata ($11,59/mês vs $19,86/mês).

### Análise 2 — Considerando Restrições Legais e Técnicas

No contexto deste projeto, existem **dois fatores adicionais críticos** que precisam ser considerados:

#### 📜 LGPD — Lei Geral de Proteção de Dados (Lei nº 13.709/2018)

Os sensores agrícolas coletam dados operacionais da fazenda que podem conter informações sensíveis sobre produção, localização e estratégias do negócio. A **LGPD** exige que dados de cidadãos e empresas brasileiras sejam armazenados e tratados com garantias específicas. A transferência internacional de dados é permitida, mas exige mecanismos adicionais de proteção (cláusulas contratuais, adequação do país receptor), o que aumenta a complexidade jurídica e operacional.

#### ⚡ Latência — Acesso Rápido aos Dados dos Sensores

O enunciado menciona explicitamente que há necessidade de **acessar rapidamente os dados dos sensores**. Uma API hospedada na Virgínia do Norte (a ~8.000 km do Brasil) teria latência significativamente maior do que uma hospedada em São Paulo, prejudicando a resposta em tempo real do sistema de irrigação.

### ✅ Decisão Final: São Paulo (Brasil)

**Escolhemos a região de São Paulo** como opção mais adequada para este projeto pelos seguintes motivos:

1. **Conformidade com a LGPD:** Os dados dos sensores e do sistema agrícola permanecem em território nacional, eliminando complexidades legais de transferência internacional de dados
2. **Menor latência:** A API hospedada em São Paulo responde com muito mais rapidez aos sensores instalados na fazenda brasileira, garantindo decisões de irrigação em tempo real
3. **Soberania dos dados:** Dados estratégicos do negócio agrícola ficam sob jurisdição brasileira
4. **Simplicidade operacional:** Sem necessidade de contratos de adequação para transferência internacional de dados

> 💡 **Conclusão:** Embora a N. Virgínia seja ~41% mais barata ($99,24 USD de economia anual), o custo adicional de São Paulo é justificado pela **conformidade legal**, **menor latência** e **segurança dos dados**. Para um sistema de suporte à decisão agrícola em tempo real, esses fatores superam a diferença de custo.

---

## 🛠️ Configuração Utilizada na Calculadora AWS

- **Ferramenta:** [AWS Pricing Calculator](https://calculator.aws)
- **Tipo de instância:** Amazon EC2 t3.micro
- **Tenancy:** Shared Instances
- **Sistema Operacional:** Linux
- **Workload:** Constant usage
- **Payment Option:** On-Demand (100%)
- **Usage:** 730 horas/mês (uso contínuo)
- **Armazenamento:** Amazon EBS — General Purpose SSD (gp3) — 50 GB
- **Snapshots:** Nenhum

---

*Estimativa gerada em fevereiro de 2026. Preços sujeitos a alterações pela AWS.*
