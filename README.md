# **Breast Cancer Analysis using Machine Learning** 🎗️  

## **Overview**  
This project aims to analyze and predict breast cancer using machine learning techniques. The dataset consists of **various tumor characteristics**, and the model predicts whether a tumor is **benign or malignant**.  

## **Features**  
✅ **Data Preprocessing** – Handling missing values, feature scaling, and encoding categorical data.  
✅ **Exploratory Data Analysis (EDA)** – Visualizing the distribution of features and correlations.  
✅ **Machine Learning Models** – Implemented **Random Forest, SVM, Logistic Regression, and Decision Trees**.  
✅ **Model Evaluation** – Accuracy, precision, recall, F1-score, and ROC curve analysis.  
✅ **User Interface** – A simple web app using **Flask / Streamlit** for prediction.  

## **Dataset**  
- **Source:** [Breast Cancer Wisconsin Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)  
- **Features:**  
  - ID, Diagnosis (M = Malignant, B = Benign)  
  - Mean, Standard Error, and Worst values of tumor characteristics:  
    - **Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, Symmetry, Fractal Dimension**  

## **Technologies Used**  
- **Python** (NumPy, Pandas, Matplotlib, Seaborn)  
- **Machine Learning** (Scikit-learn, TensorFlow)  
- **Web Framework** (Flask / Streamlit)  
- **Data Visualization** (Matplotlib, Seaborn)  

## **Installation & Setup**  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/your-username/breast-cancer-analysis.git
   cd breast-cancer-analysis
   ```

2. **Create a virtual environment (optional but recommended):**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the web application:**  
   ```bash
   python app.py
   ```
   OR for Streamlit UI:  
   ```bash
   streamlit run app.py
   ```

5. **Access the web app:**  
   Open your browser and go to `http://127.0.0.1:5000/`  

## **Usage**  
- Upload or input tumor characteristics.  
- The model predicts whether the tumor is **benign or malignant**.  
- View **detailed statistics** and **visualizations**.  

## **Results & Accuracy**  
- **Random Forest:** ~96% Accuracy  
- **Logistic Regression:** ~92% Accuracy  
- **SVM:** ~94% Accuracy  
- **ROC-AUC Score:** High performance in distinguishing between classes.  

## **Future Enhancements**  
🚀 Deploy on **AWS/GCP** for cloud-based analysis.  
🚀 Implement **Deep Learning (CNNs)** for enhanced accuracy.  
🚀 Add **real-time data visualization**.  

-
