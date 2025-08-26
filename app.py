import streamlit as st
import joblib
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Train model if not exists
# -----------------------------
MODEL_FILE = "iris_model.joblib"

if not os.path.exists(MODEL_FILE):
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_FILE)

# Load trained model
model = joblib.load(MODEL_FILE)

# Iris dataset (for class names)
iris = load_iris()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🌸 Iris Flower Classifier")
st.write("Enter flower measurements and get the predicted species.")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

if st.button("Predict"):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)[0]
    species = iris.target_names[prediction]
    st.success(f"🌼 Predicted Species: **{species}**")