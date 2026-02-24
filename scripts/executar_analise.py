#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para executar a análise exploratória de dados
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend não-interativo
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy import stats
from sklearn.ensemble import IsolationForest
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("FARMTECH SOLUTIONS - ANALISE EXPLORATORIA DE DADOS")
print("="*80)

# Seed para reprodutibilidade
np.random.seed(42)

# Configuração de visualização
plt.rcParams['figure.figsize'] = (12, 6)
sns.set_style('whitegrid')
sns.set_palette('husl')

print("\n[OK] Bibliotecas importadas com sucesso!\n")

# ============================
# 1. CARREGAMENTO DOS DADOS
# ============================
print("1. CARREGAMENTO DOS DADOS")
print("-" * 80)

df = pd.read_csv('crop_yield.csv')
print(f"[OK] Dataset carregado com sucesso!")
print(f"Dimensoes: {df.shape[0]} linhas, {df.shape[1]} colunas\n")

print("Primeiras 5 linhas:")
print(df.head())
print()

print("Colunas do dataset:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")
print()

# ============================
# 2. INFORMAÇÕES GERAIS
# ============================
print("\n📊 2. INFORMAÇÕES GERAIS")
print("-" * 80)

print("ℹ️ Tipos de dados:")
print(df.dtypes)
print()

print(f"📊 Estatísticas do dataset:")
print(f"  - Total de registros: {len(df):,}")
print(f"  - Total de colunas: {len(df.columns)}")
print(f"  - Valores nulos: {df.isnull().sum().sum()}")
print(f"  - Linhas duplicadas: {df.duplicated().sum()}")
print()

# ============================
# 3. ESTATÍSTICAS DESCRITIVAS
# ============================
print("\n📊 3. ESTATÍSTICAS DESCRITIVAS")
print("-" * 80)

print("\n📈 Estatísticas das variáveis numéricas:")
print(df.describe().T)
print()

print("\n🌾 Análise das Culturas (Crop):")
crop_counts = df['Crop'].value_counts()
print(crop_counts)
print(f"\nTotal de culturas diferentes: {df['Crop'].nunique()}")
print()

# ============================
# 4. ANÁLISE DE CORRELAÇÃO
# ============================
print("\n📊 4. ANÁLISE DE CORRELAÇÃO")
print("-" * 80)

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"Variáveis numéricas: {numeric_cols}\n")

correlation_matrix = df[numeric_cols].corr()
print("\n🔍 Correlações com a variável alvo (Yield):")
correlations_with_yield = correlation_matrix['Yield'].sort_values(ascending=False)
print(correlations_with_yield)
print()

# ============================
# 5. ANÁLISE POR CULTURA
# ============================
print("\n📊 5. ANÁLISE POR CULTURA")
print("-" * 80)

print("\n📈 Estatísticas de Rendimento por Cultura:")
yield_stats = df.groupby('Crop')['Yield'].agg(['count', 'mean', 'std', 'min', 'max']).round(2)
yield_stats.columns = ['Quantidade', 'Média', 'Desvio Padrão', 'Mínimo', 'Máximo']
print(yield_stats.sort_values('Média', ascending=False))
print()

# ============================
# 6. DETECÇÃO DE OUTLIERS
# ============================
print("\n📊 6. DETECÇÃO DE OUTLIERS")
print("-" * 80)

# IQR Method
def detect_outliers_iqr(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

print("\n🔍 Detecção de Outliers usando Método IQR:")
outliers_summary = []
for col in numeric_cols:
    outliers, lower, upper = detect_outliers_iqr(df, col)
    outliers_summary.append({
        'Variável': col,
        'Qtd Outliers': len(outliers),
        'Percentual (%)': round(len(outliers) / len(df) * 100, 2),
        'Limite Inferior': round(lower, 2),
        'Limite Superior': round(upper, 2)
    })

outliers_df = pd.DataFrame(outliers_summary)
print(outliers_df.to_string(index=False))
print()

# Z-Score
print("\n🔍 Detecção de Outliers usando Z-Score (|z| > 3):")
df_numeric = df[numeric_cols].copy()
z_scores = np.abs(stats.zscore(df_numeric))
outliers_zscore = (z_scores > 3).sum(axis=0)

zscore_summary = pd.DataFrame({
    'Variável': numeric_cols,
    'Outliers (Z-Score)': outliers_zscore.values,
    'Percentual (%)': (outliers_zscore.values / len(df) * 100).round(2)
})
print(zscore_summary.to_string(index=False))
print()

# Isolation Forest
print("\n🔍 Detecção de Outliers usando Isolation Forest:")
X_outlier = df[numeric_cols].copy()
iso_forest = IsolationForest(contamination=0.1, random_state=42, n_estimators=100)
outlier_predictions = iso_forest.fit_predict(X_outlier)

n_outliers_iso = (outlier_predictions == -1).sum()
print(f"Quantidade de outliers detectados: {n_outliers_iso}")
print(f"Percentual: {(n_outliers_iso/len(df)*100):.2f}%")
print()

df['is_outlier'] = outlier_predictions == -1
print("Outliers por cultura:")
print(df.groupby('Crop')['is_outlier'].sum().sort_values(ascending=False))
print()

# ============================
# 7. RESUMO FINAL
# ============================
print("\n" + "="*80)
print("📊 RESUMO DA ANÁLISE EXPLORATÓRIA")
print("="*80)

print(f"\n1. QUALIDADE DOS DADOS:")
print(f"   - Total de registros: {len(df):,}")
print(f"   - Valores nulos: {df.isnull().sum().sum()}")
print(f"   - Linhas duplicadas: {df.duplicated().sum()}")
print(f"   ✅ Dataset limpo e pronto para modelagem!")

print(f"\n2. CULTURAS:")
print(f"   - Número de culturas diferentes: {df['Crop'].nunique()}")
print(f"   - Culturas: {df['Crop'].unique().tolist()}")

print(f"\n3. RENDIMENTO (YIELD):")
print(f"   - Média geral: {df['Yield'].mean():.2f}")
print(f"   - Desvio padrão: {df['Yield'].std():.2f}")
print(f"   - Mínimo: {df['Yield'].min():.2f}")
print(f"   - Máximo: {df['Yield'].max():.2f}")

print(f"\n4. CORRELAÇÕES COM YIELD:")
top_correlations = correlation_matrix['Yield'].drop('Yield').sort_values(ascending=False)
for var, corr in top_correlations.items():
    print(f"   - {var}: {corr:.3f}")

print(f"\n5. OUTLIERS:")
print(f"   - Total de outliers detectados (Isolation Forest): {n_outliers_iso} ({(n_outliers_iso/len(df)*100):.2f}%)")

print("\n" + "="*80)
print("✅ ANÁLISE EXPLORATÓRIA CONCLUÍDA COM SUCESSO!")
print("="*80)

print("\n🎯 PRÓXIMOS PASSOS:")
print("  1. Análise de Clusterização (K-Means, DBSCAN, Hierarchical)")
print("  2. Desenvolvimento de 5 Modelos Preditivos de Regressão")
print("  3. Avaliação e Comparação dos Modelos (R², RMSE, MAE, MAPE)")
