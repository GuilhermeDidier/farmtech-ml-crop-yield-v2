# 📓 Notebooks do Projeto

Este diretório contém todos os notebooks Jupyter do projeto, organizados em ordem de execução.

## 📋 Ordem de Execução

Execute os notebooks na seguinte ordem:

### 1️⃣ Análise Exploratória de Dados (EDA)
**Arquivo:** `GuilhermeDidierGarcia_rm568457_pbl_fase4_eda.ipynb`

**Conteúdo:**
- Carregamento e inspeção do dataset
- Análise de qualidade dos dados (nulos, duplicatas)
- Estatísticas descritivas completas
- Visualizações (histogramas, boxplots, correlação)
- Análise por tipo de cultura
- Detecção de outliers (IQR, Z-Score, Isolation Forest)

**Tempo estimado:** 5-10 minutos

---

### 2️⃣ Análise de Clusterização
**Arquivo:** `GuilhermeDidierGarcia_rm568457_pbl_fase4_cluster.ipynb`

**Conteúdo:**
- K-Means clustering com Elbow Method
- Determinação do número ótimo de clusters
- DBSCAN para detecção de outliers por densidade
- Hierarchical Clustering (Agglomerative)
- Comparação dos métodos
- Visualização com PCA (redução dimensional)
- Análise dos clusters formados

**Tempo estimado:** 10-15 minutos

---

### 3️⃣ Modelos Preditivos de Regressão
**Arquivo:** `GuilhermeDidierGarcia_rm568457_pbl_fase4_modelos.ipynb`

**Conteúdo:**
- Preparação dos dados (encoding, normalização)
- Treinamento de 5 modelos:
  1. Regressão Linear
  2. Random Forest Regressor
  3. Gradient Boosting Regressor
  4. Support Vector Regression (SVR)
  5. Multi-Layer Perceptron (MLP)
- Comparação de métricas (R², RMSE, MAE, MAPE)
- Análise de importância das features
- Validação cruzada
- Salvamento do melhor modelo

**Tempo estimado:** 15-20 minutos

---

## 🚀 Como Executar

### Método 1: Jupyter Notebook
```bash
# Navegar até a pasta do projeto
cd farmtech-ml-crop-yield-v2

# Abrir Jupyter
jupyter notebook

# Executar os notebooks em ordem
```

### Método 2: Jupyter Lab
```bash
# Abrir Jupyter Lab
jupyter lab

# Navegar até a pasta notebooks e executar
```

### Método 3: VS Code
```bash
# Abrir VS Code na pasta do projeto
code .

# Abrir os notebooks e executar célula por célula
```

---

## 📊 Resultados Esperados

### Análise Exploratória
- ✅ Dataset limpo (sem nulos ou duplicatas)
- ✅ 4 tipos de culturas identificadas
- ✅ ~10% de outliers detectados

### Clusterização
- ✅ 2 clusters ótimos (K-Means) — Oil palm fruit vs demais culturas
- ✅ Silhouette Score: 0.243
- ✅ Hierarchical Clustering com mesmo resultado (Silhouette: 0.243)
- ✅ DBSCAN não adequado para este dataset (baixa variabilidade de densidade)

### Modelos Preditivos
- ✅ Regressão Linear: R² = 0.9950 (melhor R² de teste — beneficiada pelo OneHotEncoding)
- ✅ Random Forest: R² = 0.9942 — recomendado para produção (menor MAPE: 7.47%)
- ✅ Gradient Boosting: R² = 0.9913
- ✅ SVR: R² = 0.9397 (corrigido com normalização do target)
- ✅ MLP: R² = 0.9793 (corrigido com normalização do target)

---

## 📝 Notas Importantes

- Certifique-se de ter instalado todas as dependências: `pip install -r requirements.txt`
- O dataset `crop_yield.csv` deve estar na pasta `data/`
- Os notebooks geram visualizações que podem demorar alguns segundos
- O treinamento dos modelos pode levar alguns minutos dependendo do hardware
