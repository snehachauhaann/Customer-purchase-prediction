import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from load_data import load_data

def train_models():
    # Load data from database
    df = load_data()

    # Features and target
    X = df[['age', 'salary']]
    y = df['purchased']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Logistic Regression
    log_model = LogisticRegression()
    log_model.fit(X_train, y_train)
    log_pred = log_model.predict(X_test)
    log_acc = accuracy_score(y_test, log_pred)
    print("Logistic Regression Accuracy:", log_acc)

    # Random Forest
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_pred)
    print("Random Forest Accuracy:", rf_acc)

    return log_model, rf_model, X_train, X_test, y_train, y_test

# Test training
if __name__ == "__main__":
    train_models()
