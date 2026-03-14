# 🏏 Cricket Shot Prediction System

A **Machine Learning based Cricket Shot Prediction Web Application**
that predicts the most likely cricket shot a batsman will play based on
ball characteristics such as speed, line, length, footwork, and shot
angle.

This project demonstrates the **complete machine learning workflow**,
including:

-   Data preprocessing
-   Feature engineering
-   Model training
-   Model serialization
-   Deployment using **Streamlit**

------------------------------------------------------------------------

# 🚀 Project Overview

Cricket is a complex sport where batsmen choose shots depending on
multiple factors such as:

-   Ball speed
-   Ball line
-   Ball length
-   Bowling type
-   Footwork
-   Shot angle
-   Side of play

This project uses **supervised machine learning classification** to
learn patterns between these features and the resulting cricket shot.

The trained model predicts the shot played by the batsman based on the
input features.

------------------------------------------------------------------------

# 📥 Dataset

The dataset used to train the machine learning model can be downloaded
from the following **Kaggle link**:

Dataset Link:\
https://www.kaggle.com/datasets/priyambhattacharya/cricket-shot-prediction/data/settings/settings/data

Steps to download:

1.  Open the Kaggle link above.
2.  Download the dataset.
3.  Place the dataset file inside the project directory.
4.  Run the Jupyter notebook to train the model.

------------------------------------------------------------------------

# 🎯 Features

✔ Interactive **Streamlit Web App**\
✔ Machine Learning based shot classification\
✔ Real-time prediction interface\
✔ Feature preprocessing pipeline\
✔ Model saved using **Joblib**\
✔ Reproducible training using **Jupyter Notebook**

------------------------------------------------------------------------

# 📂 Project Structure

ML_cricket_shot_prediction_app │ ├── shot_prediction.ipynb \# Model
training notebook ├── app.py \# Streamlit application │ ├──
shot_model.pkl \# Trained ML model ├── scaler.pkl \# Feature scaler ├──
label_encoder.pkl \# Label encoder ├── feature_columns.pkl \# Feature
column order │ ├── requirements.txt \# Dependencies └── README.md \#
Project documentation

------------------------------------------------------------------------

# ⚙️ Machine Learning Pipeline

## 1️⃣ Data Preprocessing

Categorical variables are converted into numerical format using **One
Hot Encoding**.

Example:

``` python
pd.get_dummies()
```

------------------------------------------------------------------------

## 2️⃣ Feature Scaling

Numerical features such as **Ball Speed** and **Shot Angle** are
standardized using **StandardScaler**.

``` python
from sklearn.preprocessing import StandardScaler
```

This ensures that all features have comparable magnitudes.

------------------------------------------------------------------------

## 3️⃣ Model Training

A classification model is trained to predict the cricket shot.

Example algorithms:

-   Logistic Regression
-   Random Forest
-   Support Vector Machine
-   Voting Classifier (Ensemble)

The trained model is saved using:

``` python
joblib.dump(model, "shot_model.pkl")
```

------------------------------------------------------------------------

## 4️⃣ Model Deployment

The trained model is deployed using **Streamlit** to build an
interactive web application.

Steps performed in the app:

1.  Accept user input
2.  Convert input to DataFrame
3.  Apply one-hot encoding
4.  Align features with training columns
5.  Scale the input
6.  Predict the shot

------------------------------------------------------------------------

# 🖥️ Running the Application

Clone the repository:

``` bash
git clone https://github.com/itspriyambhattacharya/ML_cricket_shot_prediction_app.git
```

Move into the project directory:

``` bash
cd ML_cricket_shot_prediction_app
```

Create a virtual environment:

``` bash
python -m venv venv
```

Activate the environment.

Windows:

``` bash
venv\Scripts\activate
```

Linux / Mac:

``` bash
source venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run the Streamlit application:

``` bash
streamlit run app.py
```

The app will run at:

http://localhost:8501

------------------------------------------------------------------------

# 📊 Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Joblib
-   Streamlit
-   Matplotlib
-   Seaborn
-   Jupyter Notebook

------------------------------------------------------------------------

# 👨‍💻 Author

**Priyam Bhattacharya**\
M.Sc. Computer Science\
University of Calcutta

GitHub:\
https://github.com/itspriyambhattacharya

------------------------------------------------------------------------

# ⭐ Future Improvements

Possible future enhancements:

-   Deep learning based shot prediction
-   Larger cricket datasets
-   Probability visualization
-   Shot trajectory visualization
-   Real match data integration
