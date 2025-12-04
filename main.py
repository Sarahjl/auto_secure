from data_generator import generate_data
from model_training import train_model, train_model_anonymized, evaluate_model
from privacy import risk_of_identification, apply_k_anonymity, laplace_mechanism
from plots import plot_histograms

# gerar dados
df = generate_data()

# modelo original
clf, prob, pred, y_test = train_model(df)
acc, auc = evaluate_model(prob, pred, y_test)

print("=== Modelo original ===")
print("Acurácia:", acc)
print("ROC AUC:", auc)

# risco de identificação
unicidade = risk_of_identification(df)
print("\n=== Risco de identificação ===")
print(f"Unicidade antes: {unicidade:.2%}")

# K-ANONYMITY
df, kmin = apply_k_anonymity(df)
print(f"k mínimo: {kmin}, prob. máxima de identificar: {1/kmin:.2%}")

clf2, prob2, y_test2 = train_model_anonymized(df)
auc2 = evaluate_model(prob2, prob2 > 0.5, y_test2)[1]

print("\n=== Modelo com K-anonymity ===")
print("ROC AUC:", auc2)

# DIFFERENTIAL PRIVACY
prob_noisy = laplace_mechanism(prob2, epsilon=1.0)
auc_dp = evaluate_model(prob_noisy, prob_noisy > 0.5, y_test2)[1]

print("\n=== Modelo com Differential Privacy ===")
print("ROC AUC:", auc_dp)

# PLOTS
plot_histograms(df)
