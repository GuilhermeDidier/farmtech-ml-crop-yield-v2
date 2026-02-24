# 📁 Dados do Projeto

Este diretório contém os datasets utilizados no projeto.

## 📊 Datasets

### `crop_yield.csv` (Dataset Original)

**Descrição:** Dataset com informações de rendimento de safras em uma fazenda de 200 hectares.

**Dimensões:** 156 linhas × 6 colunas

**Variáveis:**

| Coluna | Tipo | Descrição | Unidade |
|--------|------|-----------|---------|
| `Crop` | Categórica | Tipo de cultura/safra | - |
| `Precipitation (mm day-1)` | Numérica | Precipitação diária | mm/dia |
| `Specific Humidity at 2 Meters (g/kg)` | Numérica | Umidade específica a 2m | g/kg |
| `Relative Humidity at 2 Meters (%)` | Numérica | Umidade relativa a 2m | % |
| `Temperature at 2 Meters (C)` | Numérica | Temperatura a 2m | °C |
| `Yield` | Numérica | **Rendimento da safra (target)** | toneladas/hectare |

---

## 📈 Estatísticas Gerais

- **Total de registros:** 156
- **Valores nulos:** 0 ✅
- **Duplicatas:** 0 ✅
- **Culturas únicas:** 4 tipos

### Tipos de Culturas:
1. Cocoa, beans (Cacau)
2. Coffee, green (Café)
3. Tea (Chá)
4. Cassava (Mandioca)

---

## 🔍 Estatísticas das Variáveis

### Precipitation (Precipitação)
- Média: 2,486 mm/dia
- Min: 1,935 mm/dia
- Max: 3,086 mm/dia

### Temperature (Temperatura)
- Média: 25.5°C
- Min: 24.1°C
- Max: 27.1°C

### Yield (Rendimento) - **Variável Alvo**
- Média: 56,153 ton/ha
- Mediana: 18,871 ton/ha
- Min: 5,249 ton/ha
- Max: 203,399 ton/ha
- Desvio padrão: 70,422 ton/ha

**Observação:** Grande variação no rendimento indica diferentes tipos de culturas com produtividades muito distintas.

---

## 📊 Correlações com Yield

As correlações entre as variáveis climáticas e o rendimento são relativamente baixas:

- Precipitation: 0.019
- Temperature: 0.013
- Specific Humidity: 0.013
- Relative Humidity: 0.000

**Interpretação:** O tipo de cultura (`Crop`) é o fator mais importante para o rendimento, mais do que as condições climáticas.

---

## 🎯 Uso dos Dados

Este dataset é utilizado para:

1. **Análise Exploratória:** Compreender padrões e distribuições
2. **Clusterização:** Identificar grupos de rendimento similares
3. **Modelagem Preditiva:** Treinar modelos de regressão para prever o rendimento

---

## 📝 Observações

- Todos os dados são numéricos, exceto `Crop` (categórica)
- Não há valores negativos
- Dataset está limpo e pronto para uso
- Dados já foram normalizados/padronizados nos notebooks quando necessário

---

## 🔗 Fonte

Dataset fornecido como parte do projeto acadêmico da FIAP - Fase 5.
