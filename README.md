# Customer Segmentation Chatbot

This is an interactive Streamlit-based chatbot that classifies customers into distinct segments based on behavioral and financial inputs. It merges clustering-based customer segmentation with a LightGBM classifier to identify whether a customer is a high-value loyalist or a budget-conscious shopper. The chatbot takes user input through a clean interface and provides predictions in real-time.

## Features

- Classifies customers into predefined segments using a trained ML model.
- Minimal, intuitive interface styled with custom CSS.
- Scalable and easy to deploy for marketing teams or analysts.
- Handles preprocessing, scaling, and prediction behind the scenes.

## Technologies Used

- Python
- Streamlit
- LightGBM
- Scikit-learn
- Pandas & NumPy
- Joblib

## How to Run

1. Clone this repository:
<pre>git clone https://github.com/Fizakh3n/Customer-Chatbot-Assistant </pre>
2.Install the required libraries:
<pre>pip install -r requirements.txt</pre>
3.Launch the chatbot:
<pre>streamlit run app.py </pre>


## Model Overview

The model was trained on a marketing dataset. DBSCAN clustering with PCA was used to identify behavioral patterns. The majority clusters were:
- **High-Value Loyalists**: High income, high engagement across campaigns and channels.
- **Budget-Conscious Customers**: Moderate income, low interaction and purchase volume.

A LightGBM classifier was trained on numeric features including income, web/catalog/store purchase behavior, product expenditure, and campaign response. The model was evaluated and tuned before being exported.
