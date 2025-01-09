# IMDb Sentiment Analysis

A machine learning project that predicts whether a given text sentiment is positive or negative. This project is based on the IMDb movie reviews dataset and includes a sentiment analysis model served through a Streamlit web application.

## Watch the Video 📺

[![YouTube Video](https://img.shields.io/badge/YouTube-Watch%20Video-red?logo=youtube&logoColor=white&style=for-the-badge)](https://www.youtube.com/watch?v=uAz2i5CFa0c&t=674s)

---

## 🎯 Project Overview
This project involves:
- **Dataset**: IMDb dataset for training and testing the sentiment analysis model.
- **Notebook**: A Jupyter Notebook used for preprocessing data, training the model, and evaluation.
- **Streamlit App**: An interactive web application where users can input text and receive sentiment predictions (positive/negative).
- **Saved Models**: Pre-trained machine learning models and tokenizers saved in `.pkl` format for inference.

---

## 🗂 Project Structure

```
├── IMDB dataset.csv              # Dataset containing IMDb movie reviews
├── IMDB_Sentiment_analysis.ipynb # Jupyter Notebook for model training and evaluation
├── app.py                        # Streamlit web app for sentiment prediction
├── model.pkl                     # Serialized trained sentiment analysis model
├── tokenizer.pkl                 # Tokenizer used in preprocessing
└── README.md                     # Documentation (you're reading this!)
```

---

## 🚀 How to Run the Project

### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/Text-Sentiment-Analysis-Project.git
cd Text-Sentiment-Analysis-Project
```

### 2. **Install Required Dependencies**
Create a Python virtual environment and install the dependencies listed in `requirements.txt`.:

To install dependencies:
```bash
pip install -r requirements.txt
```

### 3. **Run the Streamlit App**
Start the Streamlit app to test the sentiment prediction:
```bash
streamlit run app.py
```
This will launch a local web page where you can input text and view the model's sentiment predictions.

---

## 📈 Workflow Details

### 1. **Dataset**
The dataset (`IMDB dataset.csv`) contains IMDb movie reviews, labeled as positive or negative. It serves as the basis for training and evaluation.

### 2. **Model Training**
The machine learning workflow for this project includes:
- **Data Preprocessing**: Tokenization, stop-word removal, HTML-tags removal and text vectorization.
- **Modeling**: A classification model built using libraries like Scikit-learn, TensorFlow.
- **Serialization**: The trained model and tokenizer are saved as `model.pkl` and `tokenizer.pkl` respectively, to be used for inference.

### 3. **Interactive Web App**
The Streamlit web app (`app.py`) allows users to:
1. Enter custom text inputs.
2. Receive predictions (positive/negative sentiment) powered by the trained model.

---

## 🛠 Technologies Used
- **Languages**: Python
- **Libraries**:
  - Machine Learning: Scikit-learn, TensorFlow/Keras
  - Data Handling: Pandas, NumPy
  - Visualization: Matplotlib, Seaborn
  - Web App: Streamlit
- **Tools**: Jupyter Notebook, Git, Virtual Environment

---

## 📊 Results
- **Accuracy**: 87.55% (calculated on the test dataset)
---

## 🌐 Web App Screenshots
Add some screenshots of your Streamlit app to make your project visually appealing.

![Screenshot 2025-01-06 153328](https://github.com/user-attachments/assets/361c9fe9-42e1-454c-918a-cf335dab938f)



---

## 🤝 Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to:
1. Fork the repo
2. Create a branch
3. Submit a Pull Request

---

## 📄 License
This project is licensed under the MIT License.

---

## 💡 Acknowledgments
- Kaggle for providing the dataset.
- [Streamlit](https://streamlit.io/) for simplifying the web application deployment.

---

## 📞 Contact
For any questions or feedback:
- Email: nikzmishra@gmail.com
- Youtube: [Your Channel](https://www.youtube.com/@DataScienceSensei/videos)

---
**⭐ If you found this project helpful, give it a star! ⭐**
