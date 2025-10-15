# 📦 Tipos de Materiais - Nexum Supply Chain

## Classificação de Materiais

O sistema Nexum utiliza 3 tipos principais de classificação de materiais, baseados em sua capacidade de reparação e reutilização:

---

## 🔧 Tipo 10 - REPARÁVEL (T-10)

**Características:**
- Peças **100% reparáveis**
- Podem ser consertadas e retornar ao estoque
- Alta prioridade para gestão de ciclo de vida

**Cálculo de Saldo Total:**
```
Saldo Total = Peças Boas + Peças em Teste + Peças para Reparo - Perdas Estimadas
```

**Componentes do Saldo:**
- `saldo_manut`: Peças boas prontas para uso
- `pecas_teste_kit` + `pecas_teste`: Peças sendo testadas
- `fornecedor_reparo` + `laboratorio` + `wr`: Peças em processo de reparo
- `coef_perda`: Coeficiente de perda aplicado sobre peças em reparo

**Exemplo:**
- Saldo bom: 50
- Em teste: 20
- Em reparo: 30
- Coef. perda: 0.1 (10%)
- **Saldo Total = 50 + 20 + 30 - (30 × 0.1) = 97**

---

## 🧪 Tipo 19 - TESTÁVEL (T-19)

**Características:**
- Peças **passíveis de teste**
- Podem ser aprovadas ou reprovadas após teste
- Requerem validação antes de retornar ao uso

**Cálculo de Saldo Total:**
```
Saldo Total = Peças Boas + Peças em Teste + Peças para Reparo - Perdas Estimadas
```

**Componentes do Saldo:**
- Mesmo cálculo do Tipo 10 (reparável)
- Diferença está no processo: teste → aprovação → uso

**Exemplo:**
- Saldo bom: 30
- Em teste: 50
- Em reparo: 10
- Coef. perda: 0.05 (5%)
- **Saldo Total = 30 + 50 + 10 - (10 × 0.05) = 89.5**

---

## 🗑️ Tipo 20 - DESCARTÁVEL (T-20)

**Características:**
- Peças **descartadas após consumo**
- NÃO podem ser reparadas ou reutilizadas
- Uso único

**Cálculo de Saldo Total:**
```
Saldo Total = Apenas Peças Boas
```

**Componentes do Saldo:**
- `saldo_manut`: Único campo considerado
- Peças em teste/reparo **NÃO são somadas**

**Exemplo:**
- Saldo bom: 100
- Em teste: 20 (❌ ignorado)
- Em reparo: 15 (❌ ignorado)
- **Saldo Total = 100**

---

## 📊 Comparação Rápida

| Aspecto | T-10 Reparável | T-19 Testável | T-20 Descartável |
|---------|----------------|---------------|------------------|
| **Emoji** | 🔧 | 🧪 | 🗑️ |
| **Reutilizável?** | ✅ Sim | ✅ Sim (após teste) | ❌ Não |
| **Soma peças em teste?** | ✅ Sim | ✅ Sim | ❌ Não |
| **Soma peças em reparo?** | ✅ Sim | ✅ Sim | ❌ Não |
| **Aplica coef. perda?** | ✅ Sim | ✅ Sim | ❌ Não |
| **Complexidade** | Alta | Alta | Baixa |

---

## 🎯 Uso na API

### Endpoint de Tipos
```http
GET /api/produtos/tipos
```

**Resposta:**
```json
{
  "success": true,
  "tipos": [
    {
      "codigo": 10,
      "nome": "reparavel",
      "descricao": "Peças 100% reparáveis",
      "emoji": "🔧",
      "calculo_saldo": "saldo + peças_teste + peças_reparo - perdas"
    },
    // ...
  ]
}
```

### Filtrar por Tipo
```http
GET /api/produtos/?tipo=10  # Apenas reparáveis
GET /api/produtos/?tipo=19  # Apenas testáveis
GET /api/produtos/?tipo=20  # Apenas descartáveis
```

---

## 💡 Dicas de Gestão

### Para Tipo 10 (Reparável):
- Monitore peças em reparo
- Otimize processo de conserto
- Reduza coeficiente de perda

### Para Tipo 19 (Testável):
- Agilize processo de testes
- Aprove rapidamente peças OK
- Descarte rápido de peças ruins

### Para Tipo 20 (Descartável):
- Foco em previsão de demanda
- Gestão de estoque just-in-time
- Evite excesso de estoque

---

**Documentação atualizada em:** 15/10/2025  
**Sistema:** Nexum Supply Chain Backend
