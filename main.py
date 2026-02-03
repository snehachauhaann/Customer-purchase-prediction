from model import train_models
import numpy as np

def main():
    # Train models
    log_model, rf_model, X_train, X_test, y_train, y_test = train_models()

    print("\n--- Customer Purchase Prediction ---")
    # Take user input
    age = int(input("Enter customer age: "))
    salary = int(input("Enter customer salary: "))

    new_customer = np.array([[age, salary]])

    # Predict using Random Forest (can also use Logistic Regression)
    prediction = rf_model.predict(new_customer)

    if prediction == 1:
        print("Prediction: Customer WILL purchase.")
    else:
        print("Prediction: Customer will NOT purchase.")

if __name__ == "__main__":
    main()
