import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score

def train_model(df):
    X = pd.get_dummies(df[['idade', 'genero', 'renda']], drop_first=True)
    y = df['comprou_suv']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1
    )

    clf = RandomForestClassifier(n_estimators=100, random_state=1)
    clf.fit(X_train, y_train)

    prob = clf.predict_proba(X_test)[:, 1]
    pred = (prob > 0.5).astype(int)

    return clf, prob, pred, y_test


def train_model_anonymized(df):
    X = pd.get_dummies(df[['faixa_idade', 'genero', 'renda']], drop_first=True)
    y = df['comprou_suv']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1
    )

    clf = RandomForestClassifier(n_estimators=100, random_state=1)
    clf.fit(X_train, y_train)

    prob = clf.predict_proba(X_test)[:, 1]
    return clf, prob, y_test


def evaluate_model(prob, pred, y_test):
    return accuracy_score(y_test, pred), roc_auc_score(y_test, prob)
