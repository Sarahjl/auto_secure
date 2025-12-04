# AutoSecure 
**Recomendador de carros com Machine Learning e privacidade**

---

## Visão Geral

**AutoSecure** é um projeto de demonstração que utiliza **machine learning** para prever o interesse de clientes em determinados tipos de carros, preservando totalmente a privacidade pessoal.

A aplicação simula dados de um marketplace de carros (idade, renda, comportamento de navegação, preferências etc.) para:
- treinar um modelo preditivo (Random Forest);
- medir risco de identificação de indivíduos;
- aplicar **anonimização (k-anonymity)** e **ruído diferencial (Differential Privacy)**;
- provar estatisticamente que **não é possível identificar uma pessoa individualmente** nos dados utilizados.

---

## Objetivo

Demonstrar que é possível:
1. Usar dados pessoais **de forma ética e agregada** para direcionar compras (ex: recomendar SUVs ou sedãs);
2. **Manter utilidade dos dados** para o modelo;
3. Garantir **não-identificabilidade** através de regras estatísticas simples (ex: k-anonymity).

## Integrantes

- Ana Luísa Augusto do Val
- João Enrique Barbosa Santos Alves
- Sarah Jandozza Laurindo

# Saída
```
=== Modelo original ===
Acurácia: 0.5133333333333333
ROC AUC: 0.5123456790123457

=== Risco de identificação ===
Unicidade antes: 0.80%
k mínimo: 36, promáxima de identificar: 2.78%

=== Modelo com K-anonymity ===
ROC AUC: 0.4961531579889068

=== Modelo com Differential Privacy ===
ROC AUC: 0.49409554482018253
```

<img width="1018" height="478" alt="image" src="https://github.com/user-attachments/assets/1587f1c6-37e5-42de-a49a-bdf96b31fa96" />

# Baixar executar
```cmd
git clone https://github.com/Sarahjl/auto_secure
cd auto_secure
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
