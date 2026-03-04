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
| `Yield` | Numérica | **Rendimento da safra (target)** | kg/hectare |

---

## 📈 Estatísticas Gerais

- **Total de registros:** 156
- **Valores nulos:** 0 ✅
- **Duplicatas:** 0 ✅
- **Culturas únicas:** 4 tipos

### Tipos de Culturas:
1. Cocoa, beans (Cacau)
2. Oil palm fruit (Dendê)
3. Rice, paddy (Arroz)
4. Rubber, natural (Borracha natural)

---

## 🔍 Estatísticas das Variáveis

### Precipitation (Precipitação)
- Média: 2.471 mm/dia
- Min: 1.846 mm/dia
- Max: 3.248 mm/dia

### Temperature (Temperatura)
- Média: 26.19°C
- Min: 25.40°C
- Max: 27.10°C

### Yield (Rendimento) - **Variável Alvo**
- Média: 56.302 kg/ha
- Min: 4.569 kg/ha (Cocoa)
- Max: 216.386 kg/ha (Oil palm fruit)
- Desvio padrão: 68.606 kg/ha

**Observação:** Grande variação no rendimento (~47x entre culturas) indica que o tipo de cultura é o fator dominante — Oil palm fruit produz ~20x mais que Cocoa.

---

## 📊 Correlações com Yield

As correlações entre as variáveis climáticas e o rendimento são relativamente baixas:

- Specific Humidity: +0.120
- Precipitation: +0.043
- Relative Humidity: +0.045
- Temperature: -0.109

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
