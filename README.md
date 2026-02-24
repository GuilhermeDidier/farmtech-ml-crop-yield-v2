# 🌾 FarmTech Solutions - Análise de Rendimento de Safras

## 📋 Sobre o Projeto

Projeto de Machine Learning desenvolvido para a **FarmTech Solutions**, focado na análise e previsão de rendimento de culturas agrícolas em uma fazenda de 200 hectares.

## 🎯 Objetivos

1. **Análise Exploratória de Dados (EDA)**: Compreender padrões e características dos dados
2. **Clusterização**: Identificar tendências de produtividade e detectar outliers
3. **Modelagem Preditiva**: Desenvolver 5 modelos de regressão para prever rendimento de safras

## 📊 Dataset

O dataset `crop_yield.csv` contém as seguintes variáveis:

| Variável | Descrição |
|----------|-----------|
| **Cultura** | Nome da safra medida |
| **Precipitação (mm dia 1)** | Quantidade de chuva em mm/dia |
| **Umidade específica a 2 metros (g/kg)** | Vapor de água no ar por kg de ar seco |
| **Umidade relativa a 2 metros (%)** | Percentual de vapor de água no ar |
| **Temperatura a 2 metros (ºC)** | Temperatura em graus Celsius |
| **Rendimento** | Quantidade produzida em toneladas/hectare (variável alvo) |

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Adicionar o Dataset

Coloque o arquivo `crop_yield.csv` na pasta raiz do projeto.

### 3. Executar os Notebooks

```bash
# Navegar até a pasta notebooks
cd notebooks/

# Abrir Jupyter Notebook
jupyter notebook

# OU usar Jupyter Lab
jupyter lab

# Executar na ordem:
# 1. analise_exploratoria_crop_yield.ipynb
# 2. clusterizacao_crop_yield.ipynb
# 3. modelos_preditivos_crop_yield.ipynb
```

**Nota:** Os notebooks já estão configurados para acessar os dados em `../data/crop_yield.csv`

## 📁 Estrutura do Projeto

```
farmtech_ml_project/
│
├── 📓 notebooks/                               # Notebooks Jupyter
│   ├── analise_exploratoria_crop_yield.ipynb  # Parte 1: Análise Exploratória (EDA)
│   ├── clusterizacao_crop_yield.ipynb         # Parte 2: Clusterização e Outliers
│   ├── modelos_preditivos_crop_yield.ipynb    # Parte 3: 5 Modelos Preditivos
│   └── README.md                              # Guia dos notebooks
│
├── 📁 data/                                    # Datasets
│   ├── crop_yield.csv                         # Dataset original
│   └── README.md                              # Documentação dos dados
│
├── 🔧 scripts/                                 # Scripts auxiliares
│   └── executar_analise.py                    # Script para execução rápida
│
├── 📄 docs/                                    # Documentação adicional
│
├── 📋 Arquivos raiz
│   ├── requirements.txt                       # Dependências Python
│   ├── .gitignore                            # Arquivos ignorados pelo Git
│   └── README.md                             # Este arquivo
```

## 🔍 Análises Realizadas

### 📊 Parte 1: Análise Exploratória de Dados (EDA)
**Notebook:** `analise_exploratoria_crop_yield.ipynb`

- ✅ Carregamento e inspeção inicial dos dados
- ✅ Análise de valores nulos e duplicatas
- ✅ Estatísticas descritivas completas
- ✅ Distribuição das variáveis numéricas (histogramas e boxplots)
- ✅ Matriz de correlação (heatmap)
- ✅ Pairplot entre variáveis por cultura
- ✅ Análise detalhada por tipo de cultura
- ✅ Detecção de outliers (IQR, Z-Score, Isolation Forest)
- ✅ Visualizações interativas e conclusões

### 🎯 Parte 2: Clusterização e Detecção de Outliers
**Notebook:** `clusterizacao_crop_yield.ipynb`

- ✅ K-Means clustering com Elbow Method
- ✅ Análise de Silhouette Score
- ✅ DBSCAN (Density-Based Clustering)
- ✅ Hierarchical Clustering (Agglomerative)
- ✅ Comparação de métodos (métricas: Silhouette, Davies-Bouldin, Calinski-Harabasz)
- ✅ PCA para visualização 2D dos clusters
- ✅ Identificação de padrões de rendimento
- ✅ Análise detalhada de cada cluster

### 🤖 Parte 3: Modelos Preditivos de Regressão
**Notebook:** `modelos_preditivos_crop_yield.ipynb`

- ✅ **Modelo 1:** Regressão Linear
- ✅ **Modelo 2:** Random Forest Regressor
- ✅ **Modelo 3:** Gradient Boosting Regressor
- ✅ **Modelo 4:** Support Vector Regression (SVR)
- ✅ **Modelo 5:** Multi-Layer Perceptron (MLP)
- ✅ Comparação de todos os modelos (R², RMSE, MAE, MAPE)
- ✅ Análise de importância das features
- ✅ Análise de resíduos
- ✅ Validação cruzada (5-Fold)
- ✅ Salvamento do melhor modelo

## 📊 Métricas de Avaliação

Os modelos são avaliados usando:
- **R² (Coefficient of Determination)**: Qualidade do ajuste (quanto maior, melhor)
- **RMSE (Root Mean Squared Error)**: Erro quadrático médio (quanto menor, melhor)
- **MAE (Mean Absolute Error)**: Erro absoluto médio (quanto menor, melhor)
- **MAPE (Mean Absolute Percentage Error)**: Erro percentual médio (quanto menor, melhor)

## 🏆 Resultados

### Modelos Implementados:
1. ✅ **Regressão Linear** - Modelo base, interpretável
2. ✅ **Random Forest** - Ensemble robusto, feature importance
3. ✅ **Gradient Boosting** - Alto desempenho, boosting sequencial
4. ✅ **SVR** - Kernel trick para relações não-lineares
5. ✅ **MLP (Rede Neural)** - Deep learning para padrões complexos

### Algoritmos de Clusterização:
1. ✅ **K-Means** - Particionamento baseado em centroides
2. ✅ **DBSCAN** - Detecção de outliers por densidade
3. ✅ **Hierarchical** - Dendrograma e agrupamento hierárquico

## 📝 Como Usar o Projeto

### Ordem de Execução:
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar notebooks em ordem:
jupyter notebook analise_exploratoria_crop_yield.ipynb  # EDA completa
jupyter notebook clusterizacao_crop_yield.ipynb         # Clusterização
jupyter notebook modelos_preditivos_crop_yield.ipynb    # Modelos ML
```

### Fazer Predições com o Modelo Salvo:
```python
import pickle
import pandas as pd

# Carregar modelo
with open('melhor_modelo_rendimento.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Carregar scaler (se necessário)
with open('scaler_features.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Fazer predição
# features = [Precipitation, Specific Humidity, Relative Humidity, Temperature, Crop_Encoded]
nova_amostra = [[2000, 18, 83, 26, 0]]  # Exemplo
predicao = modelo.predict(nova_amostra)
print(f'Rendimento previsto: {predicao[0]:.2f}')
```

## 👥 Equipe

- [Seu Nome] - RM[XXXXX]
- [Adicionar membros do grupo]

## 🎥 Vídeo Demonstrativo

[Link do vídeo no YouTube - Não listado]

---

**Instituição**: FIAP
**Fase**: 5
**Disciplina**: Machine Learning e Computação em Nuvem
