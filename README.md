# ecommerce-data-analyst
analyst data e-commerce

# Description
This project is a Streamlit-based web application for e-commerce data analysis. The application provides tools for performing exploratory data analysis (EDA) on various datasets related to customers, orders, payments, reviews and products in the e-commerce domain. It also provides visualizations and statistical insights based on the data.

# Key Features
- The application loads a variety of datasets, including customer information, geolocation data, order items, order payments, product categories, and other relevant data.
- Display sample data: Users are able to select a dataset and view the top rows of data in order to gain an understanding of its structure.
- Exploratory Data Analysis (EDA): The application offers users the ability to access general statistics, histograms, and correlation analysis for selected datasets.
- RFM (Recency, Frequency, Monetary) Analysis: The RFM analysis tool allows users to gain insight into customer behaviour and relationships between different metrics.
- The distribution of payment values is as follows: A histogram showing the distribution of payment amounts.
  - Correlation Heatmap: A heatmap illustrating the correlations between recency, frequency, and monetary values.
  - Product Rating by Category: A bar chart showing the average product ratings grouped by category.
  - Sales by Product Category: A bar chart showing the total number of sales by product category.
  - Product Rating Distribution: A count plot visualising the distribution of product ratings.
- Conclusions: Summarises key insights from the analysis, including customer behaviour and product performance.
  
# Installation
- Clone Repository
  Using git clone https://github.com/nrnfadya/ecommerce-data-analyst
- Install Dependencies
  Using pip for install the required libraries
- Prepare the Datasets
  - customers_dataset.csv
  - geolocation_dataset.csv
  - order_items_dataset.csv
  - order_payments_dataset.csv
  - order_reviews_dataset.csv
  - orders_dataset.csv
  - product_category_name_translation.csv
  - products_dataset.cs
  - sellers_dataset.csv

# Dependencies
In order to run the application, the following libraries are required:
- streamlit
- pandas
- seaborn
- matplotlib
- os

# Running the Application
- running application with streamlit in the terminal app.py
  streamlit run app.py
- using link from cloning with streamlit https://ecommerce-data-analyst-cspmehjurjzwugh9xq5duf.streamlit.app/

# Applocation Structure
- Title: The main page title is displayed as E-Commerce Data Analyst.
- Loading Data The datasets include information about customers, order items, payments, product categories, and more.
- Display Sample Data
There is a dropdown selection that allows you to choose a dataset and view its first few rows. The datasets available for viewing include Customers, Geolocation, Orders, Products, and more.
- Exploratory Data Analysis (EDA)
Specific datasets (Customers, Order Items, Order Payments, Order Reviews) can be selected to display statistical summaries using the describe() method.
- Distribution of Payment Values
This histogram shows the distribution of payment values across orders, with a Kernel Density Estimation (KDE) curve for visualising the frequency distribution. This tool enables the analysis of customer behaviour based on their purchase patterns.
-  Product Rating by Category
This displays the average rating per product category in a bar chart format. This enables the identification of product categories with the highest levels of customer satisfaction.
- Sales by Product Category
A bar chart visualising the total sales per product category. This provides an overall indication of customer satisfaction with their purchases.

# Folder Structure
ecommerce-data-analyst/
│
├── data/                           # Folder containing all the datasets
│   ├── customers_dataset.csv
│   ├── geolocation_dataset.csv
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── orders_dataset.csv
│   ├── product_category_name_translation.csv
│   ├── products_dataset.csv
│   ├── sellers_dataset.csv
│
├── app.py                          # Main application code
├── requirements.txt                # Required libraries
├── README.md                       # Project documentation


