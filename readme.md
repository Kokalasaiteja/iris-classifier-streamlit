# 🌸 Iris Classifier – Streamlit App

A simple and interactive **machine learning web application** built with **Streamlit** that classifies iris flower species (*setosa*, *versicolor*, *virginica*) using a trained ML model.

This project demonstrates how to deploy a scikit-learn classifier as an easy-to-use web app.

## 🌐 Live Demo

Check out the live app here: [iris-classifier-app-by-saiteja.streamlit.app](https://iris-classifier-app-by-saiteja.streamlit.app)

---

## 🚀 Features

- 🌼 **Interactive UI** built with Streamlit
- 🤖 **Machine Learning model** (Logistic Regression)
- 📊 **Real-time predictions** based on user inputs
- 💻 **Lightweight, easy to run locally or deploy**

---

## 📂 Project Structure

```
iris-classifier-streamlit-main/
├── app.py                    # Main Streamlit application
├── iris_model.joblib         # Saved ML model (joblib file)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🧠 Model

The app uses a trained **Logistic Regression classifier** on the classic **Iris dataset** from scikit-learn.
**Model test accuracy (holdout): 100.00%**

Typical features used:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

---

## 🧪 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/iris-classifier-streamlit-main.git
cd iris-classifier-streamlit-main
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

---

## 🖥️ Usage

Open the app in your browser (usually http://localhost:8501/)

Adjust the input fields for flower measurements

Click "Predict" to view the predicted iris species

---

## 📦 Deployment

You can deploy this app to:

- Streamlit Cloud
- Railway
- Hugging Face Spaces
- Heroku (with buildpacks)

---

## 🔧 Requirements

The `requirements.txt` includes:

```
streamlit==1.32.0
scikit-learn==1.5.2
numpy>=1.26.0
pandas>=2.2.0
```

---

## 📝 Future Improvements

- Add data visualizations (pairplot, confusion matrix, etc.)
- Add multiple model options
- Add API endpoint for programmatic predictions
- Improve UI with Streamlit themes and custom components

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! If you find an issue, feel free to open one.

---

## ⭐ Acknowledgements

- Iris Dataset: Fisher, 1936
- scikit-learn developers
- Streamlit team
